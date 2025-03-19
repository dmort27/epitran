import unittest
from epitran import Epitran

class TestLuganda(unittest.TestCase):
    def setUp(self):
        self.epi = Epitran('lug-Latn')
    
    def test_basic_conversions(self):
        self.assertEqual(self.epi.transliterate('a'), 'a')
        self.assertEqual(self.epi.transliterate('b'), 'b')
    
    def test_long_vowels(self):
        self.assertEqual(self.epi.transliterate('aa'), 'aː')
        self.assertEqual(self.epi.transliterate('ee'), 'eː')
    
    def test_prenasalized_consonants(self):
        self.assertEqual(self.epi.transliterate('mb'), 'ᵐb')
        self.assertEqual(self.epi.transliterate('nd'), 'ⁿd')
    
    def test_words(self):
        self.assertEqual(self.epi.transliterate('omuntu'), 'omuntu')
        self.assertEqual(self.epi.transliterate('eggulu'), 'eɡːulu')
