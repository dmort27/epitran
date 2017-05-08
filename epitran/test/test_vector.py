#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import unittest
from epitran import vector


def map_slice(xs, start, end):
    return [x[start:end] for x in xs]


class TestTurkish(unittest.TestCase):
    def setUp(self):
        self.vwis = vector.VectorsWithIPASpace('tur-Latn',
                                               ['tur-Latn'])

    def test_punc(self):
        punc_words = ['"', "'", '.', ',', ':', ';', "‘", "’", "”", "“", "，"]
        for word in punc_words:
            segs = self.vwis.word_to_segs(word)
            self.assertEqual(segs[0][0], 'P')
            self.assertEqual(segs[0][1], 0)
            self.assertIn(segs[0][3], "\"';,.")

    def test_punc_like(self):
        punc_words = ["ʼ"]
        for word in punc_words:
            segs = self.vwis.word_to_segs(word, normpunc=True)
            self.assertEqual(segs[0][0], 'P')

    def test_haziranda(self):
        word = 'Haziranʼda'
        segs = self.vwis.word_to_segs(word, normpunc=True)
        marks = [s[:4] for s in segs]
        correct = [('L', 1, 'H', 'h'),
                   ('L', 0, 'a', 'a'),
                   ('L', 0, 'z', 'z'),
                   ('L', 0, 'i', 'i'),
                   ('L', 0, 'r', 'ɾ'),
                   ('L', 0, 'a', 'a'),
                   ('L', 0, 'n', 'n'),
                   ('P', 0, "'", ''),
                   ('L', 0, 'd', 'd'),
                   ('L', 0, 'a', 'a'), ]
        for m, c in zip(marks, correct):
            self.assertEqual(m, c)

    def test_haziranda_prime(self):
        word = 'Haziranʼda'
        segs = self.vwis.word_to_segs(word, normpunc=True)
        marks = [s[:4] for s in segs]
        correct = [('L', 1, 'H', 'h'),
                   ('L', 0, 'a', 'a'),
                   ('L', 0, 'z', 'z'),
                   ('L', 0, 'i', 'i'),
                   ('L', 0, 'r', 'ɾ'),
                   ('L', 0, 'a', 'a'),
                   ('L', 0, 'n', 'n'),
                   ('P', 0, "'", ''),
                   ('L', 0, 'd', 'd'),
                   ('L', 0, 'a', 'a'), ]
        for m, c in zip(marks, correct):
            self.assertEqual(m, c)

    def test_cat_haziranda(self):
        word = 'Haziranʼda'  # 'Apostrophe' is modifier letter
        segs = self.vwis.word_to_segs(word, normpunc=False)
        cats = [s[0] for s in segs]
        correct = ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']
        self.assertEqual(cats, correct)

    def test_cat_haziranda_normpunc(self):
        word = 'Haziranʼda'  # 'Apostrophe' is modifier letter
        segs = self.vwis.word_to_segs(word, normpunc=True)
        cats = [s[0] for s in segs]
        correct = ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'P', 'L', 'L']
        self.assertEqual(cats, correct)


class TestUzbek(unittest.TestCase):
    def setUp(self):
        self.vwis = vector.VectorsWithIPASpace('uzb-Latn',
                                               ['uzb-Latn'])

    def test_apostrophe_letter(self):
        target = [('L', 0, 'ʼ', 'ʔ')]
        test = self.vwis.word_to_segs("ʼ")
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_apostrophe_letter_normpunc(self):
        target = [('L', 0, 'ʼ', 'ʔ')]
        test = self.vwis.word_to_segs("ʼ", normpunc=True)
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_apostrophe_punc(self):
        target = [('P', 0, "'", '')]
        test = self.vwis.word_to_segs("'")
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_o_turned_comma(self):
        target = [('L', 0, "oʻ", 'o')]
        test = self.vwis.word_to_segs("oʻ")
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_o_turned_comma_normpunc(self):
        target = [('L', 0, "oʻ", 'o')]
        test = self.vwis.word_to_segs("oʻ", normpunc=True)
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_o_turned_comma_full(self):
        target = [('L', 0, 'o\u02bb', 'o', 34, [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, 0, -1, 0, -1, -1, -1, 1, 1, -1, 1, -1])]
        test = self.vwis.word_to_segs("oʻ")
        self.assertEqual(test, target)

    def test_o_turned_comma_full_normpunc(self):
        target = [('L', 0, 'o\u02bb', 'o', 34, [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, 0, -1, 0, -1, -1, -1, 1, 1, -1, 1, -1])]
        test = self.vwis.word_to_segs("oʻ", normpunc=True)
        self.assertEqual(test, target)

    def test_g_turned_comma_full(self):
        target = [('L', 0, 'g\u02bb', '\u0281', 59, [-1, -1, 1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, 0, -1, -1, -1, 1, -1, -1, 0, -1])]
        test = self.vwis.word_to_segs("gʻ")
        self.assertEqual(test, target)

    def test_g_turned_comma_full_normpunc(self):
        target = [('L', 0, 'g\u02bb', '\u0281', 59, [-1, -1, 1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, 0, -1, -1, -1, 1, -1, -1, 0, -1])]
        test = self.vwis.word_to_segs("gʻ", normpunc=True)
        self.assertEqual(test, target)

    def test_ozini1(self):
        target = [('L', 0, 'oʻ', 'o'),
                  ('L', 0, 'z', 'z'),
                  ('L', 0, 'i', 'i'),
                  ('L', 0, 'n', 'n'),
                  ('L', 0, 'i', 'i'),
                  ]
        test = self.vwis.word_to_segs('oʻzini')
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_ozini2(self):
        target = [('L', 0, "o'", 'o'),
                  ('L', 0, 'z', 'z'),
                  ('L', 0, 'i', 'i'),
                  ('L', 0, 'n', 'n'),
                  ('L', 0, 'i', 'i'),
                  ]
        test = self.vwis.word_to_segs("o'zini")
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_word_to_tuples2(self):
        target = [('L', 1, 'B', 'b'),
                  ('L', 0, 'a', 'a'),
                  ('L', 0, 'l', 'l'),
                  ('L', 0, 'o', 'ɒ'),
                  ('L', 0, 'gʻ', 'ʁ'),
                  ('L', 0, 'a', 'a'),
                  ('L', 0, 't', 't̪')]
        test = self.vwis.word_to_segs('Balogʻat')
        self.assertEqual(map_slice(test, 0, 4), target)
