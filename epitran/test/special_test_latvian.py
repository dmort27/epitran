# -*- coding: utf-8 -*-
# code base taken from Epitran Bengali test at
# https://github.com/dmort27/epitran/blob/master/epitran/test/test_bengali.py

from __future__ import unicode_literals

import unittest
import epitran

class TestLatvian(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('lav-Latn')
    def test_dadzi(self):
        tr = self.epi.transliterate('dadži')
        self.assertEqual(tr, 'dad͡ʒi')
    def test_ikdiena(self):
        tr = self.epi.transliterate('ikdiena')
        self.assertEqual(tr, 'igdiɛna')
    def test_gerbt(self):
        tr = self.epi.transliterate('ģērbt')
        self.assertEqual(tr, 'ɟɛːrpt')
    def test_bungas(self):
        tr = self.epi.transliterate('bungas')
        self.assertEqual(tr, 'buŋgas')
    def test_skabs(self):
        tr = self.epi.transliterate('skābs')
        self.assertEqual(tr, 'skaːps')
    def test_vardnica(self):
        tr = self.epi.transliterate('vārdnīca')
        self.assertEqual(tr, 'vaːrdniːt͡sa')
    def test_mezs(self):
        tr = self.epi.transliterate('mežs')
        self.assertEqual(tr, 'mɛʃː')
    def test_celts(self):
        tr = self.epi.transliterate('celts')
        self.assertEqual(tr, 't͡sælt͡s')
    def test_sods(self):
        tr = self.epi.transliterate('sods')
        self.assertEqual(tr, 'suɔt͡s')
    def test_nemt(self):
        tr = self.epi.transliterate('ņemt')
        self.assertEqual(tr, 'ɲɛmt')
    def test_rezims(self):
        tr = self.epi.transliterate('režīms')
        self.assertEqual(tr, 'rɛʒiːms')
