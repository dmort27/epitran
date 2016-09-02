# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import unicodedata

import _epitran


class TestHungarianGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'hun-Latn')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_fiaei(self):
        self._assert_trans('fiáéi', 'fiaːeːi')

    def test_baratnoje(self):
        self._assert_trans('barátnője', 'bɒraːtnøːjɛ')

    def test_magyar(self):
        self._assert_trans('magyar', 'mɒɟɒr')

    def test_(self):
        self._assert_trans('nagyszülő', 'nɒɟsyløː')
