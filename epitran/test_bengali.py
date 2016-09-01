# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import _epitran


class TestBengaliGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'ben-Beng')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_somosto(self):
        self._assert_trans('সমস্ত', 's̪omos̪t̪o')

    def test_manush(self):
        self._assert_trans('মানুষ', 'man̪uʂ')

    def test_sbadinbabe(self):
        self._assert_trans('স্বাধীনভাবে', 's̪bad̪̤in̪b̤abe')

    def test_shoman(self):
        self._assert_trans('সমান', 's̪oman̪')

    def test_morjada(self):
        self._assert_trans('মর্যাদা', 'mord͡zad̪a')

    def test_ebong(self):
        self._assert_trans('এবং', 'eboŋ')

    def test_odikar(self):
        self._assert_trans('অধিকার', 'od̪̤ikar')

    def test_niye(self):
        self._assert_trans('নিয়ে', 'n̪ie̯e')

    def test_dzonmorgrohon(self):
        self._assert_trans('জন্মগ্রহণ', 'd͡ʑon̪moɡroɦon')
