#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import unittest

import epitran

logger = logging.getLogger('epitran')


def map_slice(xs, start, end):
    return [x[start:end] for x in xs]


def assemble_ipa(xs):
    return ''.join([x[3] for x in xs])


class TestFrench(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('fra-Latn')

    def _derivation(self, orth, correct):
        logger.debug(orth.encode('utf-8'))
        attempt = self.epi.transliterate(orth)
        logger.debug('{} ?= {}'.format(attempt, correct).encode('utf-8'))
        self.assertEqual(attempt, correct)

    def test_suggerer(self):
        self._derivation('suggérer', 'syɡʒeʀe')

    def test_garcon(self):
        self._derivation('garçon', 'ɡaʀsɔ̃')

    def test_deux(self):
        self._derivation('deux', 'dœ')

    def test_coup(self):
        self._derivation('coup', 'ku')

    def test_oui(self):
        self._derivation('oui', 'wi')

    def test_xylophone(self):
        self._derivation('xylophone', 'ɡzilɔfɔn')

    def test_expansion(self):
        self._derivation('expansion', 'ɛkspɑ̃sjɔ̃')

    def test_saint(self):
        self._derivation('saint', 'sɛ̃')

    def test_seing(self):
        self._derivation('seing', 'sɛ̃')

    def test_ceins(self):
        self._derivation('ceins', 'sɛ̃')

    def test_il_ils(self):
        self._derivation('il', 'il')
        self._derivation('ils', 'il')

    def test_fusil(self):
        self._derivation('fusil', 'fyzi')
        self._derivation('fusils', 'fyzi')

    def test_oef(self):
        self._derivation('œuf', 'œf')
        self._derivation('œufs', 'œf')

    def test_decret(self):
        self._derivation('décret', 'dekʀɛ')
        self._derivation('décrets', 'dekʀɛ')

    def test_loi(self):
        self._derivation('loi', 'lwa')
        self._derivation('lois', 'lwa')

    def test_dame(self):
        self._derivation('dame', 'dam')
        self._derivation('dames', 'dam')

    def test_faite(self):
        self._derivation('fait', 'fɛ')
        self._derivation('faits', 'fɛ')
        self._derivation('faites', 'fɛt')

    def test_homme(self):
        self._derivation('homme', 'ɔm')
        self._derivation('hommes', 'ɔm')

    def test_personne(self):
        self._derivation('personne', 'pɛʀsɔn')
        self._derivation('personnes', 'pɛʀsɔn')
