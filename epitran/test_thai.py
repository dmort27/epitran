# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import _epitran


class TestGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'tha-Thai')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_thanon(self):
        self._assert_trans('ถนน', 'tʰanon')

    def test_phoq(self):
        self._assert_trans('เพาะ', 'pʰɔʔ')

    def test_bobaimai(self):
        self._assert_trans('บใบไม้', 'babajmaj')

    def test_maitaikhu(self):
        self._assert_trans('ไม้ไต่คู้', 'majtajkʰuː')

    def test_saraqa(self):
        self._assert_trans('สระอะ', 'saraʔaʔ')

    def test_klwwn(self):
        self._assert_trans('คลื่น', 'kʰlɯːn')

    def test_klong(self):
        self._assert_trans('กล่อง', 'klɔːŋ')

    def test_kloong(self):
        self._assert_trans('กลอง', 'klɔːŋ')

    def test_sut(self):
        self._assert_trans('สุด', 'sut')

    def test_suut(self):
        self._assert_trans('สูด', 'suːt')

    def test_en(self):
        self._assert_trans('เอ็น', 'ʔeːn')
