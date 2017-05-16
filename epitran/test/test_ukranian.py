# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestPolish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('ukr-Cyrl')

    def test_ju(self):
        tr = self.epi.transliterate('ю')
        self.assertEqual(tr, 'ju')
        
    def test_djim(self):
        tr = self.epi.transliterate('дім')
        self.assertEqual(tr, 'dʲim')
        
    def test_midj(self):
        tr = self.epi.transliterate('мідь')
        self.assertEqual(tr, 'midʲ')
        
    def test_nebo(self):
        tr = self.epi.transliterate('небо')
        self.assertEqual(tr, 'nɛbɔ')
