# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestSorani(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'ckb-Arab')

    def test_afandii(self):
        tr = self.epi.transliterate('ئهفهندی')
        self.assertEqual(tr, 'ɛfɛndiː')

    def test_aliiktronii(self):
        tr = self.epi.transliterate('ئهليکترۆنى')
        self.assertEqual(tr, 'ɛliːktɾona')

    def test_barra(self):
        tr = self.epi.transliterate('بهڕه')
        self.assertEqual(tr, 'bɛrɛ')

    def test_daadga(self):
        tr = self.epi.transliterate('دادگــه')
        self.assertEqual(tr, 'dadɡɛ')
