# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import epitran

class TestOccitan(unittest.TestCase):
  def setUp(self):
    self.epi = epitran.Epitran("oci-Latn")

    def test_abadia(self):
      # test intervocalic g, word-final r
      res = self.epi.transliterate("bolegar")
      self.assertEqual(res, "buleɣa")

    def test_amiga(self):
        # test intervocalic g
        res = self.epi.transliterate("amiga")
        assert res == "amiɣa"

    
    def test_diccionari(self):
        # test cc, interovcalic r, diphtong io
        res = self.epi.transliterate("diccionari")
        assert res == "dit͡sjunaɾi"

    def test_lengatge(self):
        # test n before special consonant, tg mapping
        res = self.epi.transliterate("lengatge")
        assert res == "leŋgad͡ʒe"

    
    def test_crompar(self):
        # test word-intial c
        res = self.epi.transliterate("crompar")
        assert res == "kɾumpa"

    
    def test_cinc(self):
        # test word c before i/e, n before c
        res = self.epi.transliterate("cinc")
        assert res == "siŋk"

    
    def test_nevar(self): 
       # test intervocalic v, word-final r
        res = self.epi.transliterate("nevar")
        assert res == "neβa"    
