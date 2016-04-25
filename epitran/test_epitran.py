#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import unittest
import _epitran

class TestTurkish(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'tur-Latn')

    def test_transliterate(self):
        pairs = [(u'Haziran\'da', u'haziɾan\'da'),
                 (u'Hazeran’da', u'hazeɾan’da'),
                 (u'otoparkın', u'otopaɾkɯn')]
        for orth, ipa in pairs:
            self.assertEqual(self.epi.transliterate(orth), ipa)


    def test_transliterate_norm_punc(self):
        pairs = [(u'Haziran\'da', u'haziɾan\'da'),
                 (u'Hazeran’da', u'hazeɾan\'da'),
                 (u'otoparkın', u'otopaɾkɯn')]
        for orth, ipa in pairs:
            self.assertEqual(self.epi.transliterate(orth, normpunc=True), ipa)
