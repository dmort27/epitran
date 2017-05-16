# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestPolish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('pol-Latn')

    def test_dania(self):
        tr = self.epi.transliterate('dania')
        self.assertEqual(tr, 'daɲa')

    def test_dan(self):
        tr = self.epi.transliterate('dań')
        self.assertEqual(tr, 'daɲ')

    def test_danii(self):
        tr = self.epi.transliterate('Danii')
        self.assertEqual(tr, 'daɲji')

    def test_mania(self):
        tr = self.epi.transliterate('Mania')
        self.assertEqual(tr, 'maɲa')

    def test_mani(self):
        tr = self.epi.transliterate('Mani')
        self.assertEqual(tr, 'maɲi')

    def test_manii(self):
        tr = self.epi.transliterate('manii')
        self.assertEqual(tr, 'maɲji')

    def test_kat(self):
        tr = self.epi.transliterate('kąt')
        self.assertEqual(tr, 'kɔnt')

    def test_geba(self):
        tr = self.epi.transliterate('gęba')
        self.assertEqual(tr, 'ɡɛmba')

    def test_piec(self):
        tr = self.epi.transliterate('pięć')
        self.assertEqual(tr, 'pjɛɲt͡ɕ')

    def test_nie(self):
        tr = self.epi.transliterate('nie')
        self.assertEqual(tr, 'ɲɛ')

    def test_szybko(self):
        tr = self.epi.transliterate('szybko')
        self.assertEqual(tr, 'ʂɨbkɔ')

    def test_dziadek(self):
        tr = self.epi.transliterate('dziadek')
        self.assertEqual(tr, 'd͡ʑadɛk')

    def test_jas(self):
        tr = self.epi.transliterate('Jaś')
        self.assertEqual(tr, 'jaɕ')

    def test_gienek(self):
        tr = self.epi.transliterate('Gienek')
        self.assertEqual(tr, 'ɡʲɛnɛk')
