#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import logging
import unittest

import epitran

logging.basicConfig(level=logging.ERROR)


def assemble_ipa(xs):
    return ''.join([x[3] for x in xs])


class TestGermanDuden(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('deu-Latn')

    def _derivation(self, orth, correct):
        attempt = self.epi.transliterate(orth)
        self.assertEqual(attempt, correct)

    def test_spiess(self):
        self._derivation('Spieß', 'ʃpiːs')

    def test_tur(self):
        self._derivation('Tür', 'tyːʀ')

    def test_weg(self):
        self._derivation('Weg', 'veːk')

    def test_schon(self):
        self._derivation('Schön', 'ʃøːn')

    def test_gabe(self):
        self._derivation('gäbe', 'ɡæːbə')

    def test_pfad(self):
        self._derivation('Pfad', 'p͡fɑːt')

    def test_schrot(self):
        self._derivation('Schrot', 'ʃʀoːt')

    def test_hut(self):
        self._derivation('Hut', 'huːt')

    def test_splint(self):
        self._derivation('Splint', 'ʃplɪnt')

    def test_gerust(self):
        self._derivation('Gerüst', 'ɡəʀʏst')

    def test_welt(self):
        self._derivation('Welt', 'vɛlt')

    def test_gonnen(self):
        self._derivation('gönnen', 'gœnən')

    def test_kalt(self):
        self._derivation('kalt', 'kalt')

    def test_frost(self):
        self._derivation('Frost', 'fʀɔst')

    def test_kunst(self):
        self._derivation('Kunst', 'kʊnst')


class TestGerman(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('deu-Latn')

    def _derivation(self, orth, correct):
        attempt = self.epi.transliterate(orth)
        self.assertEqual(attempt, correct)

    def test_wasser(self):
        self._derivation('wasser', 'vasɐ')

    def test_geben(self):
        self._derivation('ɡeben', 'ɡeːbən')

    def test_scheisse(self):
        self._derivation('scheiẞe', 'ʃaisə')

    def test_nietzsche(self):
        self._derivation('Nietzsche', 'niːt͡ʃə')

    def test_immer(self):
        self._derivation('immer', 'imə')

    def test_ahre(self):
        self._derivation('Ähre', 'eːʀɐ')

    def test_abdanken(self):
        self._derivation('abdanken', 'apdaŋkən')

    def test_rotgelb(self):
        self._derivation('rotɡelb', 'ʀɔtɡelp')

    def test_haar(self):
        self._derivation('Haar', 'haːɐ')

    def test_trinken(self):
        self._derivation('trinken', 'tʀiŋkən')

    def test_horen(self):
        self._derivation('hören', 'høːrən')

    def test_wehr(self):
        self._derivation('Wehr', 'veːɐ')

    def test_futur(self):
        self._derivation('futur', 'fuːtuɐ')

    def test_kurs(self):
        self._derivation('Kurs', 'kʊɐs')

    def test_markt(self):
        self._derivation('Markt', 'maɐkt')


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


class TestGermanNarrow(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('deu-Latn-nar')

    def _derivation(self, orth, correct):
        attempt = self.epi.transliterate(orth)
        self.assertEqual(attempt, correct)

    def test_wasser(self):
        self._derivation('wasser', 'vasɐ')

    def test_geben(self):
        self._derivation('ɡeben', 'ɡeːbən')

    def test_nietzsche(self):
        self._derivation('Nietzsche', 'niːt͡ʃə')

    def test_immer(self):
        self._derivation('immer', 'imɐ')

    def test_ahre(self):
        self._derivation('Ähre', 'eːʀə')

    def test_abdanken(self):
        self._derivation('abdanken', 'apdaŋkən')

    def test_rotgelb(self):
        self._derivation('rotɡelb', 'ʁotɡelp')

    def test_haar(self):
        self._derivation('Haar', 'haːɐ')

    def test_trinken(self):
        self._derivation('trinken', 'tʁiŋkən')

    def test_horen(self):
        self._derivation('hören', 'høːʀən')

    def test_wehr(self):
        self._derivation('Wehr', 'veːɐ')

    def test_futur(self):
        self._derivation('futur', 'fuːtuɐ')

    def test_kurs(self):
        self._derivation('Kurs', 'kuɐs')

    def test_markt(self):
        self._derivation('Markt', 'maɐkt')
