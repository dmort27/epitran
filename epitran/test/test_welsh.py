# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestWelsh(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'cym-Latn')

    def test_afonfarch(self):
        tr = self.epi.transliterate('afonfarch')
        self.assertEqual(tr, 'avɔnvarχ')

    def test_bysgota(self):
        tr = self.epi.transliterate('bysgota')
        self.assertEqual(tr, 'bəsɡɔta')

    def test_ysgrif(self):
        tr = self.epi.transliterate('ysgrif')
        self.assertEqual(tr, 'əsɡrɪv')

    def test_cachgwn(self):
        tr = self.epi.transliterate('cachgwn')
        self.assertEqual(tr, 'kaχɡʊn')

    def test_cheri(self):
        tr = self.epi.transliterate('cheri')
        self.assertEqual(tr, 'χɛrɪ')

    def test_iyrchod(self):
        tr = self.epi.transliterate('iyrchod')
        self.assertEqual(tr, 'jərχɔd')

    def test_sorgwm(self):
        tr = self.epi.transliterate('sorgwm')
        self.assertEqual(tr, 'sɔrɡʊm')

    def test_ysgadan(self):
        tr = self.epi.transliterate('ysgadan')
        self.assertEqual(tr, 'əsɡadan')
