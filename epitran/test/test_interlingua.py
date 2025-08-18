from __future__ import unicode_literals

import unittest
import epitran

class TestInterlingua(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran("ile-Latn")

    def test_quando(self):
        res = self.epi.transliterate("quando")
        self.assertEqual(res, "kwando")

    def test_chronic(self):
        res = self.epi.transliterate("chronic")
        self.assertEqual(res, "kronik")

    def test_cielo(self):
        res = self.epi.transliterate("cielo")
        self.assertEqual(res, "tʃelo")

    def test_gelato(self):
        res = self.epi.transliterate("gelato")
        self.assertEqual(res, "dʒlato")

    def test_philosophia(self):
        res = self.epi.transliterate("philosophia")
        self.assertEqual(res, "filozofia")

    def test_theatro(self):
        res = self.epi.transliterate("theatro")
        self.assertEqual(res, "teatro")

    def test_extra(self):
        res = self.epi.transliterate("extra")
        self.assertEqual(res, "ekstra")

    def test_jam(self):
        res = self.epi.transliterate("jam")
        self.assertEqual(res, "ʒam")

    def test_aereo(self):
        res = self.epi.transliterate("aereo")
        self.assertEqual(res, "aereo")

    def test_universo(self):
        res = self.epi.transliterate("universo")
        self.assertEqual(res, "universo")

if __name__ == '__main__':
    unittest.main()
