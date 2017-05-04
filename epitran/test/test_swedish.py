# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestSwedish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('swe-Latn')

    def test_rattstafning(self):
        tr = self.epi.transliterate('rättstafning')
        self.assertEqual(tr, 'rɛttstɐfniːŋ')
