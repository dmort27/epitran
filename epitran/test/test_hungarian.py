# -*- coding: utf-8 -*-

import unittest
import unicodedata

import epitran


class TestHungarianGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'hun-Latn')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_fiaei(self):
        self._assert_trans('fiáéi', 'fiaːeːi')

    def test_fiaiei(self):
        self._assert_trans('fiaiéi', 'fiɒieːi')

    def test_baratnoje(self):
        self._assert_trans('barátnője', 'bɒraːtnøːjɛ')

    def test_magyar(self):
        self._assert_trans('magyar', 'mɒɟɒr')

    def test_nagyszulo(self):
        self._assert_trans('nagyszülő', 'nɒɟsyløː')  # is actually pronounced as nat͡sːyløː

    def test_hang(self):
        self._assert_trans('hang', 'hɒŋ')

    def test_henger(self):
        self._assert_trans('henger', 'hɛŋɡɛr')

    def test_hangtan(self):
        self._assert_trans('hangtan', 'hɒŋtɒn')

    def test_gyongy(self):
        self._assert_trans('gyöngy', 'ɟøɲɟ')
