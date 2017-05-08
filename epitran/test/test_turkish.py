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


class TestTurkish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'tur-Latn')

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
