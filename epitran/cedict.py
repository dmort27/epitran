# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import codecs
import functools
import types
import os.path

import pkg_resources

import marisa_trie
import regex as re

ASCII_CHARS = ''.join([chr(i) for i in range(128)])


class CEDict(object):
    def __init__(self, cedict_file):
        self.hanzi = self._read_cedict(cedict_file)

    def _read_cedict(self, cedict_file):
        comment_re = re.compile('\s*#')
        lemma_re = re.compile('(?P<hanzi>[^]]+) \[(?P<pinyin>[^]]+)\] /(?P<english>.+)/')
        cedict = {}
        # cedict_file = os.path.join('data', cedict_file + '.txt')
        # cedict_file = pkg_resources.resource_filename(__name__, cedict_file)
        with codecs.open(cedict_file, 'r', 'utf-8') as f:
            for line in f:
                if comment_re.match(line):
                    pass
                elif lemma_re.match(line):
                    match = lemma_re.match(line)
                    hanzi = match.group('hanzi').split(' ')
                    pinyin = match.group('pinyin').split(' ')
                    english = match.group('english').split('/')
                    cedict[hanzi[1]] = (pinyin, english)  # Simplified characters only.
        return cedict


class CEDictFST(CEDict):
    def _read_cedict(self, dict_file):
        comment_re = re.compile('\s*#')
        lemma_re = re.compile('(?P<hanzi>[^]]+) \[(?P<pinyin>[^]]+)\] /(?P<english>.+)/')
        cedict = {}
        with codecs.open(dict_file, 'r', 'utf-8') as f:
            for line in f:
                if comment_re.match(line):
                    pass
                elif lemma_re.match(line):
                    match = lemma_re.match(line)
                    hanzi = match.group('hanzi').split(' ')
                    pinyin = self._normalize_pinyin(match.group('pinyin')).split(' ')
                    english = match.group('english').split('/')
                    cedict[hanzi[1]] = (pinyin, english)  # Simplified characters only.
        return cedict

        def _normalize_pinyin(self, text):
            text = text.lower()
            text = text.replace('u:', 'v')
            return text

        def _get_every_han_char(self):
            return functools.reduce(lambda a, b: a | b, [set(x) for x in iter(self.hanzi)], set())

        def _get_every_pinyin_char(self):
            return functools.reduce(lambda a, b: a | b, [set(p) for (p, e) in self.hanzi.iteritems()], set())

        def symbol_table(self, table):
            text = '<eps> 0\n'
            for sym, num in sorted(table.items(), key=lambda a, b: b):
                text += '{} {}\n'.format(sym, num)

        def phrase_to_att_fst(self, phrase):
            p, e = self.hanzi[phrase]
            pairs = zip(phrase, p)
            text = ''
            for ch, pw in pairs:
                text += '{} {} {} {} 1\n'.format(self.state, self.state + 1, ch, pw[0])
                pw = pw[1:]
                self.state += 1
                for let in pw:
                    text += '{} {} {} {} 1\n'.format(self.state, self.state + 1, '<eps>', let)
                    self.state += 1
            text += '{} 1'.format(self.state)
            return text

        def write_hanzi_to_pinyin_lexc(self, lexc):
            with codecs.open(lexc, 'w', 'utf-8') as f:
                print(u'LEXICON Root', file=f)
                for hanzi, fields in self.hanzi.iteritems():
                    pinyin, _ = fields
                    hanzi = ''.join([h.ljust(len(p), '0') for (h, p) in zip(list(hanzi), pinyin)])
                    pinyin = ''.join(pinyin)
                    print(u'{}:{}\t# ;'.format(hanzi, pinyin), file=f)


class CEDictTrie(CEDict):
    def __init__(self, dict_file):
        self.hanzi = self._read_cedict(dict_file)
        self.trie = self.construct_trie(self.hanzi)

    def construct_trie(self, hanzi):
        pairs = []
        for hz, df in self.hanzi.items():
            py, en = df
            py = str(''.join(filter(lambda x: x in ASCII_CHARS, ' '.join(py))))
            assert isinstance(py, types.StringTypes)
            pairs.append((hz, (py,)))
        trie = marisa_trie.RecordTrie('@s', pairs)
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
