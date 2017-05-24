# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestArabic(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('ara-Arab')

    def test_Iraq(self):
        tr = self.epi.transliterate('العراق')
        self.assertEqual(tr, 'alʕraːq')

    def test_Quran(self):
        tr = self.epi.transliterate('القرآن')
        self.assertEqual(tr, 'alqrʔaːn')

    def test_(self):
        tr = self.epi.transliterate('محمد')
        self.assertEqual(tr, 'mħmd')
