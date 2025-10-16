# -*- coding: utf-8 -*-


import unittest

import epitran


class TestSerbian(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('srp-Latn')

    # Test 1: đak -> dʑak
    def test1(self):
        result = self.epi.transliterate('đak')
        self.assertEqual(result, 'dʑak')

    # Test 2: čekić -> tʃekitɕ
    def test2(self):
        result = self.epi.transliterate('čekić')
        self.assertEqual(result, 'tʃekitɕ')

    # Test 3: žaba -> ʒaba
    def test3(self):
        result = self.epi.transliterate('žaba')
        self.assertEqual(result, 'ʒaba')

    # Test 4: šuma -> ʃuma
    def test4(self):
        result = self.epi.transliterate('šuma')
        self.assertEqual(result, 'ʃuma')

    # Test 5: sjȅme -> sjême
    def test5(self):
        result = self.epi.transliterate('sjȅme')
        self.assertEqual(result, 'sjême')
