# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import epitran

import sys
import io

# Set default encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

class TestEsperanto(unittest.TestCase):
    def setUp(self):
        # Ensure correct relative path for the files
        self.epi = epitran.Epitran('epo-Latn')
        
        # Assuming the preprocessor and postprocessor read the files
        with open('pre/esp-Latn.txt', 'r') as f:
            self.preprocessor_rules = f.read()
        
        with open('post/esp-Latn.txt', 'r') as f:
            self.postprocessor_rules = f.read()
        
        # Make sure your mapping file path is also correct
        self.mapping_file = 'map/esp-Latn.csv'

    def test_ajo(self):
        tr = self.epi.transliterate('ajo')
        self.assertEqual(tr, 'ajo')

    def test_cxar(self):
        tr = self.epi.transliterate('ĉar')
        self.assertEqual(tr, 't͡ʃar')

    def test_sxi(self):
        tr = self.epi.transliterate('ŝi')
        self.assertEqual(tr, 'ʃi')

    def test_diphthong(self):
        tr = self.epi.transliterate('aŭ')
        # Allow both 'au̯' and 'a̯u' as valid
        self.assertTrue(tr in ['au̯', 'a̯u'])

    def test_special_characters(self):
        # Test for special characters like 'ĵ', which becomes 'ʒ'
        tr = self.epi.transliterate('ĵa')
        self.assertEqual(tr, 'ʒa')

    def test_combination(self):
        # Test a word with multiple special characters and diphthongs
        tr = self.epi.transliterate('ĉu')
        self.assertEqual(tr, 't͡ʃu')

    def test_empty_string(self):
        # Test an empty string (should return empty string)
        tr = self.epi.transliterate('')
        self.assertEqual(tr, '')

    def test_edge_case(self):
        # Test edge case with mixed characters
        tr = self.epi.transliterate('superĉar')
        self.assertEqual(tr, 'supert͡ʃar')


if __name__ == "__main__":
    unittest.main()
