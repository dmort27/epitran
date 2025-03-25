# -*- coding: utf-8 -*-
# Unit test for Luganda G2P implementation in Epitran

from __future__ import unicode_literals

import unittest
import epitran

class TestLuganda(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('lug-Latn')
        
    def test_basic_vowels(self):
        tr = self.epi.transliterate('akala')
        self.assertEqual(tr, 'akala')
        
    def test_long_vowels(self):
        tr = self.epi.transliterate('abaana')
        self.assertEqual(tr, 'abaːna')
        
    def test_basic_consonants(self):
        tr = self.epi.transliterate('kubala')
        self.assertEqual(tr, 'kubala')
        
    def test_palatal_nasal(self):
        tr = self.epi.transliterate('enyama')
        self.assertEqual(tr, 'eɲama')
        
    def test_velar_nasal(self):
        tr = self.epi.transliterate('ng\'amba')
        self.assertEqual(tr, 'ŋaːᵐba')
        
    def test_prenasalized_bilabial(self):
        tr = self.epi.transliterate('embwa')
        self.assertEqual(tr, 'eːᵐbʷa')
        
    def test_prenasalized_alveolar(self):
        tr = self.epi.transliterate('endiga')
        self.assertEqual(tr, 'eːⁿdiɡa')
        
    def test_prenasalized_velar(self):
        tr = self.epi.transliterate('enkoko')
        self.assertEqual(tr, 'eːᵑkoko')
        
    def test_geminated_consonant(self):
        tr = self.epi.transliterate('essomero')
        self.assertEqual(tr, 'esːomeɾo')
        
    def test_affricate(self):
        tr = self.epi.transliterate('jjajja')
        self.assertEqual(tr, 'dʒːadʒːa')
        
    def test_prenasalized_affricate(self):
        tr = self.epi.transliterate('enjuki')
        self.assertEqual(tr, 'eːⁿdʒuki')
        
    def test_vowel_lengthening(self):
        tr = self.epi.transliterate('abantu')
        self.assertEqual(tr, 'abaːⁿtu')
        
    def test_final_devoicing(self):
        tr = self.epi.transliterate('omulwadde kirabikab')
        self.assertEqual(tr, 'omulʷadːe kiɾabikap')
        
    def test_complex_word(self):
        tr = self.epi.transliterate('omwana omuganda anyumirwa')
        self.assertEqual(tr, 'omʷana omuɡaːⁿda aɲumiɾwa')