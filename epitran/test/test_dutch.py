# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import unittest

import epitran


def assemble_ipa(xs):
    return ''.join([x[3] for x in xs])


class TestDutch(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('nld-Latn')

    def _derivation(self, orth, correct):
        attempt = assemble_ipa(self.epi.word_to_tuples(orth))
        self.assertEqual(attempt, correct)

    def test_bernhard(self):
        self._derivation('Bernhard', 'bɛrnhɑrt')

    def test_utrecht(self):
        self._derivation('Utrecht', 'ʏtrɛxt')

    def test_lodewijk(self):
        self._derivation('Lodewijk', 'loːdeːʋɛjk')

    def test_random(self):
        self._derivation('ertogenbosch', 'ɛrtoːɣɛnbɔs')
