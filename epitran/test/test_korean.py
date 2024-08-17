# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import epitran

class TestKorean(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('kor-Hang')

    def test_iltha(self):
        tr = self.epi.transliterate('잃다')
        self.assertEqual(tr, 'iltʰa')

    def test_tshukha(self):
        tr = self.epi.transliterate('축하')
        self.assertEqual(tr, 't͡ɕʰukʰa')

    def test_kap(self):
        tr = self.epi.transliterate('값')
        self.assertEqual(tr, 'kap')

    def test_antsa(self):
        tr = self.epi.transliterate('앉아')
        self.assertEqual(tr, 'ant͡ɕa')

    def test_kungmul(self):
        tr = self.epi.transliterate('국물')
        self.assertEqual(tr, 'kuŋmul')

    def test_ppalli(self):
        tr = self.epi.transliterate('빨리')
        self.assertEqual(tr, 'p͈alli')

    def test_silla(self):
        tr = self.epi.transliterate('신라')
        self.assertEqual(tr, 'silla')

    def test_kutsi(self):
        tr = self.epi.transliterate('굳이')
        self.assertEqual(tr, 'kut͡ɕi')

    def test_tsotha(self):
        tr = self.epi.transliterate('좋다')
        self.assertEqual(tr, 't͡ɕotʰa')

    def test_nala(self):
        tr = self.epi.transliterate('날아')
        self.assertEqual(tr, 'nala')

    def test_mit(self):
        tr = self.epi.transliterate('밑')
        self.assertEqual(tr, 'mit')