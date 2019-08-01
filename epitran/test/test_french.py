#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import logging
import unittest

import epitran

logging.basicConfig(level=logging.ERROR)


def map_slice(xs, start, end):
    return [x[start:end] for x in xs]


def assemble_ipa(xs):
    return ''.join([x[3] for x in xs])


class TestFrench(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('fra-Latn')

    def _derivation(self, orth, correct):
        logging.debug(orth.encode('utf-8'))
        attempt = self.epi.transliterate(orth)
        logging.debug('{} ?= {}'.format(attempt, correct).encode('utf-8'))
        self.assertEqual(attempt, correct)

    def test_suggerer(self):
        self._derivation('suggérer', 'syɡʒere')

    def test_garcon(self):
        self._derivation('garçon', 'ɡarsɔ̃')

    def test_deux(self):
        self._derivation('deux', 'dœ')

    def test_coup(self):
        self._derivation('coup', 'ku')

    def test_oui(self):
        self._derivation('oui', 'wi')

    def test_xylophone(self):
        self._derivation('xylophone', 'ksilɔfɔn')

    def test_expansion(self):
        self._derivation('expansion', 'ɛkspɑ̃sjɔ̃')

    def test_saint(self):
        self._derivation('saint', 'sɛn')

    def test_seing(self):
        self._derivation('seing', 'sɛn')

    def test_ceins(self):
        self._derivation('ceins', 'sɛn')

    def test_il_ils(self):
        self._derivation('il', 'il')
        self._derivation('ils', 'il')

    def test_fusil(self):
        self._derivation('fusil', 'fyzil')
        self._derivation('fusils', 'fyzil')

    def test_oef(self):
        self._derivation('œuf', 'œf')
        self._derivation('œufs', 'œf')

    def test_decret(self):
        self._derivation('décret', 'dekrɛ')
        self._derivation('décrets', 'dekrɛ')

    def test_loi(self):
        self._derivation('loi', 'lwa')
        self._derivation('lois', 'lwa')

    def test_dame(self):
        self._derivation('dame', 'dam')
        self._derivation('dames', 'dam')

    def test_garage(self):
        self._derivation('garage', 'ɡaraʒ')
        self._derivation('garages', 'ɡaraʒ')

    def test_faite(self):
        self._derivation('fait', 'fɛ')
        self._derivation('faits', 'fɛ')
        self._derivation('faites', 'fɛt')

    def test_homme(self):
        self._derivation('homme', 'ɔm')
        self._derivation('hommes', 'ɔm')

    def test_personne(self):
        self._derivation('personne', 'pɛrsɔn')
        self._derivation('personnes', 'pɛrsɔn')
