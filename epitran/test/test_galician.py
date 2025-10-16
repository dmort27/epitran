

import unittest

import epitran

class TestGalician(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('glg-Latn')

    def test_niño(self):
        tr = self.epi.transliterate('niño')
        self.assertEqual(tr, 'niɲʊ')

    def test_cruz(self):
        tr = self.epi.transliterate('cruz')
        self.assertEqual(tr, 'kɾuθ')

    def test_coller(self):
        tr = self.epi.transliterate('coller')
        self.assertEqual(tr, 'koʎeɾ')

    def test_rato(self):
        tr = self.epi.transliterate('rato')
        self.assertEqual(tr, 'ratʊ')

    def test_vida(self):
        tr = self.epi.transliterate('vida')
        self.assertEqual(tr, 'bidɐ')