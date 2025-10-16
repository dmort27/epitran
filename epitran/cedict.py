# -*- coding: utf-8 -*-

import codecs
from typing import Dict, List, Tuple, Any

import marisa_trie
import regex as re

ASCII_CHARS = ''.join([chr(i) for i in range(128)])


class CEDictTrie(object):
    def __init__(self, cedict_file: str, traditional: bool = False) -> None:
        """Construct a trie over CC-CEDict

        Args:
            cedict_file (str): path to the CC-CEDict dictionary
            traditional (bool): if True, use traditional characters
        """
        self.hanzi = self._read_cedict(cedict_file, traditional=traditional)
        self.trie = self._construct_trie(self.hanzi)

    def _read_cedict(self, cedict_file: str, traditional: bool = False) -> Dict[str, Tuple[List[str], List[str]]]:
        comment_re = re.compile(r'\s*#')
        lemma_re = re.compile(r'(?P<hanzi>[^]]+) \[(?P<pinyin>[^]]+)\] /(?P<english>.+)/')
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

    def _construct_trie(self, hanzi: Dict[str, Tuple[List[str], List[str]]]) -> Any:
        pairs = []
        for hz, df in self.hanzi.items():
            py, en = df
            py_str = ''.join(filter(lambda x: x in ASCII_CHARS, ' '.join(py)))
            pairs.append((hz, (py_str.encode('utf-8'),)))
        trie = marisa_trie.RecordTrie('@s', pairs)
        return trie

    def has_key(self, key: str) -> bool:
        return key in self.hanzi

    def prefixes(self, s: str) -> List[str]:
        return self.trie.prefixes(s)

    def longest_prefix(self, s: str) -> str:
        prefixes = self.prefixes(s)
        if not prefixes:
            return ''
        else:
            return sorted(prefixes, key=len)[-1]  # Sort by length and return last.

    def tokenize(self, s: str) -> List[str]:
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


class CEDictTrieForCantonese(CEDictTrie):
    def _read_cedict(self, cedict_file: str, traditional: bool = False) -> Dict[str, Tuple[List[str], List[str]]]:
        comment_re = re.compile(r'\s*#')
        lemma_re = re.compile(r'(?P<hanzi>[^[]+) \[(?P<pinyin>[^]]+)\] \{(?P<jyutping>[^}]+)\} /(?P<english>.+)/')
        cedict = {}
        with codecs.open(cedict_file, 'r', 'utf-8') as f:
            for line in f:
                if comment_re.match(line):
                    pass
                elif lemma_re.match(line):
                    match = lemma_re.match(line)
                    hanzi = match.group('hanzi').split(' ')
                    jyutping = match.group('jyutping').split(' ')
                    english = match.group('english').split('/')
                    
                    hanzi = hanzi[0] if traditional else hanzi[1]
                    cedict[hanzi] = (jyutping, english)

                    # NOTE(Jinchuan): Some isolated characters are missing in the dict
                    # but there are many words contains those characters. So we split
                    # the words and get the pronunciation of each single character.
                    # This operation will reduce out-of-vocabulary issue but will
                    # definitely introduce errors: some characters have multiple
                    # pronunciation, but we only keep one of it.
                    for char, syllable in zip(hanzi, jyutping):
                        if char not in cedict_file:
                            cedict[char] = (syllable, "")
        return cedict


class CEDictTrieForJapanese(object):
    def __init__(self, cedict_file: str) -> None:
        """Construct a trie over src

        Args:
            cedict_file (str): path to the src dictionary
        """
        self.character = self._read_cedict(cedict_file)
        self.trie = self._construct_trie(self.character)

    def _read_cedict(self, cedict_file: str) -> Dict[str, str]:
        cedict = {}
        with codecs.open(cedict_file, 'r', 'utf-8') as f:
            for line in f:
                character, v = line.split('\t')
                match = re.search(r'/([^/]+)/', v)
                if match:
                    pron = match.group(1)
                    cedict[character] = pron
                else:
                    cedict[character] = ''
        return cedict

    def _construct_trie(self, character: Dict[str, str]) -> Any:
        pairs = []
        for ch, pron in self.character.items():
            pairs.append((ch, (pron.encode('utf-8'),)))
        trie = marisa_trie.RecordTrie('@s', pairs)
        return trie

    def has_key(self, key: str) -> bool:
        return key in self.character

    def prefixes(self, s: str) -> List[str]:
        return self.trie.prefixes(s)

    def longest_prefix(self, s: str) -> str:
        prefixes = self.prefixes(s)
        if not prefixes:
            return ''
        else:
            return sorted(prefixes, key=len)[-1]

    def tokenize(self, s: str) -> List[str]:
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
