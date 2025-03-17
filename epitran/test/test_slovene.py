# -*- coding: utf-8 -*-
# Examples from the Handbook of the International Phonetic Association (Slovene)

from __future__ import unicode_literals

import unittest

import epitran


class TestSlovene(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran("slv-Latn")

    @staticmethod
    def _preprocess(gt):
        # Vowel length, however, can no longer be regarded as distinctive for most speakers, and it is generally accepted that long vowels occur in stressed, and short vowels in unstressed position.
        # Stress placement is not predictable but is also rarely distinctive in Slovene, although in a few instances different forms of the same noun or verb differ only in stress placement.
        gt = gt.replace("ː", "")

        # In most cases, unstressed vowels are nowadays written as /e, o/ before the stress and as /ɛ, ɔ/ after the stress; however, an older way of writing them as /ɛ, ɔ/ everywhere is still very common (e.g. in Toporišič 2001).
        gt = gt.replace("e", "ɛ").replace("o", "ɔ")
        return gt

    def _test_boilerplate(self, testcases):    
        for i, gt in testcases:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, self._preprocess(gt))

    def test_consonants(self):
        self._test_boilerplate([
            ("piti", "piːti"),
            ("biti", "biːti"),
            ("tisk", "tiːsk"),
            ("disk", "diːsk"),
            ("tsin", "tsiːn"),
            ("kip", "kiːp"),
            ("gib", "ɡiːp"),
            ("čin", "tʃiːn"),
            # ("gin", "dʒiːn"),
            ("miti", "miːti"),
            ("fin", "fiːn"),
            ("vidiš", "ʋiːdiʃ"),
            ("niti", "niːti"),
            ("siniti", "siːniti"),
            ("ziniti", "ziːniti"),
            ("riti", "ɾiːti"),
            ("liti", "liːti"),
            ("šila", "ʃiːla"),
            ("žila", "ʒiːla"),
            ("hiti", "xiːti"),
            ("jidiš", "jiːdiʃ"),
        ])

    def test_devoicing(self):
        self._test_boilerplate([
            ("slad", "slːat"),
            ("sladkor", "slaːtkɔɾ"),
        ])

    def test_postalveolar_assm(self):
        self._test_boilerplate([
            ("sčasoma", "ʃtʃaːsɔma"),
            ("izžepa", "iʒɛːpa"),
        ])

    def test_vowels(self):
        self._test_boilerplate([
            ("mit", "miːt"),
            ("med", "meːt"),
            ("peta", "pɛːta"),
            ("mat", "maːt"),
            ("pot", "poːt"),
            ("pust", "puːst"),
            ("miti", "miːti"),
            ("pete", "pɛːtɛ"),
            ("mata", "maːta"),
            ("potem", "pɔːtɛm"),
            ("pustu", "puːstu"),
        ])

    def test_transcription(self):
        self._test_boilerplate([
            ("in", "in"),
            ("sonce", "soːntsɛ"),
            ("sta", "sta"),
            ("se", "sɛ"),
            ("prepirala", "pɾɛpiːɾala"),
            ("kateri", "katɛːɾi"),
            ("njiju", "njiːju"),
            ("je", "jɛ"),
        ])

if __name__ == '__main__':
    unittest.main()
