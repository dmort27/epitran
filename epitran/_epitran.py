# -*- coding: utf-8 -*-
from __future__ import print_function

import os.path
import sys
import unicodedata
from collections import defaultdict

import pkg_resources

import panphon
import regex as re
import unicodecsv as csv


class Epitran(object):
    """Transliterate text in Latin scripts to Unicode IPA."""
    def __init__(self, code):
        self.g2p = self._load_g2p_map(code)
        self.regexp = self._construct_regex()
        self.puncnorm = self._load_punc_norm_map()
        self.puncnorm_vals = self.puncnorm.values()
        self.ft = panphon.FeatureTable()
        self.num_panphon_fts = len(self.ft.names)

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
                    graph = unicodedata.normalize('NFD', graph)
                    phon = unicodedata.normalize('NFD', phon)
                    g2p[graph].append(phon)
        except IOError:
            print(u'Unknown language.')
            print(u'Add an appropriately-named mapping to the data folder.')
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

    def transliterate(self, text, normpunc=False):
        """Transliterate text from orthography to Unicode IPA.

        text -- The text to be transliterated
        """
        def trans(m):
            if m.group(0) in self.g2p:
                return self.g2p[m.group(0)][0]
            else:
                print('Cannot match "{}"!'.format(m.group(0)), file=sys.stderr)
                return m.group(0)

        def normp(c):
            if c in self.puncnorm:
                return unicode(self.normalize_punc(c))
            else:
                return unicode(c)

        text = unicodedata.normalize('NFD', text.lower())
        text = self.regexp.sub(trans, text)
        text = ''.join([normp(c) for c in text])
        return text

    def robust_trans_pairs(self, text):
        """Given noisy orthographic text returns <orth, ipa> pairs."""
        pairs = []
        text = unicodedata.normalize('NFD', text)
        while text:
            # print(text)
            match = self.regexp.match(text)
            if match:
                # With span of letters corresponding to IPA segment, find IPA
                # equivalent and add to pairs.
                span = match.group(0)
                pairs.append((span, self.transliterate(span)))
                text = text[len(span):]
            else:
                # With first character in text, append to pairs (paired with
                # empty IPA equivalent).
                c = text[0]
                c = self.normalize_punc(c)
                pairs.append((c, u''))
                text = text[1:]
        return pairs

    def word_to_tuples(self, word):
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
            return self.ft.seg_seq[seg], vec2bin(self.ft.segment_to_vector(seg))

        def to_vectors(phon):
            if phon == u'':
                return [(-1, [0] * self.num_panphon_fts)]
            else:
                return [to_vector(seg) for seg in self.ft.segs(phon)]

        tuples = []
        word = unicodedata.normalize('NFD', word)
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
                span = self.normalize_punc(span)
                cat, case = cat_and_cap(span)
                phon = u''
                vecs = to_vectors(phon)
                tuples.append((cat, case, span, phon, vecs))
                word = word[1:]
        return tuples

    def ipa_segs(self, ipa):
        return self.ft.segs(ipa)
