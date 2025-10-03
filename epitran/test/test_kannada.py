# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import unicodedata
import epitran

class TestKannadaGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'kan-Knda')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        self.assertEqual(trans, tar)

    def test_kudi(self):
        self._assert_trans('ಕುಡಿ', 'kuɖi')
    
    def test_maiduna(self):
        self._assert_trans("ಮೈದುನ", "maid̪una")


class TestKannadaConsonantConjuncts(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'kan-Knda')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        self.assertEqual(trans, tar)

    def test_nanna(self):
        self._assert_trans('ನನ್ನ', 'nanna')

    def test_obba(self):
        self._assert_trans('ಒಬ್ಬ', 'obba')
    
    def test_atte(self):
        self._assert_trans('ಅತ್ತೆ', 'at̪t̪e')


class TestKannadaRaTransposition(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'kan-Knda')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        self.assertEqual(trans, tar)

    def test_karnataka(self):
        self._assert_trans("ಕರ್ನಾಟಕ", "karnaːʈaka")


class TestKannadaAnusvara(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'kan-Knda')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        self.assertEqual(trans, tar)

    def test_bengaluru(self):
        self._assert_trans("ಬೆಂಗಳೂರು", "beŋgaɭuːru")
    
    def test_kombu(self):
        self._assert_trans("ಕೊಂಬು", "kombu")

    def test_ante(self):
        self._assert_trans("ಅಂತೆ", "ant̪e")


class TestKannadaRetroflexSha(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'kan-Knda')

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize('NFD', trans)
        self.assertEqual(trans, tar)
    
    def test_june(self):
        self._assert_trans("ಜ್ಯೇಷ್ಠ", "dʒjeːʃʈʰa")


