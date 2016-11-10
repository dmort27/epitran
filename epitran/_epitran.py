# -*- coding: utf-8 -*-
from __future__ import print_function

import os.path
import sys
import unicodedata
from collections import defaultdict

import pkg_resources
import regex as re
import unicodecsv as csv

import panphon
from ppprocessor import PrePostProcessor
from stripdiacritics import StripDiacritics


class Epitran(object):
    """Transliterate text in Latin scripts to Unicode IPA."""
    def __init__(self, code, preproc=True, postproc=True):
        self.g2p = self._load_g2p_map(code)
        self.regexp = self._construct_regex()
        self.puncnorm = self._load_punc_norm_map()
        self.puncnorm_vals = self.puncnorm.values()
        self.ft = panphon.FeatureTable()
        self.num_panphon_fts = len(self.ft.names)
        self.preprocessor = PrePostProcessor(code, 'pre')
        self.postprocessor = PrePostProcessor(code, 'post')
        self.strip_diacritics = StripDiacritics(code)
        self.preproc = preproc
        self.postproc = postproc
        self.nils = defaultdict(int)


    def __enter__(self):
        return self

    def __exit__(self, type_, val, tb):
        for nil, count in self.nils.items():
            sys.stderr.write('Unknown character "{}" occured {} times.\n'.format(nil, count))


    def _load_g2p_map(self, code):
        """Load the code table for the specified language.

        code -- ISO 639-3 code for the language to be loaded
        """
        g2p = defaultdict(list)
        path = os.path.join('data', code + '.csv')
        path = pkg_resources.resource_filename(__name__, path)
        try:
            with open(path, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                reader.next()
                for graph, phon in reader:
                    graph = unicodedata.normalize('NFC', graph)
                    phon = unicodedata.normalize('NFC', phon)
                    g2p[graph].append(phon)
        except IOError:
            print(u'Unknown language.')
            print(u'Add an appropriately-named mapping to the data directory.')
        return g2p

    def _load_punc_norm_map(self):
        """Load the map table for normalizing 'down' punctuation."""
        path = pkg_resources.resource_filename(__name__, 'data/puncnorm.csv')
        with open(path, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8', delimiter=',', quotechar='"')
            reader.next()
            return {punc: norm for (punc, norm) in reader}

    def _construct_regex(self):
        """Build a regular expression that will greadily match segments from
           the mapping table.
        """
        graphemes = sorted(self.g2p.keys(), key=len, reverse=True)
        #  print(graphemes)
        return re.compile(ur'({})'.format(ur'|'.join(graphemes)), re.I)

    def normalize_punc(self, text):
        new_text = []
        for c in text:
            if c in self.puncnorm:
                new_text.append(self.puncnorm[c])
            else:
                new_text.append(c)
        return u''.join(new_text)

    def transliterate2(self, text, normpunc=False):
        """Transliterate text from orthography to Unicode IPA.

        text -- The text to be transliterated
        normpunc -- Normalize punctuation?
        """
        def normp(c):
            if c in self.puncnorm:
                return unicode(self.normalize_punc(c))
            else:
                return unicode(c)

        text = unicode(text)
        text = self.strip_diacritics.process(text)
        text = unicodedata.normalize('NFKD', text)
        text = unicodedata.normalize('NFC', text.lower())
        if self.preproc:
            text = self.preprocessor.process(text)
        # main loop
        tr_list = []
        while text:
            m = self.regexp.match(text)
            if m:
                from_seg = m.group(0)
                to_seg = self.g2p[from_seg][0]
                tr_list.append(to_seg)
                text = text[len(from_seg):]
            else:
                tr_list.append(text[0])
                self.nils[text[0]] += 1
                text = text[1:]
        text = ''.join([normp(c) for c in tr_list]) if normpunc else ''.join(tr_list)
        if self.postproc:
            text = self.postprocessor.process(text)
        return text

    def transliterate(self, text, normpunc=False):
        """Transliterate text from orthography to Unicode IPA.

        text -- The text to be transliterated
        normpunc -- Normalize punctuation?
        """

        def trans(m):
            if m.group(0) in self.g2p:
                return self.g2p[m.group(0)][0]
            else:
                print('Cannot match "{}"!'.format(m.group(0)), file=sys.stderr)
                return m.group(0)

        def normp(c):
            if normpunc:
                if c in self.puncnorm:
                    return unicode(self.normalize_punc(c))
                else:
                    return unicode(c)
            else:
                return c

        text = unicode(text)
        text = self.strip_diacritics.process(text)
        text = unicodedata.normalize('NFKD', text)
        text = unicodedata.normalize('NFC', text.lower())
        if self.preproc:
            text = self.preprocessor.process(text)
        text = self.regexp.sub(trans, text)
        text = ''.join([normp(c) for c in text]) if normpunc else text
        if self.postproc:
            text = self.postprocessor.process(text)
        return text

    def trans_list(self, text, normpunc=False):
        """Transliterate text from orthography to Unicode IPA (as a list of
        segments.

        text -- The text to be transliterated
        normpunc -- Normalize punctuation?
        """
        def normp(c):
            if normpunc:
                if c in self.puncnorm:
                    return unicode(self.normalize_punc(c))
                else:
                    return unicode(c)
            else:
                return c

        text = unicode(text)
        text = self.strip_diacritics.process(text)
        text = unicodedata.normalize('NFKD', text)
        text = unicodedata.normalize('NFC', text.lower())
        text = self.preprocessor.process(text)
        tr_list = []
        while text:
            m = self.regexp.match(text)
            if m:
                from_seg = m.group(0)
                to_seg = self.g2p[from_seg][0]
                tr_list.append(to_seg)
                text = text[len(from_seg):]
            else:
                tr_list.append(text[0])
                text = text[1:]
        tr_list = [normp(c) for c in tr_list] if normpunc else tr_list
        return tr_list

    def trans_delimiter(self, text, delimiter=' ', normpunc=False):
        return delimiter.join(self.trans_list(text, normpunc=normpunc))

    def word_to_tuples(self, word, normpunc=False):
        """Given a word, returns a list of tuples corresponding to IPA segments.

        word -- Unicode string.
        normpunc -- If True, normalizes punctuation to ASCII inventory.
        returns -- A list of <category, lettercase, orthographic_form,
                   phonetic_form, fecture_vectors> test_word_to_tuples.

        The "feature vectors" form a list consisting of <segment, vector> pairs.
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
            if phon == u'':
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
                tuples.append((u'L', case, span, phon, vecs))
                word = word[len(span):]
            else:
                span = word[0]
                span = self.normalize_punc(span) if normpunc else span
                cat, case = cat_and_cap(span)
                cat = 'P' if normpunc and cat in self.puncnorm else cat
                phon = u''
                vecs = to_vectors(phon)
                tuples.append((cat, case, span, phon, vecs))
                word = word[1:]
        return tuples

    def ipa_segs(self, ipa):
        return self.ft.segs(ipa)
