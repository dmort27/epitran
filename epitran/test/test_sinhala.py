# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestSinhalaGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'sin-Sinh')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_alapila(self):
        self._assert_trans('ඇලපිල්ල', 'ælapilla')

    def test_kombuva(self):
        self._assert_trans('කොම්බුව', 'kombuva')

    def test_deka(self):
        self._assert_trans('දෙක', 'deka')
