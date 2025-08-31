# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestPashto(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('pbu-Arab')

    def test_basic_consonants(self):
        """Test basic consonant transliterations"""
        test_cases = [
            ('ب', 'b'),
            ('پ', 'p'),
            ('ت', 't'),
            ('ج', 'd͡ʒ'),
            ('چ', 't͡ʃ'),
            ('د', 'd'),
            ('ر', 'r'),
            ('ز', 'z'),
            ('س', 's'),
            ('ش', 'ʃ'),
            ('ف', 'f'),
            ('ق', 'q'),
            ('ك', 'k'),
            ('ل', 'l'),
            ('م', 'm'),
            ('ن', 'n'),
            ('ه', 'h'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_pashto_specific_consonants(self):
        """Test Pashto-specific consonant transliterations"""
        test_cases = [
            ('څ', 'ts'),
            ('ځ', 'dz'),
            ('ډ', 'ɖ'),
            ('ړ', 'ɽ'),
            ('ښ', 'ʂ'),
            ('ږ', 'ʐ'),
            ('ګ', 'ɡ'),
            ('ڼ', 'ɳ'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_vowels(self):
        """Test vowel transliterations"""
        test_cases = [
            ('ا', 'ɑ'),
            ('ي', 'i'),
            ('و', 'u'),
            ('ې', 'e'),
            ('ۍ', 'ai'),
            ('ئ', 'ə'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_vowel_diacritics(self):
        """Test vowel diacritic transliterations"""
        test_cases = [
            ('َ', 'ɑ'),
            ('ِ', 'i'),
            ('ُ', 'u'),
            ('ْ', 'ə'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_initial_alif_variations(self):
        """Test initial alif variations"""
        test_cases = [
            ('أ', 'ʔɑ'),
            ('إ', 'ʔi'),
            ('آ', 'ʔɑː'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_common_words(self):
        """Test common Pashto words"""
        test_cases = [
            ('پښتو', 'pəxto'),  # Pashto (language name)
            ('سلام', 'sɑlɑm'),  # Hello
            ('ښځه', 'ʂd͡zɑ'),   # Woman
            ('سړی', 'sɑɽɑi'),  # Man
            ('کور', 'kor'),     # House
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_consonant_clusters(self):
        """Test consonant cluster handling"""
        test_cases = [
            ('څځ', 'tsdz'),
            ('ښږ', 'ʂʐ'),
            ('ګګ', 'ɡɡ'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_gemination(self):
        """Test gemination handling"""
        test_cases = [
            ('بّ', 'bː'),
            ('دّ', 'dː'),
            ('سّ', 'sː'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_emphatic_consonants(self):
        """Test emphatic consonant transliterations"""
        test_cases = [
            ('ص', 'sˤ'),
            ('ض', 'dˤ'),
            ('ط', 'tˤ'),
            ('ظ', 'ðˤ'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_pharyngeal_consonants(self):
        """Test pharyngeal consonant transliterations"""
        test_cases = [
            ('ع', 'ʔ'),
            ('غ', 'ɣ'),
            ('ح', 'h'),
            ('خ', 'x'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_affricates(self):
        """Test affricate transliterations"""
        test_cases = [
            ('چ', 't͡ʃ'),
            ('څ', 'ts'),
            ('ځ', 'dz'),
            ('ج', 'd͡ʒ'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_retroflex_consonants(self):
        """Test retroflex consonant transliterations"""
        test_cases = [
            ('ډ', 'ɖ'),
            ('ړ', 'ɽ'),
            ('ڼ', 'ɳ'),
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_complex_words(self):
        """Test more complex Pashto words"""
        test_cases = [
            ('پښتون', 'pəxtun'),      # Pashtun (ethnic group)
            ('افغانستان', 'ɑfɣɑnstɑn'), # Afghanistan
            ('کابل', 'kɑbul'),        # Kabul
            ('پېښور', 'peʂor'),      # Peshawar
        ]
        for orth, expected in test_cases:
            with self.subTest(orth=orth):
                tr = self.epi.transliterate(orth)
                self.assertEqual(tr, expected)

    def test_word_to_tuples(self):
        """Test word_to_tuples method"""
        word = 'پښتو'
        tuples = self.epi.word_to_tuples(word)
        self.assertIsInstance(tuples, list)
        self.assertGreater(len(tuples), 0)
        
        # Check that each tuple has the expected structure
        for tup in tuples:
            self.assertIsInstance(tup, tuple)
            self.assertGreaterEqual(len(tup), 4)

    def test_trans_list(self):
        """Test trans_list method"""
        word = 'پښتو'
        segments = self.epi.trans_list(word)
        self.assertIsInstance(segments, list)
        self.assertGreater(len(segments), 0)
        
        # Check that segments are strings
        for seg in segments:
            self.assertIsInstance(seg, str)

    def test_strict_trans(self):
        """Test strict_trans method"""
        word = 'پښتو123'  # Mix of Pashto and non-Pashto characters
        tr = self.epi.strict_trans(word)
        # Should only contain IPA characters, no digits
        self.assertNotIn('1', tr)
        self.assertNotIn('2', tr)
        self.assertNotIn('3', tr)


if __name__ == '__main__':
    unittest.main()
