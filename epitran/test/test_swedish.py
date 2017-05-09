# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestSwedish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('swe-Latn')

    def test_rattstafning(self):
        tr = self.epi.transliterate('rättstafning')
        self.assertEqual(tr, 'rɛttstɐfnɪŋ')

    def test_stjarna(self):
        tr = self.epi.transliterate('stjärna')
        self.assertEqual(tr, 'ɧɛrnɑː')

    def test_stjal(self):
        tr = self.epi.transliterate('stjäl')
        self.assertEqual(tr, 'ɧɛːl')
