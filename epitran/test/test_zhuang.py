# -*- coding: utf-8 -*-


import unittest

import epitran


class TestZhuang(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('zha-Latn')

    def test_boux(self):
        tr = self.epi.transliterate('boux')
        self.assertEqual(tr, 'poːu')

    def test_daengz(self):
        tr = self.epi.transliterate('daengz')
        self.assertEqual(tr, 'taŋ')

    def test_lajmbwn(self):
        tr = self.epi.transliterate('lajmbwn')
        self.assertEqual(tr, 'laːɓɯn')

    def test_cinhyenz(self):
        tr = self.epi.transliterate('cinhyenz')
        self.assertEqual(tr, 'ɕinjen')
