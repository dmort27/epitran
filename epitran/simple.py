# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import logging
import os.path
import sys
import unicodedata
from collections import defaultdict

import pkg_resources

import panphon
import regex as re
import unicodecsv as csv
from epitran.ligaturize import ligaturize
from epitran.ppprocessor import PrePostProcessor
from epitran.puncnorm import PuncNorm
from epitran.stripdiacritics import StripDiacritics
from epitran.exceptions import DatafileError, MappingError

if sys.version_info[0] == 3:
    def unicode(x):
        return x
logging.basicConfig(level=logging.DEBUG)


class SimpleEpitran(object):
    def __init__(self, code, preproc=True, postproc=True, ligatures=False):
        """Constructs the backend object epitran uses for most languages

        Args:
            code (str): ISO 639-3 code and ISO 15924 code joined with a hyphen
            preproc (bool): if True, apply preprocessor
            postproc (bool): if True, apply postprocessors
            ligatures (bool): if True, use phonetic ligatures for affricates
                              instead of standard IPA
        """
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

    def _one_to_many_gr_by_line_map(self, gr_by_line):
        for g, ls in gr_by_line.items():
            if len(ls) != 1:
                return (g, ls)
        return None

    def _load_g2p_map(self, code):
        """Load the code table for the specified language.

        Args:
            code (str): ISO 639-3 code plus "-" plus ISO 15924 code for the
                        language/script to be loaded
        """
        g2p = defaultdict(list)
        gr_by_line = defaultdict(list)
        try:
            path = os.path.join('data', 'map', code + '.csv')
            path = pkg_resources.resource_filename(__name__, path)
        except IndexError:
            raise DatafileError('Add an appropriately-named mapping to the data/maps directory.')
        with open(path, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            next(reader)
            for (i, fields) in enumerate(reader):
                try:
                    graph, phon = fields
                except ValueError:
                    raise DatafileError('Map file is not well formed at line {}.'.format(i + 2))
                graph = unicodedata.normalize('NFC', graph)
                phon = unicodedata.normalize('NFC', phon)
                g2p[graph].append(phon)
                gr_by_line[graph].append(i)
        if self._one_to_many_gr_by_line_map(g2p):
            graph, lines = self._one_to_many_gr_by_line_map(gr_by_line)
            lines = [l + 2 for l in lines]
            raise MappingError('One-to-many G2P mapping for "{}" on lines {}'.format(graph, ', '.join(map(str, lines))).encode('utf-8'))
        return g2p

    def _load_punc_norm_map(self):
        """Load the map table for normalizing 'down' punctuation."""
        path = os.path.join('data', 'puncnorm.csv')
        path = pkg_resources.resource_filename(__name__, path)
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

    def transliterate(self, text, normpunc=False, ligatures=False, safe=True):
        """Transliterates/transcribes a word into IPA

        Passes unmapped characters through to output unchanged.

        Args:
            word (str): word to transcribe; unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            unicode: IPA string with unrecognized characters included
        """
        text = unicode(text)
        if safe and not self.regexp.search(text):
            return text
        text = self.strip_diacritics.process(text)
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
                    to_seg = from_seg
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

    def strict_trans(self, text, normpunc=False, ligatures=False):
        """Transliterates/transcribes a word into IPA

        Ignores umapped characters.

        Args:
            word (str): word to transcribe; unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            unicode: IPA string
        """
        text = unicode(text)
        if not self.regexp.search(text):
            return ''
        text = self.strip_diacritics.process(text)
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
            return list(map(recode_ft, vec))

        def to_vector(seg):
            return seg, vec2bin(self.ft.segment_to_vector(seg))

        def to_vectors(phon):
            if phon == '':
                return [(-1, [0] * self.num_panphon_fts)]
            else:
                return [to_vector(seg) for seg in self.ft.ipa_segs(phon)]

        tuples = []
        word = unicode(word)
        word = self.strip_diacritics.process(word)
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
        """Given an IPA string, decompose it into a list of segments

        Args:
            ipa (unicode): a Unicode IPA string

        Returns:
            list: a list of unicode strings corresponding to segments
                  (consonants and vowels) in the input string
        """
        return self.ft.segs(ipa)
