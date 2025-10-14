# -*- coding: utf-8 -*-


import unittest

import epitran


class TestBurmese(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('mya-Mymr')

    def test_1(self):
        tr = self.epi.transliterate('ပန်း')
        self.assertEqual(tr, 'paɴ')

    def test_2(self):
        tr = self.epi.transliterate('ဝင်')
        self.assertEqual(tr, 'wɪɴ')

    def test_3(self):
        tr = self.epi.transliterate('ဇွန်း')
        self.assertEqual(tr, 'zʊɴ')

    def test_4(self):
        tr = self.epi.transliterate('အိမ်')
        self.assertEqual(tr, 'ʔeɪɴ')

    def test_5(self):
        tr = self.epi.transliterate('ရန်ကုန်')
        self.assertEqual(tr, 'jaɴkoʊɴ')

    def test_6(self):
        tr = self.epi.transliterate('ကောင်း')
        self.assertEqual(tr, 'kaʊɴ')

    def test_7(self):
        tr = self.epi.transliterate('ဆိုင်')
        self.assertEqual(tr, 'sʰaɪɴ')
