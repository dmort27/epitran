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
        punc_words = [u'"', u"'", u'.', u',', u':', u';', u"‘", u"’", u"ʼ", u"”", u"“", u"。", u"，"]
        for word in punc_words:
            print('Item:\t{}'.format(word))
            segs = self.vwis.word_to_segs(word)
            self.assertEqual(segs[0][0], u'P')
            self.assertEqual(segs[0][1], 0)
            self.assertIn(segs[0][3], u"\"';,.")
