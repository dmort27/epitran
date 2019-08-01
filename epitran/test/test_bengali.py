# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestBengaliGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'ben-Beng')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_somosto(self):
        self._assert_trans('সমস্ত', 's̪ɔmɔs̪t̪ɔ')

    def test_manush(self):
        self._assert_trans('মানুষ', 'man̪uʂ')

    def test_sbadinbabe(self):
        self._assert_trans('স্বাধীনভাবে', 's̪bad̪̤in̪b̤abe')

    def test_shoman(self):
        self._assert_trans('সমান', 's̪ɔman̪')

    def test_morjada(self):
        self._assert_trans('মর্যাদা', 'mɔrd͡zad̪a')

    def test_ebong(self):
        self._assert_trans('এবং', 'ebɔŋ')

    def test_odikar(self):
        self._assert_trans('অধিকার', 'od̪̤ikar')

    def test_niye(self):
        self._assert_trans('নিয়ে', 'n̪ie̯e')
