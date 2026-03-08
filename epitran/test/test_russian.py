# -*- coding: utf-8 -*-


import unittest

import epitran


class TestRussian(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'rus-Cyrl')

    def test_straitilstva(self):
        tr = self.epi.transliterate('строительство')
        self.assertEqual(tr, 'stroitʲelʲstvo')

    def test_gasurdarstva(self):
        tr = self.epi.transliterate('государство')
        self.assertEqual(tr, 'ɡosudarstvo')

    def test_vzglat(self):
        tr = self.epi.transliterate('взгляд')
        self.assertEqual(tr, 'vzɡlʲat')

    def test_exceptions(self):
        """Lexical exceptions to general phonetic rules."""
        tr = self.epi.transliterate('сегодня')
        self.assertEqual(tr, 'sʲivodnʲa')
        tr = self.epi.transliterate('бог')
        self.assertEqual(tr, 'box')

    def test_g_softening(self):
        """The letter г is pronounced as /v/ or /x/ in certain regular contexts."""
        pairs = [
            ('легко', 'lʲexko'),
            ("мягкий", 'mʲaxkij'),
            ('легчать', 'lʲext͡ɕʲatʲ'),
            ("чего", 't͡ɕʲevo'),
            ("кого", 'kovo')
        ]
        for orth, phon in pairs:
            tr = self.epi.transliterate(orth)
            self.assertEqual(tr, phon)

    def test_voicing_assimilation(self):
        pairs = [
            ('все', 'fsʲe'),
            ('встретить', 'fstrʲetʲitʲ'),
            ("рассказ", 'raskas'),
            ("сделать", 'zdʲelatʲ'),
            ("просьба", 'prozʲba'),
            ("водка", 'votka'),
        ]
        for orth, phon in pairs:
            tr = self.epi.transliterate(orth)
            self.assertEqual(tr, phon)

    def test_hushers(self):
        pairs = [
            ('жить', 'ʒɨtʲ'),
            ('шить', 'ʂɨtʲ'),
            ("цифра", 't͡sɨfra'),
        ]
        for orth, phon in pairs:
            tr = self.epi.transliterate(orth)
            self.assertEqual(tr, phon)

if __name__ == '__main__':
    unittest.main()