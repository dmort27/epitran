# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import epitran

class TestAfrikaans(unittest.TestCase):
  def setUp(self):
    self.epi = epitran.Epitran("afr-Latn")
    
    def test_(self):
      res = self.epi.transliterate("kind")
      self.assertEqual(res, "kint")
    
    def test_(self):
      res = self.epi.transliterate("tjap")
      self.assertEqual(res, "tʃap")

    def test_(self):
      res = self.epi.transliterate("berge")
      self.assertEqual(res, "berge")  

    def test_(self):
      res = self.epi.transliterate("kwaad")
      self.assertEqual(res, "kwɑːt")
    
    def test_(self):
      res = self.epi.transliterate("dink")
      self.assertEqual(res, "diŋk")

    def test_(self):
      res = self.epi.transliterate("kus")
      self.assertEqual(res, "kɵs")

    def test_(self):
      res = self.epi.transliterate("gat")
      self.assertEqual(res, "χat")
    