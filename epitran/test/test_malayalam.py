# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestMalayalamGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'mal-Mlym')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_malayalam(self):
        self._assert_trans('മലയാളം', 'malajaːɭam')

    def test_kala(self):
        self._assert_trans('കല', 'kala')

    def test_eniykk(self):
        self._assert_trans('എനിയ്ക്ക്', 'enijkkə')

class TestMalayalamFaDisambiguation(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('mal-Mlym')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        # print('{}\t{}\t{}'.format(trans, tar, zip(trans, tar)))
        self.assertEqual(trans, tar)

    def test_phalam(self):
        self._assert_trans('ഫലം', 'pʰalam')

    def test_fan(self):
        self._assert_trans('ഫാൻ', 'faːn')

class TestMalayalamDentalAlveolarNasalDisambiguation(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('mal-Mlym')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        src = unicodedata.normalize('NFD', trans)
        self.assertEqual(trans, tar)

    def test_nannayi(self):
        self._assert_trans('നന്നായി', 'n̪an̪n̪aːji')

    def test_nanavu(self):
        self._assert_trans('നനവ്', 'n̪anaʋə')

    def test_sneham(self):
        self._assert_trans('സ്നേഹം', 'sneːɦam')
