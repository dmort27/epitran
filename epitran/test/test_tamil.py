# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import _epitran


class TestTamilGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'tam-Taml')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_tamil(self):
        self._assert_trans('தமிழ்', 't̪amiɻ')

    def test_eluttu(self):
        self._assert_trans('எழுத்து', 'eɻut̪t̪u')

    def test_num1(self):
        self._assert_trans('சூனியங்கள்', 't͡ʃuːnijaŋkaɭ')

    def test_num2(self):
        self._assert_trans('துர்தேவதைகள்', 't̪uɾt̪eːʋat̪ajkaɭ')

    def test_num3(self):
        self._assert_trans('தகவல்களைக்', 't̪akaʋalkaɭajk')

    def test_num4(self):
        self._assert_trans('நேரடித்', 'n̪eːɾaʈit̪')

    def test_num5(self):
        self._assert_trans('குலதெய்வத்தை', 'kulat̪ejʋat̪t̪aj')

    def test_num6(self):
        self._assert_trans('ஆத்மா', 'aːt̪maː')
