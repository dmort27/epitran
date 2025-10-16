# -*- coding: utf-8 -*-

import os.path
import unicodedata
from typing import List

from importlib import resources

import marisa_trie
import panphon
import csv


class XSampa(object):
    ipa2xs_fn = 'ipa-xsampa.csv'

    def __init__(self) -> None:
        """Construct an IPA-XSampa conversion object
        """
        self.trie = self._read_ipa2xs()
        self.ft = panphon.FeatureTable()

    def _read_ipa2xs(self) -> marisa_trie.BytesTrie:
        path_str = os.path.join('data', self.ipa2xs_fn)
        path = resources.files(__package__).joinpath(path_str)
        pairs = []
        with path.open('r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for ipa, xs, _ in reader:
                pairs.append((ipa, xs.encode('utf-8'),))
        trie = marisa_trie.BytesTrie(pairs)
        return trie

    def prefixes(self, s: str) -> List[str]:
        return self.trie.prefixes(s)

    def longest_prefix(self, s: str) -> str:
        prefixes = self.prefixes(s)
        if not prefixes:
            return ''
        else:
            return sorted(prefixes, key=len)[-1]  # sort by length and return last

    def ipa2xs(self, ipa: str) -> str:
        """Convert IPA string (unicode) to X-SAMPA string

        Args:
            ipa (unicode): An IPA string as unicode

        Returns:
            list: a list of strings corresponding to X-SAMPA segments

            Non-IPA segments are skipped.
        """
        xsampa = []
        ipa = unicodedata.normalize('NFD', ipa)
        while ipa:
            token = self.longest_prefix(ipa)
            if token:
                xs = self.trie[token][0]  # take first member of the list
                xsampa.append(xs.decode('utf-8'))
                ipa = ipa[len(token):]
            else:
                ipa = ipa[1:]
        return ''.join(xsampa)
