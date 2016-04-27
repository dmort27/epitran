#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import unittest
import vector


class TestTurkish(unittest.TestCase):
    def setUp(self):
        self.vwis = vector.VectorsWithIPASpace('tur-Latn',
                                               'tur-with_attached_suffixes-space')

    def testPunc(self):
        punc_words = [u'"', u"'", u'.', u',', u':', u';', u"‘", u"’", u"”", u"“", u"。", u"，"]
        for word in punc_words:
            print(u'Item:\t{}'.format(word))
            segs = self.vwis.word_to_segs(word)
            self.assertEqual(segs[0][0], u'P')
            self.assertEqual(segs[0][1], 0)
            self.assertIn(segs[0][3], u"\"';,.")

    def testPuncLike(self):
        punc_words = [u"ʼ"]
        for word in punc_words:
            print(u'Item:\t{}'.format(word))
            segs = self.vwis.word_to_segs(word)
            self.assertNotEqual(segs[0][0], u'P')

    def testHaziranda(self):
        word = u'Haziranʼda'
        segs = self.vwis.word_to_segs(word)
        marks = [s[:4] for s in segs]
        correct = [('L', 1, 'H', u'h'),
                   ('L', 0, 'a', u'a'),
                   ('L', 0, 'z', u'z'),
                   ('L', 0, 'i', u'i'),
                   ('L', 0, 'r', u'ɾ'),
                   ('L', 0, 'a', u'a'),
                   ('L', 0, 'n', u'n'),
                   ('P', 0, "'", u''),
                   ('L', 0, 'd', u'd'),
                   ('L', 0, 'a', u'a'), ]
        for m, c in zip(marks, correct):
            self.assertEqual(m, c)

    def testHazirandaPrime(self):
        word = u'Haziranʼda'
        segs = self.vwis.word_to_segs(word)
        marks = [s[:4] for s in segs]
        correct = [('L', 1, 'H', u'h'),
                   ('L', 0, 'a', u'a'),
                   ('L', 0, 'z', u'z'),
                   ('L', 0, 'i', u'i'),
                   ('L', 0, 'r', u'ɾ'),
                   ('L', 0, 'a', u'a'),
                   ('L', 0, 'n', u'n'),
                   ('P', 0, "'", u''),
                   ('L', 0, 'd', u'd'),
                   ('L', 0, 'a', u'a'), ]
        for m, c in zip(marks, correct):
            self.assertEqual(m, c)
