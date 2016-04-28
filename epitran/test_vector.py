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
                                               'tur-with_attached_suffixes-space')

    def testPunc(self):
        punc_words = [u'"', u"'", u'.', u',', u':', u';', u"‘", u"’", u"”", u"“", u"，"]
        for word in punc_words:
            print(u'Punctuation mark:\t{}'.format(word))
            segs = self.vwis.word_to_segs(word)
            print(segs)
            self.assertEqual(segs[0][0], u'P')
            self.assertEqual(segs[0][1], 0)
            self.assertIn(segs[0][3], u"\"';,.")

    def testPuncLike(self):
        punc_words = [u"ʼ"]
        for word in punc_words:
            segs = self.vwis.word_to_segs(word)
            self.assertEqual(segs[0][0], u'P')

    def testHaziranda(self):
        word = u'Haziranʼda'
        segs = self.vwis.word_to_segs(word)
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

    def testHazirandaPrime(self):
        word = u'Haziranʼda'
        segs = self.vwis.word_to_segs(word)
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

class TestUzbek(unittest.TestCase):
    def setUp(self):
        self.vwis = vector.VectorsWithIPASpace('tur-Latn',
                                               'tur-with_attached_suffixes-space')

    def test_apostrophe_letter(self):
        target = [(u'L', 0, u"'", u'')]
        test = self.vwis.word_to_segs(u"ʼ")
        print(test)
        self.assertEqual(map_slice(test, 0, 4), target)

    def test_apostrophe_punc(self):
        target = [(u'P', 0, u"'", u'')]
        test = self.vwis.word_to_segs(u"'")
        print(test)
        self.assertEqual(map_slice(test, 0, 4), target)
