# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestChinese(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('cmn-Hans', cedict_file='/home/dmortens/Downloads/cedict_1_0_ts_utf-8_mdbg.txt')

    def test_yu(self):
        tr = self.epi.transliterate('雨')
        self.assertEqual(tr, 'y')

    def test_pengyou(self):
        tr = self.epi.transliterate('朋友')
        self.assertEqual(tr, 'pʰəŋjou')
