# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestTigrinya(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('tir-Ethi-pp')

    def test_bee(self):
        tr = self.epi.transliterate('ንህቢ')
        self.assertEqual(tr, 'nɨhbi')

    def test_bees(self):
        tr = self.epi.transliterate('ኣናህብ')
        self.assertEqual(tr, 'ʔanahɨb')

    def test_cry(self):
        tr = self.epi.transliterate('ምብካይ')
        self.assertEqual(tr, 'mɨbkaj')

    def test_he_cried(self):
        tr = self.epi.transliterate('በኸየ')
        self.assertEqual(tr, 'bəxəjə')

    def test_they_steal(self):
        tr = self.epi.transliterate('ይሰርቁ')
        self.assertEqual(tr, 'jɨsərqu')

    def test_he_steals(self):
        tr = self.epi.transliterate('ይሰርቕ')
        self.assertEqual(tr, 'jɨsərɨqʰ')

    def test_amahara_m(self):
        tr = self.epi.transliterate('ኣምሓራይ')
        self.assertEqual(tr, 'ʔamħaraj')

    def test_amhara_f(self):
        tr = self.epi.transliterate('ኣምሓራይቲ')
        self.assertEqual(tr, 'ʔamħarajti')

    def test_mountain(self):
        tr = self.epi.transliterate('እምባ')
        self.assertEqual(tr, 'ʔɨmba')

    def test_horses(self):
        tr = self.epi.transliterate('ኣፍራሰ')
        self.assertEqual(tr, 'ʔafrasə')

    def test_ear(self):
        tr = self.epi.transliterate('እዝኒ')
        self.assertEqual(tr, 'ʔɨzni')

    def test_chair(self):
        tr = self.epi.transliterate('መንበር')
        self.assertEqual(tr, 'mənbər')

    def test_elephant(self):
        tr = self.epi.transliterate('ሓርማዝ')
        self.assertEqual(tr, 'ħarmaz')
