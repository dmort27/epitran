# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestWesternSierraPueblaNahuatl(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('nhi-Latn')

    def test_monamictililuitl(self):
        tr = self.epi.transliterate('monamictililuitl')
        self.assertEqual(tr, 'monamiktililwit͡ɬ')

    def test_nej(self):
        tr = self.epi.transliterate('nej')
        self.assertEqual(tr, 'neh')
    
    def test_yej(self):
        tr = self.epi.transliterate('yej')
        self.assertEqual(tr, 'jeh')

    def test_ijkwak(self):
        tr = self.epi.transliterate('ijkwak')
        self.assertEqual(tr, 'ihkʷak')

    def test_okxikowaya(self): # non-ILV (w-u)
        tr = self.epi.transliterate('okxikowaya')
        self.assertEqual(tr, 'okʃikowaja')

    def test_ocxicouaya(self): # ILV orthography
        tr = self.epi.transliterate('ocxicouaya')
        self.assertEqual(tr, 'okʃikowaja')

    def test_tlaokoxtokej(self): # non-ILV (ke-que)
        tr = self.epi.transliterate('tlaokoxtokej')
        self.assertEqual(tr, 't͡ɬaokoʃtokeh')

    def test_tlaocoxtoqueh(self): # ILV orthography
        tr = self.epi.transliterate('tlaocoxtoqueh')
        self.assertEqual(tr, 't͡ɬaokoʃtokeh')

    def test_ikchiyas(self): # non-ILV (k-c)
        tr = self.epi.transliterate('ikchiyas')
        self.assertEqual(tr, 'ikt͡ʃijas')
    
    def test_icchiyas(self): # ILV orthography
        tr = self.epi.transliterate('icchiyas')
        self.assertEqual(tr, 'ikt͡ʃijas')

    def test_iitlakoyook(self): # non-ILV orthography (indicates vowel length)
        tr = self.epi.transliterate('iitlakoyook')
        self.assertEqual(tr, 'it͡ɬakojok')