# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import unittest

import epitran


def assemble_ipa(xs):
    return ''.join([x[3] for x in xs])


class TestSpanish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'spa-Latn')

    def _derivation(self, orth, correct):
        attempt = assemble_ipa(self.epi.word_to_tuples(orth))
        self.assertEqual(attempt, correct)

    def test_queso(self):
        self._derivation(u'queso', u'keso')

    def test_general(self):
        self._derivation(u'general', u'xeneɾal')

    def test_cuestion(self):
        self._derivation(u'cuestión', u'kwestjon')

    def test_sabado(self):
        self._derivation(u'sábado', u'sabado')
