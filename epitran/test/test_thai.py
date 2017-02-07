# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestGeneral(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'tha-Thai')

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

    def test_lek_hindu_chunlaphak(self):
        self._assert_trans('จุลภาค', 't͡ɕunpʰaːk')

    def test_lek_thai(self):
        self._assert_trans('เลขไทย', 'leːktʰaj')

    def test_okson(self):
        self._assert_trans('อักษร', 'ʔakson')

    def test_ngan(self):
        self._assert_trans('เงิน', 'ŋɤn')

    def test_pheq(self):
        self._assert_trans('แพะ', 'pʰɛʔ')

    def test_kriit(self):
        self._assert_trans('กรีด', 'kriːt')

    def test_phasaphut(self):
        self._assert_trans('ภาษาพูด', 'pʰaːsaːpʰuːt')

    def test_phasakhian(self):
        self._assert_trans('ภาษาเขียน', 'pʰaːsaːkʰiːa̯n')

    def test_rachasap(self):
        self._assert_trans('ราชาศัพท์', 'raːt͡ɕʰaːsap')

    def test_maatraa(self):
        self._assert_trans('มาตรา', 'maːtraː')

    def test_inthra(self):
        self._assert_trans('อินทรา', 'ʔintʰraː')

    def test_mak(self):
        self._assert_trans('มัก', 'mak')

    def test_maak(self):
        self._assert_trans('มาก', 'maːk')
