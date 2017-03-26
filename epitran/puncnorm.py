# -*- coding: utf-8 -*-

import pkg_resources
import unicodecsv as csv


class PuncNorm(object):
    def __init__(self):
        self.puncnorm = self._load_punc_norm_map()

    def _load_punc_norm_map(self):
        """Load the map table for normalizing 'down' punctuation."""
        path = pkg_resources.resource_filename(__name__, 'data/puncnorm.csv')
        with open(path, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8', delimiter=str(','), quotechar=str('"'))
            next(reader)
            return {punc: norm for (punc, norm) in reader}

    def norm(self, text):
        new_text = []
        for c in text:
            if c in self.puncnorm:
                new_text.append(self.puncnorm[c])
            else:
                new_text.append(c)
        return ''.join(new_text)
