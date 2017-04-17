# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

import os.path
import unicodedata

import unicodecsv as csv

import pkg_resources

class StripDiacritics(object):
    def __init__(self, code):
        """Constructs object to strip specified diacritics from text

        Args:
            code (str): ISO 639-3 code and ISO 15924 code joined with a hyphen
        """
        self.diacritics = self._read_diacritics(code)

    def _read_diacritics(self, code):
        diacritics = []
        fn = os.path.join('data', 'strip', code + '.csv')
        try:
            abs_fn = pkg_resources.resource_filename(__name__, fn)
        except KeyError:
            return []
        if os.path.isfile(abs_fn):
            with open(abs_fn, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                for [diacritic] in reader:
                    diacritics.append(diacritic)
        return diacritics

    def process(self, word):
        """Remove diacritics from an input string

        Args:
            word (unicode): Unicode IPA string

        Returns:
            unicode: Unicode IPA string with specified diacritics removed
        """
        word = unicodedata.normalize('NFD', word)
        for diacritic in self.diacritics:
            word = word.replace(diacritic, '')
        return word
