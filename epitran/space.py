# -*- coding: utf-8 -*-

import os
from typing import Dict, List, Iterator

from importlib import resources
import csv
from epitran import Epitran


class Space(object):
    def __init__(self, code: str, space_names: List[str]) -> None:
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

    def _load_space(self, space_names: List[str]) -> Dict[str, int]:
        segs = set()
        scripts = list(set([nm.split('-')[1] for nm in space_names]))
        punc_fns = ['punc-{}.csv'.format(sc) for sc in scripts]
        for punc_fn in punc_fns:
            punc_fn_str = os.path.join('data', 'space', punc_fn)
            punc_fn_path = resources.files(__package__).joinpath(punc_fn_str)
            with punc_fn_path.open('r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for (mark,) in reader:
                    segs.add(mark)
        for name in space_names:
            fn_str = os.path.join('data', 'space', name + '.csv')
            fn_path = resources.files(__package__).joinpath(fn_str)
            with fn_path.open('r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for _, to_ in reader:
                    for seg in self.epi.ft.ipa_segs(to_):
                        segs.add(seg)
        enum = enumerate(sorted(list(segs)))
        return {seg: num for num, seg in enum}

    def __iter__(self) -> Iterator[str]:
        return iter(self.dict)

    def __getitem__(self, key: str) -> int:
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
