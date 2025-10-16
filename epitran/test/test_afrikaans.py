# -*- coding: utf-8 -*-

import unittest
import epitran

class TestAfrikaans(unittest.TestCase):
  def setUp(self):
    self.epi = epitran.Epitran("afr-Latn")
    
    def test_1(self):
      res = self.epi.transliterate("kind")
      self.assertEqual(res, "kint")
    
    def test_2(self):
      res = self.epi.transliterate("tjap")
      self.assertEqual(res, "tʃap")

    def test_3(self):
      res = self.epi.transliterate("berge")
      self.assertEqual(res, "berge")  

    def test_4(self):
      res = self.epi.transliterate("kwaad")
      self.assertEqual(res, "kwɑːt")
    
    def test_5(self):
      res = self.epi.transliterate("dink")
      self.assertEqual(res, "diŋk")

    def test_6(self):
      res = self.epi.transliterate("kus")
      self.assertEqual(res, "kɵs")

    def test_7(self):
      res = self.epi.transliterate("gat")
      self.assertEqual(res, "χat")
