from __future__ import print_function, unicode_literals

import logging
import os.path
import string
import unicodedata

import pkg_resources

import panphon
import regex as re
import unicodecsv as csv
from epitran.ligaturize import ligaturize

import sys
if os.name == 'posix' and sys.version_info[0] < 3:
    import subprocess32 as subprocess
else:
    import subprocess

logging.basicConfig(level=logging.CRITICAL)
logging.disable(logging.DEBUG)


if sys.version_info[0] == 3:
    def unicode(x):
        return x


class Flite(object):
    def __init__(self, darpabet='darpabet', ligatures=False):
        darpabet = pkg_resources.resource_filename(__name__, os.path.join('data', darpabet + '.csv'))
        self.darpa_map = self._read_darpabet(darpabet)
        self.chunk_re = re.compile(r'(\p{L}+|[^\p{L}]+)', re.U)
        self.puncnorm = self._load_punc_norm_map()
        self.puncnorm_vals = self.puncnorm.values()
        self.ligatures = ligatures

    def _read_darpabet(self, darpabet):
        darpa_map = {}
        with open(darpabet, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            for darpa, ipa in reader:
                darpa_map[darpa] = ipa
        return darpa_map

    def _load_punc_norm_map(self):
        """Load the map table for normalizing 'down' punctuation."""
        path = pkg_resources.resource_filename(__name__, 'data/puncnorm.csv')
        with open(path, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8', delimiter=str(','), quotechar=str('"'))
            next(reader)
            return {punc: norm for (punc, norm) in reader}

    def normalize_punc(self, text):
        new_text = []
        for c in text:
            if c in self.puncnorm:
                new_text.append(self.puncnorm[c])
            else:
                new_text.append(c)
        return u''.join(new_text)

    def normalize(self, text):
        text = unicode(text)
        text = unicodedata.normalize('NFD', text)
        text = ''.join(filter(lambda x: x in string.printable, text))
        return text

    def darpa_to_ipa(self, darpa_text):
        darpa_text = darpa_text.strip()
        darpa_list = darpa_text.split(' ')[1:-1]  # remove pauses
        darpa_list = map(lambda d: re.sub('\d', '', d), darpa_list)
        ipa_list = map(lambda d: self.darpa_map[d], darpa_list)
        return ''.join(ipa_list)

    def english_g2p(self, text):
        text = self.normalize(text)
        try:
            darpa_text = subprocess.check_output(['t2p', '"{}"'.format(text)])
            darpa_text = darpa_text.decode('utf-8')
        except subprocess.CalledProcessError:
            logging.warning('Non-zero exit status from flite.')
            darpa_text = ''
        return self.darpa_to_ipa(darpa_text)

    def transliterate(self, text, normpunc=False, ligatures=False):
        text = unicodedata.normalize('NFC', text)
        acc = []
        for chunk in self.chunk_re.findall(text):
            if unicodedata.category(chunk[0])[0] == 'L':
                acc.append(self.english_g2p(chunk))
            else:
                acc.append(chunk)
        acc = map(ligaturize, acc) if ligatures or self.ligatures else acc
        return ''.join(acc)


class VectorsWithIPASpace(object):
    def __init__(self, code='eng-Latn', space_name='eng-Latn'):
        self.flite = Flite()
        self.ft = panphon.FeatureTable()
        self.space = self._load_space(space_name)
        self.darpa2ipa = self._load_darpa2ipa_map()
        self.regexp = self._compile_regexp()
        self.num_panphon_fts = len(self.ft.names)

    def _load_space(self, space_name):
        space_fn = os.path.join('data', 'space', space_name + '.csv')
        space_fn = pkg_resources.resource_filename(__name__, space_fn)
        with open(space_fn, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            return {seg: num for (num, seg) in reader}

    def _load_darpa2ipa_map(self):
        darpa2ipa = {}
        path = os.path.join('data', 'darpabet.csv')
        path = pkg_resources.resource_filename(__name__, path)
        with open(path, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            next(reader)
            for darpa, phon in reader:
                darpa2ipa[darpa] = phon
        return darpa2ipa

    def _compile_regexp(self):
        regex = r'({})'.format('|'.join([v for v in self.darpa2ipa.values()]))
        return re.compile(regex, re.U)

    def word_to_segs(self, word, normpunc=False):
        """Returns feature vectors, etc. for segments and punctuation in a word.

        word -- Unicode string representing a word in the orthography specified
                when the class is instantiated.
        return -- a list of tuples, each representing an IPA segment or a
                  punctuation character. Tuples consist of <category, lettercase,
                  orthographic_form, phonetic_form, id, feature_vector>.

        Category consists of the standard Unicode classes (e.g. 'L' for letter
        and 'P' for punctuation). Case is binary: 1 for uppercase and 0 for
        lowercase.
        """

        def cat_and_cap(c):
            cat, case = tuple(unicodedata.category(c))
            case = 1 if case == 'u' else 0
            return unicode(cat), case

        def recode_ft(ft):
            if ft == '+':
                return 1
            elif ft == '0':
                return 0
            elif ft == '-':
                return -1

        def vec2bin(vec):
            return map(recode_ft, vec)

        def to_vector(seg):
            if seg == '':
                return [0] * self.num_panphon_fts
            else:
                return vec2bin(self.ft.segment_to_vector(seg))

        def to_space(seg):
            if seg in self.space:
                return int(self.space[seg])
            else:
                return -1

        tuples = []
        _, capitalized = cat_and_cap(word[0])
        first = True
        trans = self.flite.transliterate(word, normpunc)
        while trans:
            match = self.ft.seg_regex.match(trans)
            if match:
                span = match.group(1)
                case = capitalized if first else 0
                first = False
                logging.debug(u'span = "{}" (letter)'.format(span))
                tuples.append(('L', case, span, span, to_space(span), to_vector(span)))
                trans = trans[len(span):]
                logging.debug(u'trans = "{}" (letter)'.format(trans))
            else:
                span = trans[0]
                logging.debug('span = "{}" (non-letter)'.format(span))
                span = self.normalize_punc(span) if normpunc else span
                cat, case = cat_and_cap(span)
                cat = 'P' if normpunc and cat in self.puncnorm else cat
                tuples.append((cat, case, span, '', to_space(span), to_vector('')))
                trans = trans[1:]
                logging.debug(u'trans = "{}" (non-letter)'.format(trans))
        return tuples
