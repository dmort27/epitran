# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import codecs

import marisa_trie
import regex as re

ASCII_CHARS = ''.join([chr(i) for i in range(128)])


class CEDictTrie(object):
    def __init__(self, cedict_file, traditional=False):
        """Construct a trie over CC-CEDict

        Args:
            cedict_file (str): path to the CC-CEDict dictionary
            traditional (bool): if True, use traditional characters
        """
        self.hanzi = self._read_cedict(cedict_file, traditional=traditional)
        self.trie = self._construct_trie(self.hanzi)

    def _read_cedict(self, cedict_file, traditional=False):
        comment_re = re.compile('\s*#')
        lemma_re = re.compile('(?P<hanzi>[^]]+) \[(?P<pinyin>[^]]+)\] /(?P<english>.+)/')
        cedict = {}
        with codecs.open(cedict_file, 'r', 'utf-8') as f:
            for line in f:
                if comment_re.match(line):
                    pass
                elif lemma_re.match(line):
                    match = lemma_re.match(line)
                    hanzi = match.group('hanzi').split(' ')
                    pinyin = match.group('pinyin').split(' ')
                    english = match.group('english').split('/')
                    if traditional:
                        cedict[hanzi[0]] = (pinyin, english)  # traditional characters only
                    else:
                        cedict[hanzi[1]] = (pinyin, english)  # simplified characters only.
        return cedict


    def _construct_trie(self, hanzi):
        pairs = []
        for hz, df in self.hanzi.items():
            py, en = df
            py = str(''.join(filter(lambda x: x in ASCII_CHARS, ' '.join(py))))
            pairs.append((hz, (py.encode('utf-8'),)))
        trie = marisa_trie.RecordTrie(str('@s'), pairs)
        return trie

    def has_key(self, key):
        return key in self.hanzi

    def prefixes(self, s):
        return self.trie.prefixes(s)

    def longest_prefix(self, s):
        prefixes = self.prefixes(s)
        if not prefixes:
            return ''
        else:
            return sorted(prefixes, key=len)[-1]  # Sort by length and return last.

    def tokenize(self, s):
        tokens = []
        while s:
            token = self.longest_prefix(s)
            if token:
                tokens.append(token)
                s = s[len(token):]
            else:
                tokens.append(s[0])
                s = s[1:]
        return tokens
