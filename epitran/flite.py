# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

import logging
import os.path
import string
import unicodedata

import pkg_resources

import panphon
import regex as re
import unicodecsv as csv
from epitran.puncnorm import PuncNorm
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
    """English G2P using the Flite speech synthesis system."""
    def __init__(self, arpabet='arpabet', ligatures=False, cedict_file=None):
        """Construct a Flite "wrapper"

        Args:
            arpabet (str): file containing ARPAbet to IPA mapping
            ligatures (bool): if True, use non-standard ligatures instead of
                              standard IPA
            cedict_filename (str): path to CC-CEDict dictionary (included for
                                   compatibility)
        """
        arpabet = pkg_resources.resource_filename(__name__, os.path.join('data', arpabet + '.csv'))
        self.arpa_map = self._read_arpabet(arpabet)
        self.chunk_re = re.compile(ur"([A-Za-z'’]+|[^A-Za-z'’]+)", re.U)
        self.letter_re = re.compile(ur"[A-Za-z'’]+")
        self.puncnorm = PuncNorm()
        self.ligatures = ligatures
        self.ft = panphon.FeatureTable()

    def _read_arpabet(self, arpabet):
        arpa_map = {}
        with open(arpabet, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            for arpa, ipa in reader:
                arpa_map[arpa] = ipa
        return arpa_map

    def normalize(self, text):
        text = unicode(text)
        text = unicodedata.normalize('NFD', text)
        text = ''.join(filter(lambda x: x in string.printable, text))
        return text

    def arpa_text_to_list(self, arpa_text):
        return arpa_text.split(' ')[1:-1]

    def arpa_to_ipa(self, arpa_text, ligatures=False):
        arpa_text = arpa_text.strip()
        arpa_list = self.arpa_text_to_list(arpa_text)
        arpa_list = map(lambda d: re.sub('\d', '', d), arpa_list)
        ipa_list = map(lambda d: self.arpa_map[d], arpa_list)
        text = ''.join(ipa_list)
        return text

    def transliterate(self, text, normpunc=False, ligatures=False):
        """Convert English text to IPA transcription

        Args:
            text (unicode): English text
            normpunc (bool): if True, normalize punctuation downward
            ligatures (bool): if True, use non-standard ligatures instead of
                              standard IPA
        """
        text = unicodedata.normalize('NFC', text)
        acc = []
        for chunk in self.chunk_re.findall(text):
            if self.letter_re.match(chunk):
                acc.append(self.english_g2p(chunk))
            else:
                acc.append(chunk)
        text = ''.join(acc)
        text = self.puncnorm.norm(text) if normpunc else text
        text = ligaturize(text) if ligatures else text
        return text

    def strict_trans(self, text, normpunc=False, ligatures=False):
        return self.transliterate(text, normpunc, ligatures)

    def word_to_tuples(self, word, normpunc=False):
        """Given a word, returns a list of tuples corresponding to IPA segments.

        Args:
            word (unicode): word to transliterate
            normpunc (bool): If True, normalizes punctuation to ASCII inventory

        Returns:
            list: A list of (category, lettercase, orthographic_form,
                  phonetic_form, feature_vectors) tuples.

        The "feature vectors" form a list consisting of (segment, vector) pairs.
        For IPA segments, segment is a substring of phonetic_form such that the
        concatenation of all segments in the list is equal to the phonetic_form.
        The vectors are a sequence of integers drawn from the set {-1, 0, 1}
        where -1 corresponds to '-', 0 corresponds to '0', and 1 corresponds to
        '+'.
        """
        def cat_and_cap(c):
            cat, case = tuple(unicodedata.category(c))
            case = 1 if case == 'u' else 0
            return unicode(cat), case

        def recode_ft(ft):
            try:
                return {'+': 1, '0': 0, '-': -1}[ft]
            except KeyError:
                return None

        def vec2bin(vec):
            return map(recode_ft, vec)

        def to_vector(seg):
            return seg, vec2bin(self.ft.segment_to_vector(seg))

        def to_vectors(phon):
            if phon == '':
                return [(-1, [0] * self.num_panphon_fts)]
            else:
                return [to_vector(seg) for seg in self.ft.segs(phon)]

        tuples = []
        word = unicode(word)
        # word = self.strip_diacritics.process(word)
        word = unicodedata.normalize('NFKD', word)
        word = unicodedata.normalize('NFC', word)
        while word:
            match = re.match('[A-Za-z]+', word)
            if match:
                span = match.group(0)
                cat, case = cat_and_cap(span[0])
                phonword = self.transliterate(span)
                phonsegs = self.ft.segs(phonword)
                maxlen = max(len(phonsegs), len(span))
                orth = list(span) + [''] * (maxlen - len(span))
                phonsegs += [''] * (maxlen - len(phonsegs))
                for p, o in zip(phonsegs, orth):
                    tuples.append(('L', case, o, p, to_vectors(p)))
                word = word[len(span):]
            else:
                span = word[0]
                span = self.puncnorm.norm(span) if normpunc else span
                cat, case = cat_and_cap(span)
                cat = 'P' if normpunc and cat in self.puncnorm else cat
                phon = ''
                vecs = to_vectors(phon)
                tuples.append((cat, case, span, phon, vecs))
                word = word[1:]
        return tuples


class FliteT2P(Flite):
    """Flite G2P using t2p."""

    def english_g2p(self, text):
        text = self.normalize(text)
        try:
            arpa_text = subprocess.check_output(['t2p', '"{}"'.format(text)])
            arpa_text = arpa_text.decode('utf-8')
        except OSError:
            logging.warning('t2p (from flite) is not installed.')
            arpa_text = ''
        except subprocess.CalledProcessError:
            logging.warning('Non-zero exit status from t2p.')
            arpa_text = ''
        return self.arpa_to_ipa(arpa_text)


class FliteLexLookup(Flite):
    """Flite G2P using lex_lookup."""

    def arpa_text_to_list(self, arpa_text):
        return arpa_text[1:-1].split(' ')

    def english_g2p(self, text):
        text = self.normalize(text).lower()
        try:
            arpa_text = subprocess.check_output(['lex_lookup', text])
            arpa_text = arpa_text.decode('utf-8')
        except OSError:
            logging.warning('lex_lookup (from flite) is not installed.')
            arpa_text = ''
        except subprocess.CalledProcessError:
            logging.warning('Non-zero exit status from lex_lookup.')
            arpa_text = ''
        return self.arpa_to_ipa(arpa_text)
