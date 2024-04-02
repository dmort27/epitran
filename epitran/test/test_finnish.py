# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestFinnish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'fin-Latn')

    def test_tuulenhenkays(self):
        tr = self.epi.transliterate('tuulenhenkäys')
        self.assertEqual(tr, 'tu:lenheŋkæys')

    def test_parekattoon(self):
        tr = self.epi.transliterate('pärekattoon')
        self.assertEqual(tr, 'pærekɑt:o:n')

    def test_keinuvat(self):
        tr = self.epi.transliterate('keinuvat')
        self.assertEqual(tr, 'keinuʋɑt')

    # rules for /h/
    def test_hamu(self):
        tr = self.epi.transliterate('haamu')
        self.assertEqual(tr, 'hɑ:mu')

    def test_vihko(self):
        tr = self.epi.transliterate('vihko')
        self.assertEqual(tr, 'ʋiçko')

    def test_kohme(self):
        tr = self.epi.transliterate('kohme')
        self.assertEqual(tr, 'koxme')

    def test_vaha(self):
        tr = self.epi.transliterate('vähä')
        self.assertEqual(tr, 'ʋæɦæ')

    # rules for /m/
    def test_amfetamiini(self):
        tr = self.epi.transliterate('amfetamiini')
        self.assertEqual(tr, 'ɑɱfetɑmi:ni')

    # rules for /n/
    def test_kalenteri(self):
        tr = self.epi.transliterate('kalenteri')
        self.assertEqual(tr, 'kɑlen̪teri')

    def test_luutnantti(self):
        tr = self.epi.transliterate('luutnantti')
        self.assertEqual(tr, 'lu:tn̪ɑn̪t:i')

    def test_menna(self):
        tr = self.epi.transliterate('mennä')
        self.assertEqual(tr, 'men:æ')

    # rules for /l/
    def test_atlas(self):
        tr = self.epi.transliterate('atlas')
        self.assertEqual(tr, 'ɑtl̪ɑs')

    def test_iltapaivaa(self):
        tr = self.epi.transliterate('iltapäivää')
        self.assertEqual(tr, 'il̪tɑpæiʋæ:')

    # rules for /r/
    def test_paras(self):
        tr = self.epi.transliterate('paras')
        self.assertEqual(tr, 'pɑrɑs')

    def test_parras(self):
        tr = self.epi.transliterate('parras')
        self.assertEqual(tr, 'pɑr:ɑs')

    def test_einesruoka(self):
        tr = self.epi.transliterate('einesruoka')
        self.assertEqual(tr, 'einexruokɑ')

    # rules for v
    def test_sauva(self):
        tr = self.epi.transliterate('sauva')
        self.assertEqual(tr, 'sɑuwɑ')

    # rules for phonetic nasal
    def test_lanka(self):
        tr = self.epi.transliterate('lanka')
        self.assertEqual(tr, 'lɑŋkɑ')

    def test_sangen(self):
        tr = self.epi.transliterate('sangen')
        self.assertEqual(tr, 'sɑŋ:en')

    def test_magneetti(self):
        tr = self.epi.transliterate('magneetti')
        self.assertEqual(tr, 'mɑŋne:t:i')