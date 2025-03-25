#!/usr/bin/env Python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import unittest
import epitran
from epitran import flite


class TestFlite(unittest.TestCase):
    def setUp(self):
        self.flite = epitran.Epitran('eng-Latn')

    def test_san_leandro(self):
        self.assertEqual(self.flite.transliterate('San Leandro'), 'sæn liɑndɹow')

    def test_parowan(self):
        self.assertEqual(self.flite.transliterate('Parowan'), 'pɛɹ̩awən')


class TestLexLookup(unittest.TestCase):
    def setUp(self):
        self.flite = flite.FliteLexLookup()

    def test_san_leandro(self):
        self.assertEqual(self.flite.transliterate('San Leandro'), 'sæn liɑndɹow')

    def test_parowan(self):
        self.assertEqual(self.flite.transliterate('Parowan'), 'pɛɹ̩awən')

    def test_brzezinski(self):
        self.assertEqual(self.flite.transliterate('Brzezinski'), 'bɹɪzɪnski')
