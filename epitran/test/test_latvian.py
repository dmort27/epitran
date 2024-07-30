# -*- coding: utf-8 -*-
# code base taken from Epitran Bengali test at
# https://github.com/dmort27/epitran/blob/master/epitran/test/test_bengali.py

from __future__ import unicode_literals

import unittest

class TestLatvian(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('lav-Latn')
    def test_(self):
        tr = self.epi.transliterate('dadži')
        self.assertEqual(tr, 'dad͡ʒi')
    def test_(self):
        tr = self.epi.transliterate('ikdiena')
        self.assertEqual(tr, 'igdiɛna')
    def test_(self):
        tr = self.epi.transliterate('ģērbt ')
        self.assertEqual(tr, 'ɟɛːrpt')
    def test_(self):
        tr = self.epi.transliterate('bungas')
        self.assertEqual(tr, 'buŋgas')
    def test_(self):
        tr = self.epi.transliterate('skābs')
        self.assertEqual(tr, 'skaːps')
    def test_(self):
        tr = self.epi.transliterate('vārdnīca')
        self.assertEqual(tr, 'vaːrdniːt͡sa')
    def test_(self):
        tr = self.epi.transliterate('mežs')
        self.assertEqual(tr, 'mɛʃː')
    def test_(self):
        tr = self.epi.transliterate('celts')
        self.assertEqual(tr, 't͡sælt͡s')
    def test_(self):
        tr = self.epi.transliterate('sods')
        self.assertEqual(tr, 'suɔt͡s')
    def test_(self):
        tr = self.epi.transliterate('ņemt')
        self.assertEqual(tr, 'ɲɛmt')
    def test_(self):
        tr = self.epi.transliterate('režīms')
        self.assertEqual(tr, 'rɛʒiːms')