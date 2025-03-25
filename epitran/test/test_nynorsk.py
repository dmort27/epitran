# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestNynorsk(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('nno-Latn')
    
    def test_bok(self):
        tr = self.epi.transliterate('bok')
        self.assertEqual(tr, 'buːk')
    
    def test_du(self):
        tr = self.epi.transliterate('du')
        self.assertEqual(tr, 'dʉː')
    
    def test_breidd(self):
        tr = self.epi.transliterate('breidd')
        self.assertEqual(tr, 'brɛɪdː')
    
    def test_rydja(self):
        tr = self.epi.transliterate('rydja')
        self.assertEqual(tr, 'ryːjɑ')
    
    def test_fot(self):
        tr = self.epi.transliterate('fot')
        self.assertEqual(tr, 'fuːt')
        
    def test_flatt(self):
        tr = self.epi.transliterate('flått')
        self.assertEqual(tr, 'flot')
    
    def test_kyrkja(self):
        tr = self.epi.transliterate('kyrkja')
        self.assertEqual(tr, 'çyrçɑ')
    
    def test_kjapp(self):
        tr = self.epi.transliterate('kjapp')
        self.assertEqual(tr, 'çɑp')
    
    def test_land(self):
        tr = self.epi.transliterate('land')
        self.assertEqual(tr, 'lɑnd')
        
    def test_skodd(self):
        tr = self.epi.transliterate('skodd')
        self.assertEqual(tr, 'skudː')
        
    def test_bergmann(self):
        tr = self.epi.transliterate('bergmann')
        self.assertEqual(tr, 'bærgmɑn')
        
    def test_hage(self):
        tr = self.epi.transliterate('hage')
        self.assertEqual(tr, 'hɑːgɛ')
    
    def test_nes(self):
        tr = self.epi.transliterate('nes')
        self.assertEqual(tr, 'nɛːs')
    
    def test_stengja(self):
        tr = self.epi.transliterate('stengja')
        self.assertEqual(tr, 'stɛɲʝɑ')
        
    def test_gapa(self):
        tr = self.epi.transliterate('gapa')
        self.assertEqual(tr, 'gɑːpɑ')
    
    def test_sol(self):
        tr = self.epi.transliterate('sol')
        self.assertEqual(tr, 'suːl')
    
    def test_sju(self):
        tr = self.epi.transliterate('sju')
        self.assertEqual(tr, 'ʃʉː')
    
    def test_ski(self):
        tr = self.epi.transliterate('ski')
        self.assertEqual(tr, 'ʃiː')
    
    def test_tal(self):
        tr = self.epi.transliterate('tal')
        self.assertEqual(tr, 'tɑːl')
    
    def test_vat(self):
        tr = self.epi.transliterate('våt')
        self.assertEqual(tr, 'voːt')