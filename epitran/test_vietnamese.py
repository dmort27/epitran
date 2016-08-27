# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import _epitran


class TestNormalizePunc(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'vie-Latn')

    def test_tieng(self):
        tr = self.epi.transliterate('tiếng')
        print(tr)
        self.assertEqual(tr, 'tiə̯ŋ')

    def test_viet(self):
        tr = self.epi.transliterate('Việt')
        print(tr)
        self.assertEqual(tr, 'viə̯t')

    def test_ngang(self):
        tr = self.epi.transliterate('ngang')
        print(tr)
        self.assertEqual(tr, 'ŋaːŋ')

    def test_huyen(self):
        tr = self.epi.transliterate('huyền')
        print(tr)
        self.assertEqual(tr, 'hwiə̯n')

    def test_sac(self):
        tr = self.epi.transliterate('sắc')
        print(tr)
        self.assertEqual(tr, 'sak')

    def test_hoi(self):
        tr = self.epi.transliterate('hỏi')
        print(tr)
        self.assertEqual(tr, 'hoj')

    def test_nga(self):
        tr = self.epi.transliterate('ngã')
        print(tr)
        self.assertEqual(tr, 'ŋɑː')

    def test_nang(self):
        tr = self.epi.transliterate('nặng')
        print(tr)
        self.assertEqual(, 'naŋ')
