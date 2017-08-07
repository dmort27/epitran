# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestBurmese(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('mya-Mymr')

    def test_(self):
        tr = self.epi.transliterate('ပန်း')
        self.assertEqual(tr, 'paɴ')

    def test_(self):
        tr = self.epi.transliterate('ဝင်')
        self.assertEqual(tr, 'wɪɴ')

    def test_(self):
        tr = self.epi.transliterate('ဇွန်း')
        self.assertEqual(tr, 'zʊɴ')

    def test_(self):
        tr = self.epi.transliterate('အိမ်')
        self.assertEqual(tr, 'ʔeɪɴ')

    def test_(self):
        tr = self.epi.transliterate('ရန်ကုန်')
        self.assertEqual(tr, 'jaɴkoʊɴ')

    def test_(self):
        tr = self.epi.transliterate('ကောင်း')
        self.assertEqual(tr, 'kaʊɴ')

    def test_(self):
        tr = self.epi.transliterate('ဆိုင်')
        self.assertEqual(tr, 'sʰaɪɴ')
