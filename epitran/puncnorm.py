# -*- coding: utf-8 -*-

import pkg_resources
import unicodecsv as csv


class PuncNorm(object):
    def __init__(self):
        """Constructs a punctuation normalization object"""
        self.puncnorm = self._load_punc_norm_map()

    def _load_punc_norm_map(self):
        """Load the map table for normalizing 'down' punctuation."""
        path = pkg_resources.resource_filename(__name__, 'data/puncnorm.csv')
        with open(path, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8', delimiter=str(','), quotechar=str('"'))
            next(reader)
            return {punc: norm for (punc, norm) in reader}

    def norm(self, text):
        """Apply punctuation normalization to a string of text

        Args:
            text (unicode): text to normalize_punc

        Returns:
            unicode: text with normalized punctuation
        """
        new_text = []
        for c in text:
            if c in self.puncnorm:
                new_text.append(self.puncnorm[c])
            else:
                new_text.append(c)
        return ''.join(new_text)

    def __iter__(self):
        return iter(self.puncnorm)

    def __getitem__(self, key):
        return self.puncnorm[key]
