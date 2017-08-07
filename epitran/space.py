# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os

import pkg_resources
import unicodecsv as csv
from epitran import Epitran


class Space(object):
    def __init__(self, code, space_names):
        """Construct a Space object

        Space objects take strings (corresponding to segments) and return
        integers, placing them in an integer space that can be translated into
        a one-hot vector.

        The resulting object has a dictionary-like interface that supports
        indexing and iteration over "keys".

        Args:
            code (str): ISO 639-3 code joined to ISO 15924 code with "-"
            space_names (list): list of space names consisting of ISO 639-3
            codes joined to ISO 15924 codes with "-"
        """
        self.epi = Epitran(code)
        self.dict = self._load_space(space_names)

    def _load_space(self, space_names):
        segs = set()
        scripts = list(set([nm.split('-')[1] for nm in space_names]))
        punc_fns = ['punc-{}.csv'.format(sc) for sc in scripts]
        for punc_fn in punc_fns:
            punc_fn = os.path.join('data', 'space', punc_fn)
            punc_fn = pkg_resources.resource_filename(__name__, punc_fn)
            with open(punc_fn, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                for (mark,) in reader:
                    segs.add(mark)
        for name in space_names:
            fn = os.path.join('data', 'space', name + '.csv')
            fn = pkg_resources.resource_filename(__name__, fn)
            with open(fn, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                for _, to_ in reader:
                    for seg in self.epi.ft.ipa_segs(to_):
                        segs.add(seg)
        enum = enumerate(sorted(list(segs)))
        return {seg: num for num, seg in enum}

    def __iter__(self):
        return iter(self.dict)

    def __getitem__(self, key):
        """Given a string as a key, return the corresponding integer

        Args:
            key (unicode): a unicode key corresponding to a segment

        Returns:
            int: the integer corresponding to the unicode string
        """
        try:
            return self.dict[key]
        except KeyError:
            return len(self.dict)
