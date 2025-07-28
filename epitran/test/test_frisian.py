# -*- coding: utf-8 -*-
# Sources include Wiktionary and Frysk Hânwurdboek

from __future__ import print_function, unicode_literals

import unittest

import epitran


def assemble_ipa(xs):
    return ''.join([x[3] for x in xs])


class TestFrisian(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('fry-Latn')

    def _derivation(self, orth, correct):
        attempt = assemble_ipa(self.epi.word_to_tuples(orth))
        self.assertEqual(attempt, correct)

    def test_wurde(self):
        self._derivation('wurde', 'vødə')

    def test_alden(self):
        self._derivation('âlden', 'ɔːdən')

    def test_wenne(self):
        self._derivation('wenne', 'vɛnə')

    def test_tsjelke(self):
        self._derivation('tsjelke', 'tsjɛlkə')

    def test_skriuwe(self):
        self._derivation('skriuwe', 'skrjoːu̯ə')
