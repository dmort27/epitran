#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import unittest
import vector


def map_slice(xs, start, end):
    return [x[start:end] for x in xs]


class TestTurkish(unittest.TestCase):
    def setUp(self):
        self.vwis = vector.VectorsWithIPASpace('tur-Latn',
                                               'tur-Latn')

    def test_punc(self):
        punc_words = [u'"', u"'", u'.', u',', u':', u';', u"‘", u"’", u"”", u"“", u"，"]
        for word in punc_words:
            segs = self.vwis.word_to_segs(word)
            self.assertEqual(segs[0][0], u'P')
            self.assertEqual(segs[0][1], 0)
            self.assertIn(segs[0][3], u"\"';,.")

    def test_punc_like(self):
        punc_words = [u"ʼ"]
        for word in punc_words:
            segs = self.vwis.word_to_segs(word, normpunc=True)
            self.assertEqual(segs[0][0], u'P')

    def test_haziranda(self):
        word = u'Haziranʼda'
        segs = self.vwis.word_to_segs(word, normpunc=True)
        marks = [s[:4] for s in segs]
        correct = [(u'L', 1, u'H', u'h'),
                   (u'L', 0, u'a', u'a'),
                   (u'L', 0, u'z', u'z'),
                   (u'L', 0, u'i', u'i'),
                   (u'L', 0, u'r', u'ɾ'),
                   (u'L', 0, u'a', u'a'),
                   (u'L', 0, u'n', u'n'),
                   (u'P', 0, u"'", u''),
                   (u'L', 0, u'd', u'd'),
                   (u'L', 0, u'a', u'a'), ]
        for m, c in zip(marks, correct):
            self.assertEqual(m, c)

    def test_haziranda_prime(self):
        word = u'Haziranʼda'
        segs = self.vwis.word_to_segs(word, normpunc=True)
        marks = [s[:4] for s in segs]
        correct = [(u'L', 1, u'H', u'h'),
                   (u'L', 0, u'a', u'a'),
                   (u'L', 0, u'z', u'z'),
                   (u'L', 0, u'i', u'i'),
                   (u'L', 0, u'r', u'ɾ'),
                   (u'L', 0, u'a', u'a'),
                   (u'L', 0, u'n', u'n'),
                   (u'P', 0, u"'", u''),
                   (u'L', 0, u'd', u'd'),
                   (u'L', 0, u'a', u'a'), ]
        for m, c in zip(marks, correct):
            self.assertEqual(m, c)

    def test_cat_haziranda(self):
        word = u'Haziranʼda'  # 'Apostrophe' is modifier letter
        segs = self.vwis.word_to_segs(word, normpunc=False)
        cats = [s[0] for s in segs]
        correct = [u'L', u'L', u'L', u'L', u'L', u'L', u'L', u'L', u'L', u'L']
        self.assertEqual(cats, correct)

    def test_cat_haziranda_normpunc(self):
        word = u'Haziranʼda'  # 'Apostrophe' is modifier letter
        segs = self.vwis.word_to_segs(word, normpunc=True)
        cats = [s[0] for s in segs]
        correct = [u'L', u'L', u'L', u'L', u'L', u'L', u'L', u'P', u'L', u'L']
        self.assertEqual(cats, correct)


class TestUzbek(unittest.TestCase):
    def setUp(self):
        self.vwis = vector.VectorsWithIPASpace('uzb-Latn',
                                               'uzb-Latn')

    def test_apostrophe_letter(self):
        target = [(u'L', 0, u'ʼ', u'ʔ')]
        test = self.vwis.word_to_segs(u"ʼ")
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_apostrophe_letter_normpunc(self):
        target = [(u'L', 0, u'ʼ', u'ʔ')]
        test = self.vwis.word_to_segs(u"ʼ", normpunc=True)
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_apostrophe_punc(self):
        target = [(u'P', 0, u"'", u'')]
        test = self.vwis.word_to_segs(u"'")
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_o_turned_comma(self):
        target = [(u'L', 0, u"oʻ", u'o')]
        test = self.vwis.word_to_segs(u"oʻ")
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_o_turned_comma_normpunc(self):
        target = [(u'L', 0, u"oʻ", u'o')]
        test = self.vwis.word_to_segs(u"oʻ", normpunc=True)
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_o_turned_comma_full(self):
        target = [(u'L', 0, u'o\u02bb', u'o', 51, [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, 0, -1, 0, -1, -1, -1, 1, 1, 1, -1])]
        test = self.vwis.word_to_segs(u"oʻ")
        self.assertEqual(test, target)

    def test_o_turned_comma_full_normpunc(self):
        target = [(u'L', 0, u'o\u02bb', u'o', 51, [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, 0, -1, 0, -1, -1, -1, 1, 1, 1, -1])]
        test = self.vwis.word_to_segs(u"oʻ", normpunc=True)
        self.assertEqual(test, target)

    def test_g_turned_comma_full(self):
        target = [(u'L', 0, u'g\u02bb', u'\u0281', 87, [-1, -1, 1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, 0, -1, -1, -1, 1, -1, 0, -1])]
        test = self.vwis.word_to_segs(u"gʻ")
        self.assertEqual(test, target)

    def test_g_turned_comma_full_normpunc(self):
        target = [(u'L', 0, u'g\u02bb', u'\u0281', 87, [-1, -1, 1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, 0, -1, -1, -1, 1, -1, 0, -1])]
        test = self.vwis.word_to_segs(u"gʻ", normpunc=True)
        self.assertEqual(test, target)

    def test_ozini1(self):
        target = [(u'L', 0, u'oʻ', u'o'),
                  (u'L', 0, u'z', u'z'),
                  (u'L', 0, u'i', u'i'),
                  (u'L', 0, u'n', u'n'),
                  (u'L', 0, u'i', u'i'),
                  ]
        test = self.vwis.word_to_segs(u'oʻzini')
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_ozini2(self):
        target = [(u'L', 0, u"o'", u'o'),
                  (u'L', 0, u'z', u'z'),
                  (u'L', 0, u'i', u'i'),
                  (u'L', 0, u'n', u'n'),
                  (u'L', 0, u'i', u'i'),
                  ]
        test = self.vwis.word_to_segs(u"o'zini")
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_word_to_tuples2(self):
        target = [(u'L', 1, u'B', u'b'),
                  (u'L', 0, u'a', u'a'),
                  (u'L', 0, u'l', u'l'),
                  (u'L', 0, u'o', u'ɒ'),
                  (u'L', 0, u'gʻ', u'ʁ'),
                  (u'L', 0, u'a', u'a'),
                  (u'L', 0, u't', u't̪')]
        test = self.vwis.word_to_segs(u'Balogʻat')
        self.assertEqual(map_slice(test, 0, 4), target)
