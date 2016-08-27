# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import _epitran


class TestNormalizePunc(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'vie-Latn')

    def test_tieng(self):
        tr = self.epi.transliterate('tiếng')
        self.assertEqual(tr, 'tiə̯ŋ')

    def test_viet(self):
        tr = self.epi.transliterate('Việt')
        self.assertEqual(tr, 'viə̯t')

    def test_ngang(self):
        tr = self.epi.transliterate('ngang')
        self.assertEqual(tr, 'ŋaːŋ')

    def test_huyen(self):
        tr = self.epi.transliterate('huyền')
        self.assertEqual(tr, 'hwiə̯n')

    def test_sac(self):
        tr = self.epi.transliterate('sắc')
        self.assertEqual(tr, 'sak')

    def test_hoi(self):
        tr = self.epi.transliterate('hỏi')
        self.assertEqual(tr, 'hɔj')

    def test_nga(self):
        tr = self.epi.transliterate('ngã')
        self.assertEqual(tr, 'ŋaː')

    def test_nang(self):
        tr = self.epi.transliterate('nặng')
        self.assertEqual(tr, 'naŋ')
