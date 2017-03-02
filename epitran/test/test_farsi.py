# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestSorani(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'fas-Arab')

    def test_faarsi(self):
        tr = self.epi.transliterate('فارسی')
        self.assertEqual(tr, 'fɒrsj')

    def test_rowshan(self):
        tr = self.epi.transliterate('روشن')
        self.assertEqual(tr, 'rvʃn')

    def test_hamaye(self):
        tr = self.epi.transliterate('همهٔ')
        self.assertEqual(tr, 'hmhʔ')

    def test_aafraad(self):
        tr = self.epi.transliterate('افراد')
        self.assertEqual(tr, 'ɒfrɒd')

    def test_bashar(self):
        tr = self.epi.transliterate('بشر')
        self.assertEqual(tr, 'bʃr')

    def test_aazaad(self):
        tr = self.epi.transliterate('آزاد')
        self.assertEqual(tr, 'ɒzɒd')

    def test_donjaa(self):
        tr = self.epi.transliterate('دنیا')
        self.assertEqual(tr, 'dnjɒ')

    def test_miaayand(self):
        tr = self.epi.transliterate('می‌آیند')
        self.assertEqual(tr, 'mj‌ɒjnd')

    def test_heysiyaat(self):
        tr = self.epi.transliterate('حیثیت')
        self.assertEqual(tr, 'hjsjt')
