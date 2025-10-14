# -*- coding: utf-8 -*-

import os.path
from typing import List

from importlib import resources

import csv


class StripDiacritics(object):
    def __init__(self, code: str) -> None:
        """Constructs object to strip specified diacritics from text

        Args:
            code (str): ISO 639-3 code and ISO 15924 code joined with a hyphen
        """
        self.diacritics = self._read_diacritics(code)

    def _read_diacritics(self, code: str) -> List[str]:
        diacritics = []
        fn = os.path.join('data', 'strip', code + '.csv')
        try:
            resource_path = resources.files(__package__).joinpath(fn)
            if resource_path.is_file():
                with resource_path.open('r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for [diacritic] in reader:
                        diacritics.append(diacritic)
        except (KeyError, FileNotFoundError):
            pass
        return diacritics

    def process(self, word: str) -> str:
        """Remove diacritics from an input string

        Args:
            word (str): Unicode IPA string

        Returns:
            str: Unicode IPA string with specified diacritics
            removed
        """
        # word = unicodedata.normalize('NFD', word)
        word = ''.join(filter(lambda x: x not in self.diacritics, word))
        # return unicodedata.normalize('NFC', word)
        return word
