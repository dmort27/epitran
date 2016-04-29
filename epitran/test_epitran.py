#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import unicodedata
import unittest

import _epitran


def map_slice(xs, start, end):
    return [x[start:end] for x in xs]


class TestNormalizePunc(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'tur-Latn')

    def test_modifier_letter_apostrophe(self):
        self.assertEqual(self.epi.normalize_punc(u'\u02bc'), "'")

    def test_left_apostrophe(self):
        self.assertEqual(self.epi.normalize_punc(u'\u2018'), "'")

    def test_right_apostrophe(self):
        self.assertEqual(self.epi.normalize_punc(u'\u2019'), "'")

    def test_modifier_letter_turned_comma(self):
        self.assertEqual(self.epi.normalize_punc(u'\u02bb'), "'")


class TestTurkish(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'tur-Latn')

    def test_transliterate1(self):
        self.assertEqual(self.epi.transliterate(u'Haziran\'da'), u'haziɾan\'da')
        self.assertEqual(self.epi.transliterate(u'Hazeran’da'), u'hazeɾan’da')
        self.assertEqual(self.epi.transliterate(u'otoparkın'), u'otopaɾkɯn')

    def test_transliterate2(self):
        self.assertEqual(self.epi.transliterate(u'"'), u'"')
        self.assertEqual(self.epi.transliterate(u'\''), u'\'')
        self.assertEqual(self.epi.transliterate(u'’'), u'’')
        self.assertEqual(self.epi.transliterate(u'‘'), u'‘')

    def test_transliterate_norm_punc1(self):
        self.assertEqual(self.epi.transliterate(u'Haziran\'da', normpunc=True), u'haziɾan\'da')
        self.assertEqual(self.epi.transliterate(u'Hazeran’da', normpunc=True), u'hazeɾan\'da')
        self.assertEqual(self.epi.transliterate(u'otoparkın', normpunc=True), u'otopaɾkɯn')

    def test_transliterate_norm_punc2(self):
        self.assertEqual(self.epi.transliterate(u'"', normpunc=True), u'"')
        self.assertEqual(self.epi.transliterate(u'\'', normpunc=True), u'\'')
        self.assertEqual(self.epi.transliterate(u'’', normpunc=True), u'\'')
        self.assertEqual(self.epi.transliterate(u'‘', normpunc=True), u'\'')

    def test_word_to_tuples1(self):
        target = [(u'L', 1, u'H', u'h'),
                  (u'L', 0, u'a', u'a'),
                  (u'L', 0, u'z', u'z'),
                  (u'L', 0, u'i', u'i'),
                  (u'L', 0, u'r', u'ɾ'),
                  (u'L', 0, u'a', u'a'),
                  (u'L', 0, u'n', u'n'),
                  (u'L', 0, u'ʼ', u''),
                  (u'L', 0, u'd', u'd'),
                  (u'L', 0, u'a', u'a')]
        word = u'Haziranʼda'
        test = map_slice(self.epi.word_to_tuples(word), 0, 4)
        self.assertEqual(test, target)

    def test_word_to_tuples2(self):
        target = [(u'L', 1, u'H', u'h'),
                  (u'L', 0, u'a', u'a'),
                  (u'L', 0, u'z', u'z'),
                  (u'L', 0, u'i', u'i'),
                  (u'L', 0, u'r', u'ɾ'),
                  (u'L', 0, u'a', u'a'),
                  (u'L', 0, u'n', u'n'),
                  (u'P', 0, u"'", u''),
                  (u'L', 0, u'd', u'd'),
                  (u'L', 0, u'a', u'a')]
        word = u'Haziranʼda'
        test = map_slice(self.epi.word_to_tuples(word, normpunc=True), 0, 4)
        self.assertEqual(test, target)


class TestUzbek(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'uzb-Latn')

    def test_e_diaresis1(self):
        char = unicodedata.normalize('NFD', u'ë')
        target = [(u'L', 0, char, u'ja')]
        test = self.epi.word_to_tuples(u'ë')
        self.assertEqual([x[:4] for x in test], target)

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
