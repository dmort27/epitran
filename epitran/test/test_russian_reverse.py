# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestRussian(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'rus-Cyrl', rev=True)

    def _assert_reverse(self, ipa, text):
        tr = self.epi.reverse_transliterate(ipa)
        self.assertEqual(tr, text)

    # Test Russian words

    def test_vzglat(self):
        self._assert_reverse('vzɡlʲad', 'взгляд')

    def test_med(self):
        self._assert_reverse('mʲod', 'мёд')

    def test_medik(self):
        self._assert_reverse('mʲedʲik', 'медик')

    def test_yula(self):
        self._assert_reverse('jula', 'юла')

    def test_yel(self):
        self._assert_reverse('jelʲ', 'ель')

    def test_yama(self):
        self._assert_reverse('jama', 'яма')

    def test_musli(self):
        self._assert_reverse('mʲuslʲi', 'мюсли')

    def test_podyezd(self):
        self._assert_reverse('podʲjezd', 'подъезд')

    def test_izyavit(self):
        self._assert_reverse('izʲjavʲitʲ', 'изъявить')

    def test_zhena(self):
        self._assert_reverse('ʒena', 'жена')

    def test_shest(self):
        self._assert_reverse('ʂest', 'шест')

    def test_chem(self):
        self._assert_reverse('t͡ɕem', 'чем')

    def test_shchel(self):
        self._assert_reverse('ɕɕelʲ', 'щель')

    def test_tsel(self):
        self._assert_reverse('t͡selʲ', 'цель')