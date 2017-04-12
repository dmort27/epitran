# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

import logging
import os.path
import sys
import unicodedata
from collections import defaultdict

import pkg_resources

import panphon
import regex as re
import unicodecsv as csv
from epitran.puncnorm import PuncNorm
from epitran.flite import FliteLexLookup
from epitran.epihan import Epihan
from epitran.epihan import EpihanTraditional
from epitran.ppprocessor import PrePostProcessor
from epitran.stripdiacritics import StripDiacritics
from epitran.ligaturize import ligaturize
from epitran.xsampa import XSampa

if sys.version_info[0] == 3:
    def unicode(x):
        return x
logging.basicConfig(level=logging.DEBUG)


class DatafileError(Exception):
    pass


class MappingError(Exception):
    pass


class Epitran(object):
    """Unified interface for IPA transliteration/transcription"""
    special = {'eng-Latn': FliteLexLookup,
               'cmn-Hans': Epihan,
               'cmn-Hant': EpihanTraditional}

    def __init__(self, code, preproc=True, postproc=True, ligatures=False, cedict_file=None):
        """Construct Epitran transliteration/transcription object

        Args:
            code (str): ISO 639-3 plus "-" plus ISO 15924 code of the
                        language/script pair that should be loaded
            preproc (bool): apply preprocessors
            postproc (bool): apply prostprocessors
            ligatures (bool): use precomposed ligatures instead of standard IPA
            cedict_filename (str): path to file containing the CC-CEDict
                                   dictionary; relevant only for Chinese
        """
        if code in self.special:
            self.epi = self.special[code](ligatures=ligatures, cedict_file=cedict_file)
        else:
            self.epi = SimpleEpitran(code, preproc, postproc, ligatures)
        self.ft = panphon.FeatureTable()
        self.xsampa = XSampa()

    def transliterate(self, word, normpunc=False, ligatures=False):
        """Transliterates/transcribes a word into IPA

        Args:
            word (str): word to transcribe; unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            unicode: IPA string
        """
        return self.epi.transliterate(word, normpunc, ligatures)

    def trans_list(self, word, normpunc=False, ligatures=False):
        """Transliterates/transcribes a word into list of IPA phonemes

        Args:
            word (str): word to transcribe; unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            list: list of IPA strings, each corresponding to a segment
        """
        return self.ft.segs(self.epi.transliterate(word, normpunc, ligatures))

    def xsampa_list(self, word, normpunc=False, ligaturize=False):
        """Transliterates/transcribes a word as X-SAMPA

        Args:
            word (str): word to transcribe; unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            list: X-SAMPA strings, each corresponding to a segment
        """
        ipa_segs = self.trans_list(word, normpunc, ligaturize)
        return map(self.xsampa.ipa2xs, ipa_segs)


