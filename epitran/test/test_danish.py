# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import epitran


class TestDanish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('dan-Latn')

        def test_1(self):
            res = self.epi.transliterate("jazz")
            self.assertEqual(res, "ɕass")

        def test_2(self):
            res = self.epi.transliterate("lærer")
            self.assertEqual(res, "lɛɐ̯ɐʁ")

        def test_3(self):
            res = self.epi.transliterate("får")
            self.assertEqual(res, "fɔɐ̯")

        def test_4(self):
            res = self.epi.transliterate("tyve")
            self.assertEqual(res, "tyːvɐ")

        def test_5(self):
            res = self.epi.transliterate("synge")
            self.assertEqual(res, "søŋgɐ")

        def test_6(self):
            res = self.epi.transliterate("dårlig")
            self.assertEqual(res, "dɔɐ̯lig")

        def test_7(self):
            res = self.epi.transliterate("bånd")
            self.assertEqual(res, "bʌnd")

        def test_8(self):
            res = self.epi.transliterate("nat")
            self.assertEqual(res, "nɛt")

        def test_9(self):
            res = self.epi.transliterate("aften")
            self.assertEqual(res, "ɛftɛn")

        def test_10(self):
            res = self.epi.transliterate("hej")
            self.assertEqual(res, "haɪ")

        def test_11(self):
            res = self.epi.transliterate("sejle")
            self.assertEqual(res, "saɪlɐ")


if __name__ == "__main__":
    unittest.main()
