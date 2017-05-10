# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestSwedish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('swe-Latn')

    def test_rattstafning(self):
        tr = self.epi.transliterate('rättstafning')
        self.assertEqual(tr, 'rɛtstɐfnɪŋ')

    def test_stjarna(self):
        tr = self.epi.transliterate('stjärna')
        self.assertEqual(tr, 'ɧɛrnɑː')

    def test_stjal(self):
        tr = self.epi.transliterate('stjäl')
        self.assertEqual(tr, 'ɧɛːl')

    def test_fatolj(self):
        tr = self.epi.transliterate('fåtölj')
        self.assertEqual(tr, 'foːtœj')

    def test_cigarett(self):
        tr = self.epi.transliterate('cigarett')
        self.assertEqual(tr, 'siːɡɑːrɛt')

    def test_kanna(self):
        tr = self.epi.transliterate('känna')
        self.assertEqual(tr, 'ɕɛnɑː')
