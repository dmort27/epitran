# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestYue2(unittest.TestCase):
    def setUp(self):
        # Requires downloading CC-Canto, which slows down the test suite a lot.
        self.epi = epitran.Epitran('yue-Hant', tones=True)

        # wikipedia derived test cases 
        self.tester_exs = [
            ('心','sɐm˥'),
            ('手','sɐw˨˥'),
            ('一','jɐt̚˥'),
            ('有','jɐw˨'),
            ('猪','tsy˥'),
            ('话','wa˨˥'),
            ('人','jɐn˨˩'),
            ('鋸','kœ˥'),
            ('天','tʰin˥'),
            ('好','hɔw˧'),
            ('都','tɔw˥'),
            ('媽','ma˨˧'),
        ]

    def test(self):
        for ex in self.tester_exs: 
            jyuping, ipa = ex
            pred = self.epi.transliterate(jyuping)
            self.assertEqual(pred, ipa)
