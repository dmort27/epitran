# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import unicodedata

import epitran


class TestEstonian(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('est-Latn')

    # RULE 1
    def test_kabi(self): 
        tr = self.epi.transliterate('kabi')
        self.assertEqual(tr, 'kɑpi')

    def test_kapi(self): 
        tr = self.epi.transliterate('kapi')
        self.assertEqual(tr, 'kɑpːi')

    def test_kappi(self): 
        tr = self.epi.transliterate('kappi')
        self.assertEqual(tr, 'kɑpːːi')

    def test_sodin(self): 
        tr = self.epi.transliterate('sodin')
        self.assertEqual(tr, 'sotʲin')

    def test_kota(self): 
        tr = self.epi.transliterate('kota')
        self.assertEqual(tr, 'kotːɑ')

    def test_pered(self): 
        tr = self.epi.transliterate('pered')
        self.assertEqual(tr, 'peret')

    # RULE 2
    def test_kõrbgi(self): 
        tr = self.epi.transliterate('kõrbgi')
        self.assertEqual(tr, 'kørbkːi')
    

    # RULE 3
    def test_häbi(self): 
        tr = self.epi.transliterate('häbi')
        self.assertEqual(tr, 'æpi')

    def test_homme(self): 
        tr = self.epi.transliterate('homme')
        self.assertEqual(tr, 'omːe')


    # RULE 4
    def test_siia(self): 
        tr = self.epi.transliterate('siia')
        self.assertEqual(tr, 'siːja')

    def test_maia(self): 
        tr = self.epi.transliterate('maia')
        self.assertEqual(tr, 'maiːja')

    def test_müüa(self): 
        tr = self.epi.transliterate('müüa')
        self.assertEqual(tr, 'myija')

    def test_jänes(self): 
        tr = self.epi.transliterate('jänes')
        self.assertEqual(tr, 'jænes')
    
    # RULE 5
    def test_vere(self): 
        tr = self.epi.transliterate('vere')
        self.assertEqual(tr, 'vere')
    
    def test_veere(self): 
        tr = self.epi.transliterate('veere')
        self.assertEqual(tr, 'veːre')
    
    def test_lina(self): 
        tr = self.epi.transliterate('lina')
        self.assertEqual(tr, 'linɑ')
    
    def test_linna(self): 
        tr = self.epi.transliterate('lina')
        self.assertEqual(tr, 'linːɑ')


    # RULE 7
    def test_duši(self): 
        tr = self.epi.transliterate('duši')
        self.assertEqual(tr, 'tuʃːi')
    

    def test_käsn(self): 
        tr = self.epi.transliterate('käsn')
        self.assertEqual(tr, 'kæʃːn')

    def test_šahti(self): 
        tr = self.epi.transliterate('šahti')
        self.assertEqual(tr, 'ʃɑhti')

    def test_bluffi(self): 
        tr = self.epi.transliterate('bluffi')
        self.assertEqual(tr, 'plufːːi')

    def test_fakti(self): 
        tr = self.epi.transliterate('fakti')
        self.assertEqual(tr, 'fakːti')

    # RULE 8
    def test_pani(self): 
        tr = self.epi.transliterate('pani')
        self.assertEqual(tr, 'panʲi')

    def test_lasi(self): 
        tr = self.epi.transliterate('lasi')
        self.assertEqual(tr, 'lasʲi')
    
    def test_palju(self): 
        tr = self.epi.transliterate('palju')
        self.assertEqual(tr, 'palʲju')

    def test_paljas(self): 
        tr = self.epi.transliterate('paljas')
        self.assertEqual(tr, 'palʲjas')

    def test_padi(self): 
        tr = self.epi.transliterate('padi')
        self.assertEqual(tr, 'patʲi')
