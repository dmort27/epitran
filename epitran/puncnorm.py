# -*- coding: utf-8 -*-

import csv
from importlib import resources
from typing import Dict, Iterator


class PuncNorm(object):
    def __init__(self) -> None:
        """Constructs a punctuation normalization object"""
        self.puncnorm = self._load_punc_norm_map()

    def _load_punc_norm_map(self) -> Dict[str, str]:
        """Load the map table for normalizing 'down' punctuation."""
        with resources.files(__package__).joinpath('data/puncnorm.csv').open('r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            next(reader)
            return {punc: norm for (punc, norm) in reader}

    def norm(self, text: str) -> str:
        """Apply punctuation normalization to a string of text

        Args:
            text (str): text to normalize_punc

        Returns:
            str: text with normalized punctuation
        """
        new_text = []
        for c in text:
            if c in self.puncnorm:
                new_text.append(self.puncnorm[c])
            else:
                new_text.append(c)
        return ''.join(new_text)

    def __iter__(self) -> Iterator[str]:
        return iter(self.puncnorm)

    def __getitem__(self, key: str) -> str:
        return self.puncnorm[key]