class SimpleEpitran(object):
    def __init__(self, code, preproc=True, postproc=True, ligatures=False):
        self.g2p = self._load_g2p_map(code)
        self.regexp = self._construct_regex()
        self.puncnorm = PuncNorm()
        self.ft = panphon.FeatureTable()
        self.num_panphon_fts = len(self.ft.names)
        self.preprocessor = PrePostProcessor(code, 'pre')
        self.postprocessor = PrePostProcessor(code, 'post')
        self.strip_diacritics = StripDiacritics(code)
        self.preproc = preproc
        self.postproc = postproc
        self.ligatures = ligatures
        self.nils = defaultdict(int)

    def __enter__(self):
        return self

    def __exit__(self, type_, val, tb):
        for nil, count in self.nils.items():
            sys.stderr.write('Unknown character "{}" occured {} times.\n'.format(nil, count))

    def _one_to_many_g2p_map(self, g2p):
        for g, p in g2p.items():
            if len(p) != 1:
                return g
        return None

    def _load_g2p_map(self, code):
        """Load the code table for the specified language.

        Args:
            code (str): ISO 639-3 code plus "-" plus ISO 15924 code for the
                        language/script to be loaded
        """
        g2p = defaultdict(list)
        try:
            path = os.path.join('data', 'map', code + '.csv')
            path = pkg_resources.resource_filename(__name__, path)
            with open(path, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                next(reader)
                for graph, phon in reader:
                    graph = unicodedata.normalize('NFC', graph)
                    phon = unicodedata.normalize('NFC', phon)
                    g2p[graph].append(phon)
            if self._one_to_many_g2p_map(g2p):
                graph = self._one_to_many_g2p_map(g2p)
                raise MappingError('One-to-many G2P mapping for "{}"'.format(graph).encode('utf-8'))
            return g2p
        except IndexError:
            raise DatafileError('Add an appropriately-named mapping to the data/maps directory.')

    def _load_punc_norm_map(self):
        """Load the map table for normalizing 'down' punctuation."""
        path = pkg_resources.resource_filename(__name__, 'data/puncnorm.csv')
        with open(path, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8', delimiter=str(','), quotechar=str('"'))
            next(reader)
            return {punc: norm for (punc, norm) in reader}

    def _construct_regex(self):
        """Build a regular expression that will greadily match segments from
           the mapping table.
        """
        graphemes = sorted(self.g2p.keys(), key=len, reverse=True)
        return re.compile(r'({})'.format(r'|'.join(graphemes)), re.I)

    def transliterate(self, text, normpunc=False, ligatures=False):
        """Transliterates/transcribes a word into IPA

        Args:
            word (str): word to transcribe; unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            unicode: IPA string
        """
        text = unicode(text)
        text = self.strip_diacritics.process(text)
        text = unicodedata.normalize('NFKD', text)
        text = unicodedata.normalize('NFC', text.lower())
        if self.preproc:
            text = self.preprocessor.process(text)
        tr_list = []
        while text:
            m = self.regexp.match(text)
            if m:
                from_seg = m.group(0)
                try:
                    to_seg = self.g2p[from_seg][0]
                except:
                    print("from_seg = {}".format(from_seg))
                    print("self.g2p[from_seg] = {}".format(self.g2p[from_seg]))
                tr_list.append(to_seg)
                text = text[len(from_seg):]
            else:
                tr_list.append(text[0])
                self.nils[text[0]] += 1
                text = text[1:]
        text = ''.join(tr_list)
        if self.postproc:
            text = self.postprocessor.process(text)
        if ligatures or self.ligatures:
            text = ligaturize(text)
        if normpunc:
            text = self.puncnorm.norm(text)
        return text

    def trans_delimiter(self, text, delimiter=str(' '), normpunc=False, ligatures=False):
        return delimiter.join(self.trans_list(text, normpunc=normpunc, ligatures=ligatures))

    def word_to_tuples(self, word, normpunc=False):
        """Given a word, returns a list of tuples corresponding to IPA segments.

        Args:
            word (unicode): word to transliterate
            normpunc (bool): If True, normalizes punctuation to ASCII inventory

        Returns:
        list: A list of (category, lettercase, orthographic_form, phonetic_form,
              fecture_vectors) tuples.

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
            if phon == '':
                return [(-1, [0] * self.num_panphon_fts)]
            else:
                return [to_vector(seg) for seg in self.ft.segs(phon)]

        tuples = []
        word = unicode(word)
        word = self.strip_diacritics.process(word)
        word = unicodedata.normalize('NFKD', word)
        word = unicodedata.normalize('NFC', word)
        if self.preproc:
            word = self.preprocessor.process(word)
        while word:
            match = self.regexp.match(word)
            if match:
                span = match.group(1)
                cat, case = cat_and_cap(span[0])
                phon = self.g2p[span.lower()][0]
                vecs = to_vectors(phon)
                tuples.append(('L', case, span, phon, vecs))
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

    def ipa_segs(self, ipa):
        return self.ft.segs(ipa)
