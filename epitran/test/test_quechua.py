# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestQuechua(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('quy-Latn')

    def test_runasimi(self):
        tr = self.epi.transliterate('runasimi')
        self.assertEqual(tr, 'rʊnæsɪmɪ')

    def test_siminchik(self):
        tr = self.epi.transliterate('siminchik')
        self.assertEqual(tr, 'sɪmɪntʃɪk')

    def test_nuqanchik(self):
        tr = self.epi.transliterate('ñuqanchik')
        self.assertEqual(tr, 'ɲʊχɑntʃɪk')

    def test_llamacha(self):
        tr = self.epi.transliterate('llamacha')
        self.assertEqual(tr, 'ʎæmætʃæ')
