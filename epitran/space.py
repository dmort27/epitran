# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os

import pkg_resources
import unicodecsv as csv


class Space(object):
    def __init__(self, space_name):
        self.dict = self._load_space(space_name)

    def __getitem__(self, key):
        return self.dict[key]

    def _load_space(self, space_name):
        space_fn = os.path.join('data', 'space', space_name + '.csv')
        space_fn = pkg_resources.resource_filename(__name__, space_fn)
        with open(space_fn, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            return {seg: int(num) for (num, seg) in reader}
