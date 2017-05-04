# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestTeluguGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'tel-Telu')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_telugu(self):
        self._assert_trans('తెలుగు', 't̪elʊɡu')

    def test_num1(self):
        self._assert_trans('ఆంధ్ర', 'and̪̤rə')

    def test_num2(self):
        self._assert_trans('తెలంగాణ', 't̪eləŋɡaɳə')

    def test_num3(self):
        self._assert_trans('మచిలీపట్నం', 'mət͡ʃɪliːpəʈnəm')

    def test_num4(self):
        self._assert_trans('హైదరాబాద్', 'həɪd̪ərabad̪')

    def test_num5(self):
        self._assert_trans('ముఖ్యమంత్రి', 'mʊkʰjəmənt̪ri')

    def test_num6(self):
        self._assert_trans('భాష','b̤aʂə')

    def test_num7(self):
        self._assert_trans('విద్యారంగంలో', 'ʋɪd̪jarəŋɡəmloː')
