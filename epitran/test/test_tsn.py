import unittest
import epitran

class TestSetswana(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('tsn-Latn')

    def test_simple_words(self):
        tests = {
            'bana': 'bana',
            'tlhapi': 'tɬʰapi',
            'ngaka': 'ŋaka',
            'laeborari': 'laɪbʊrari',
            'phiri': 'pʰiri',
            'motsadi': 'mʊtsadi',
            'mophane': 'mʊpʰanɪ',
            'phala': 'pʰala',
            'lekatane': 'lɪkatanɪ',
            'lodule': 'lʊdulɪ',
            'tshwene': 'tsʰwenɪ',
            'sebete': 'sɪbetɪ',
            'lefoko': 'lɪfʊkʊ',
            'ntšhe': 'ntʃʰɪ',
            'bojalwa': 'bʊdʒalwa',
            'mokabaowane': 'mʊkabaʊwanɪ'
        }
        for word, expected in tests.items():
            with self.subTest(word=word):
                result = self.epi.transliterate(word)
                self.assertEqual(result, expected)
