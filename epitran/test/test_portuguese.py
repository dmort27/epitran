# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestPortuguese(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('por-Latn')

    def test_brasil(self):
        tr = self.epi.transliterate('Brasil')
        self.assertEqual(tr, 'bɾɐzil')

    def test_boia(self):
        tr = self.epi.transliterate('bóia')
        self.assertEqual(tr, 'bɔjɐ')

    def test_orgao(self):
        tr = self.epi.transliterate('órgão')
        self.assertEqual(tr, 'ɔɾɡɐ̃w̃')

    def test_convem(self):
        tr = self.epi.transliterate('convêm')
        self.assertEqual(tr, unicodedata.normalize('NFC', 'konvẽ'))

    def test_guitarra(self):
        tr = self.epi.transliterate('guitarra')
        self.assertEqual(tr, 'ɡʷitɐʁɐ')
