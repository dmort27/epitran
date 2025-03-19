import unittest
from epitran import Epitran

class TestLuganda(unittest.TestCase):
    def setUp(self):
        self.epi = Epitran('lug-Latn')
    
    def test_basic_consonant(self):
        tr = self.epi.transliterate('baba')
        self.assertEqual(tr, 'baba')
        
    def test_prenasalized(self):
        tr = self.epi.transliterate('mbwa')
        self.assertEqual(tr, 'ᵐbʷa')
        
    def test_long_vowel(self):
        tr = self.epi.transliterate('baaba')
        self.assertEqual(tr, 'baːba')
        
    def test_palatal_nasal(self):
        tr = self.epi.transliterate('nyama')
        self.assertEqual(tr, 'ɲama')
        
    def test_velar_nasal(self):
        tr = self.epi.transliterate('ng\'amba')
        self.assertEqual(tr, 'ŋaᵐba')
        
    def test_labialized(self):
        tr = self.epi.transliterate('ekitwala')
        self.assertEqual(tr, 'ekitʷala')
        
    def test_geminated(self):
        tr = self.epi.transliterate('attabi')
        self.assertEqual(tr, 'atːabi')
        
    def test_affricate(self):
        tr = self.epi.transliterate('jjajja')
        self.assertEqual(tr, 'dʒːadʒːa')
        
    def test_prenasalized_affricate(self):
        tr = self.epi.transliterate('njovu')
        self.assertEqual(tr, 'ⁿdʒovu')
        
    def test_vowel_length_before_prenasalized(self):
        tr = self.epi.transliterate('abantu')
        self.assertEqual(tr, 'abaːⁿtu')
        
    def test_compound_word(self):
        tr = self.epi.transliterate('eggulu')
        self.assertEqual(tr, 'eɡːulu')
        
    def test_complex_word(self):
        tr = self.epi.transliterate('kyaddala')
        self.assertEqual(tr, 'tʃadːala')