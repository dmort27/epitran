# -*- coding: utf-8 -*-
# Expanded unit test for Luganda G2P implementation in Epitran

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
        
    def test_vowel_length_minimal_pairs(self):
        tr1 = self.epi.transliterate('kula')
        tr2 = self.epi.transliterate('kuula')
        self.assertEqual(tr1, 'kula')
        self.assertEqual(tr2, 'kuːla')
        
    def test_word_final_vowel_length(self):
        tr = self.epi.transliterate('omulimuu')
        self.assertEqual(tr, 'omulimuː')
        
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
        
    def test_geminated_consonants_different_positions(self):
        tr1 = self.epi.transliterate('ttima')
        tr2 = self.epi.transliterate('matta')
        self.assertEqual(tr1, 'tːima')
        self.assertEqual(tr2, 'matːa')
    
    def test_affricate(self):
        tr = self.epi.transliterate('jjajja')
        self.assertEqual(tr, 'dʒːadʒːa')
        
    def test_prenasalized_affricate(self):
        tr = self.epi.transliterate('enjuki')
        self.assertEqual(tr, 'eːⁿdʒuki')
        
    def test_vowel_lengthening(self):
        tr = self.epi.transliterate('abantu')
        self.assertEqual(tr, 'abaːⁿtu')
        
    def test_vowel_lengthening_before_prenasalized(self):
        tr = self.epi.transliterate('omuntu')
        self.assertEqual(tr, 'omuːⁿtu')
        
    def test_final_devoicing(self):
        tr = self.epi.transliterate('omulwadde kirabikab')
        self.assertEqual(tr, 'omulʷadːe kiɾabikap')
        
    def test_complex_word(self):
        tr = self.epi.transliterate('omwana omuganda anyumirwa')
        self.assertEqual(tr, 'omʷana omuɡaːⁿda aɲumiɾwa')
        
    def test_labialization(self):
        tr1 = self.epi.transliterate('omwami')
        tr2 = self.epi.transliterate('ekwano')
        self.assertEqual(tr1, 'omʷami')
        self.assertEqual(tr2, 'ekʷano')
        
    def test_labialization_with_different_vowels(self):
        tr1 = self.epi.transliterate('gwana')
        tr2 = self.epi.transliterate('bweta')
        tr3 = self.epi.transliterate('fwena')
        self.assertEqual(tr1, 'ɡʷana')
        self.assertEqual(tr2, 'bʷeta')
        self.assertEqual(tr3, 'fʷena')
        
    def test_vowel_hiatus(self):
        tr = self.epi.transliterate('baagala')
        self.assertEqual(tr, 'baːɡala')
        
    def test_compound_words(self):
        tr = self.epi.transliterate('olunyiriri')
        self.assertEqual(tr, 'oluɲiɾiɾi')
        
    def test_syllable_structure(self):
        tr1 = self.epi.transliterate('ka')
        tr2 = self.epi.transliterate('ndi')
        tr3 = self.epi.transliterate('awo')
        self.assertEqual(tr1, 'ka')
        self.assertEqual(tr2, 'ⁿdi')
        self.assertEqual(tr3, 'awo')
        
    def test_high_tone(self):
        tr = self.epi.transliterate('okúsoma')
        self.assertEqual(tr, 'okúsoma')
        
    def test_low_tone(self):
        tr = self.epi.transliterate('okusoma')
        self.assertEqual(tr, 'okusoma')
        
    def test_borrowed_words(self):
        tr2 = self.epi.transliterate('telefoni')
        self.assertEqual(tr2, 'telefoni')
        
    def test_apostrophe_usage(self):
        tr1 = self.epi.transliterate('n\'somesa')
        tr2 = self.epi.transliterate('ng\'enda')
        self.assertEqual(tr1, 'ⁿsomesa')
        self.assertEqual(tr2, 'ŋeːⁿda')
        
    def test_multiple_rule_interaction(self):
        tr = self.epi.transliterate('ng\'atto')
        self.assertEqual(tr, 'ŋatːo')
        
    def test_edge_cases(self):
        tr1 = self.epi.transliterate('mw')
        tr2 = self.epi.transliterate('nnyumba')
        self.assertEqual(tr1, 'mʷ')
        self.assertEqual(tr2, 'ɲːuːᵐba')
        
    def test_common_phrases(self):
        tr = self.epi.transliterate('webale nyo')
        self.assertEqual(tr, 'webale ɲo')