from __future__ import print_function, unicode_literals

import logging
import os.path
import string
import unicodedata

import pkg_resources

import regex as re
import subprocess32 as subprocess
import unicodecsv as csv

logging.basicConfig(level=logging.DEBUG)


class Flite(object):
    def __init__(self, darpabet='darpabet'):
        darpabet = pkg_resources.resource_filename(__name__, os.path.join('data', darpabet + '.csv'))
        self.darpa_map = self._read_darpabet(darpabet)
        self.puncnorm = self._load_punc_norm_map()
        self.puncnorm_vals = self.puncnorm.values()

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
            reader.next()
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
        ipa_list = map(lambda d: self.darpa_map[d], darpa_list)
        return ''.join(ipa_list)

    def english_g2p(self, text):
        text = self.normalize(text)
        try:
            darpa_text = subprocess.check_output(['flite', '-ps', '-o', '/dev/null', '-t', '"{}"'.format(text)])
        except subprocess.CalledProcessError:
            logging.warning('Non-zero exit status from flite.')
            darpa_text = ''
        return self.darpa_to_ipa(darpa_text)

    def transliterate(self, text, normpunc=False):
        chunk_re = re.compile(r'(\p{L}+|[^\p{L}]+)', re.U)
        text = unicodedata.normalize('NFC', text)
        acc = []
        for chunk in chunk_re.findall(text):
            if unicodedata.category(chunk[0])[0] == 'L':
                acc.append(self.english_g2p(chunk))
            else:
                acc.append(chunk)
        return ''.join(acc)


class VectorsWithIPASpace(object):
    def __init__(self, code='eng-Latn', space_name='eng-Latn'):
        self.flite = Flite()
        self.space = self._load_space(space_name)

    def _load_space(self, space_name):
        space_fn = os.path.join('data', 'space', space_name + '.csv')
        space_fn = pkg_resources.resource_filename(__name__, space_fn)
        with open(space_fn, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            return {seg: num for (num, seg) in reader}

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

        def cat(c):
            return unicodedata.category(c)[0]

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
            return seg, vec2bin(self.ft.segment_to_vector(seg))

        def to_vectors(phon):
            if phon == u'':
                return [(-1, [0] * self.num_panphon_fts)]
            else:
                return [to_vector(seg) for seg in self.ft.segs(phon)]

        def to_space(seg):
            if seg in self.space:
                return self.space[seg]
            else:
                return -1

        segs = []
        word = self.normalize(word)
        if normpunc:
            word = self.flite.normalize_punc(word)
        while word:
            while cat(word[0]) != 'L':
                pass
            while cat(word[0]) == 'L':
                pass
