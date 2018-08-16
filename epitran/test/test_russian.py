# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestRussian(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'rus-Cyrl')

    def test_straitilstva(self):
        tr = self.epi.transliterate('строительство')
        self.assertEqual(tr, 'stroitʲelʲstvo')

    def test_gasurdarstva(self):
        tr = self.epi.transliterate('государство')
        self.assertEqual(tr, 'ɡosudarstvo')

    def test_vzglat(self):
        tr = self.epi.transliterate('взгляд')
        self.assertEqual(tr, 'vzɡlʲad')
