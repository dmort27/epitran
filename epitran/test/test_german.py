#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import logging
import unittest

import epitran

logging.basicConfig(level=logging.ERROR)


def assemble_ipa(xs):
    return ''.join([x[3] for x in xs])


class TestGerman(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('deu-Latn')

    def _derivation(self, orth, correct):
        attempt = self.epi.transliterate(orth)
        self.assertEqual(attempt, correct)

    def test_wasser(self):
        self._derivation('wasser', 'vasər')

    def test_geben(self):
        self._derivation('ɡeben', 'ɡeːbən')

    def test_scheisse(self):
        self._derivation('scheiẞe', 'ʃajsə')

    def test_nietzsche(self):
        self._derivation('Nietzsche', 'niːt͡ʃə')

    def test_immer(self):
        self._derivation('immer', 'imər')

    def test_ahre(self):
        self._derivation('Ähre', 'eːrə')

    def test_abdanken(self):
        self._derivation('abdanken', 'apdaŋkən')

    def test_rotgelb(self):
        self._derivation('rotɡelb', 'rotɡelp')


class TestGermanNP(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('deu-Latn-np')

    def _derivation(self, orth, correct):
        attempt = self.epi.transliterate(orth)
        self.assertEqual(attempt, correct)

    def test_wasser(self):
        self._derivation('wasser', 'vasər')

    def test_ahre(self):
        self._derivation('Ähre', 'eːrə')

    def test_abdanken(self):
        self._derivation('abdanken', 'abdaŋkən')

    def test_rotgelb(self):
        self._derivation('rotɡelb', 'rotɡelb')
