# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os.path

import pkg_resources

import marisa_trie
import panphon
import unicodecsv as csv


class XSampa(object):
    ipa2xs_fn = 'ipa-xsampa.csv'

    def __init__(self):
        """Construct an IPA-XSampa conversion object
        """
        self.trie = self._read_ipa2xs()
        self.ft = panphon.FeatureTable()

    def _read_ipa2xs(self):
        path = os.path.join('data', self.ipa2xs_fn)
        path = pkg_resources.resource_filename(__name__, path)
        pairs = []
        with open(path, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            next(reader)
            for ipa, xs, _ in reader:
                pairs.append((ipa, xs.encode('utf-8'),))
        trie = marisa_trie.BytesTrie(pairs)
        return trie

    def prefixes(self, s):
        return self.trie.prefixes(s)

    def longest_prefix(self, s):
        prefixes = self.prefixes(s)
        if not prefixes:
            return ''
        else:
            return sorted(prefixes, key=len)[-1]  # sort by length and return last

    def ipa2xs(self, ipa):
        """Convert IPA string (unicode) to X-SAMPA string

        Args:
            ipa (unicode): An IPA string as unicode

        Returns:
            list: a list of strings corresponding to X-SAMPA segments

            Non-IPA segments are skipped.
        """
        xsampa = []
        while ipa:
            token = self.longest_prefix(ipa)
            if token:
                xs = self.trie[token][0]  # take first member of the list
                xsampa.append(xs.decode('utf-8'))
                ipa = ipa[len(token):]
            else:
                ipa = ipa[1:]
        return ''.join(xsampa)
