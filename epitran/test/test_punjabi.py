# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestPunjabi(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'pan-Guru')

    def test_lahore(self):
        tr = self.epi.transliterate('ਲਹੌਰ')
        self.assertEqual(tr, 'ləɦɔɾ')

    def test_pakistani(self):
        tr = self.epi.transliterate('ਪਾਕਿਸਤਾਨੀ')
        self.assertEqual(tr, 'pɑkɪst̪ɑni')

    def test_panjab(self):
        tr = self.epi.transliterate('ਪੰਜਾਬ')
        self.assertEqual(tr, 'pə̃d͡ʒɑb')

    def test_rajdani(self):
        tr = self.epi.transliterate('ਰਾਜਧਾਨੀ')
        self.assertEqual(tr, 'ɾɑd͡ʒt̪ɑni')

    def test_lok(self):
        tr = self.epi.transliterate('ਲੋਕ')
        self.assertEqual(tr, 'lok')

    def test_ginti(self):
        tr = self.epi.transliterate('ਗਿਣਤੀ')
        self.assertEqual(tr, 'ɡɪɳt̪i')

    def test_nal(self):
        tr = self.epi.transliterate('ਨਾਲ')
        self.assertEqual(tr, 'nɑl')

    def test_praband(self):
        tr = self.epi.transliterate('ਪ੍ਰਬੰਧ')
        self.assertEqual(tr, 'pɾəbə̃t̪')
