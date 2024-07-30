# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestEsperanto(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('epo-Latn')

    def test_ajo(self):
        tr = self.epi.transliterate('ajo')
        self.assertEqual(tr, 'ajo')

    def test_cxar(self):
        tr = self.epi.transliterate('ĉar')
        self.assertEqual(tr, 't͡ʃar')

    def test_sxi(self):
        tr = self.epi.transliterate('ŝi')
        self.assertEqual(tr, 'ʃi')
