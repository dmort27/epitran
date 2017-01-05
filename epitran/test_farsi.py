# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import _epitran


class TestSorani(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'fas-Arab')

    def test_faarsi(self):
        tr = self.epi.transliterate('فارسی')
        self.assertEqual(tr, 'fɒːrsiː')

    def test_(self):
        tr = self.epi.transliterate('روشن')
        self.assertEqual(tr, 'rowʃn')
