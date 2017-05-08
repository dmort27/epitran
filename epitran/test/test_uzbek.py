# -*- coding: utf-8 -*-
from __future__ import print_function

import logging
import unittest

import epitran

logging.basicConfig(level=logging.ERROR)


def assemble_ipa(xs):
    return ''.join([x[3] for x in xs])


def map_slice(xs, start, end):
    return [x[start:end] for x in xs]


class TestUzbek(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'uzb-Latn')

    def _derivation(self, orth, correct):
        attempt = assemble_ipa(self.epi.word_to_tuples(orth))
        self.assertEqual(attempt, correct)

    def test_uppercase_e_diaeresis(self):
        self._derivation(u'Ë', u'ja')

    def test_ozini1(self):
        # MODIFIER LETTER TURNED COMMA
        target = [(u'L', 0, u'oʻ', u'o'),
                  (u'L', 0, u'z', u'z'),
                  (u'L', 0, u'i', u'i'),
                  (u'L', 0, u'n', u'n'),
                  (u'L', 0, u'i', u'i')
                  ]
        test = self.epi.word_to_tuples(u'oʻzini')
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_ozini2(self):
        target = [(u'L', 0, u"o'", u'o'),
                  (u'L', 0, u'z', u'z'),
                  (u'L', 0, u'i', u'i'),
                  (u'L', 0, u'n', u'n'),
                  (u'L', 0, u'i', u'i'),
                  ]
        test = self.epi.word_to_tuples(u"o'zini", normpunc=True)
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_word_to_tuples2(self):
        target = [(u'L', 1, u'B', u'b'),
                  (u'L', 0, u'a', u'a'),
                  (u'L', 0, u'l', u'l'),
                  (u'L', 0, u'o', u'ɒ'),
                  (u'L', 0, u'gʻ', u'ʁ'),
                  (u'L', 0, u'a', u'a'),
                  (u'L', 0, u't', u't̪')]
        test = self.epi.word_to_tuples(u'Balogʻat')
        self.assertEqual(map_slice(test, 0, 4), target)
