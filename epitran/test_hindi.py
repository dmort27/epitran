# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import unicodedata
import unittest

import _epitran


class TestHindiHalant(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran('hin-Deva')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_knay(self):
        self._assert_trans('क्नय्', 'knəj')


class TestHindiSchwaDel(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran('hin-Deva')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_lapeta(self):
        self._assert_trans('लपट', 'ləpəʈ')

    def test_lapeten(self):
        self._assert_trans('लपटें', 'ləpʈen')

    def test_samjha(self):
        self._assert_trans('समझ', 'səməd͡ʒ̤')

    def test_bhaarata(self):
        self._assert_trans('भारत', 'b̤aːrət')

    def test_bhaaratiiya(self):
        self._assert_trans('भारतीय', 'b̤aːrtiːj')

    def test_devnaagrii1(self):
        self._assert_trans('देवनागरी', 'devnaːɡriː')

    def test_devnaagrii2(self):  # Nonce
        self._assert_trans('ेवनागरी', 'evnaːɡriː')

    def test_ingalisha(self):
        self._assert_trans('इंगलिश', 'iŋɡliʃ')

    def test_vimalaa(self):
        self._assert_trans('विमला', 'vimlaː')

    def test_sulochanaa(self):
        self._assert_trans('सुलोचना', 'sulot͡ʃnaː')

    def test_raam(self):
        self._assert_trans('राम', 'raːm')

    def test_rachanaa(self):
        self._assert_trans('रचना', 'rət͡ʃnaː')

    def test_veda(self):
        self._assert_trans('वेद', 'ved')

    def test_namakiina(self):
        self._assert_trans('नमकीन', 'nəmkiːn')

    def test_taanadaa(self):  # Nonce
        self._assert_trans('तानदा', 'taːndaː')
