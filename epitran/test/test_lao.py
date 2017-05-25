# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestLao(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('lao-Laoo')

    def test_aksonlao(self):
        tr = self.epi.transliterate('ອັກສອນລາວ')
        self.assertEqual(tr, 'ʔaksɔːnlaːw')

    def test_phanyasana(self):
        tr = self.epi.transliterate('ພະຍັນຊະນະ')
        self.assertEqual(tr, 'pʰaɲansana')

    def test_sala(self):
        tr = self.epi.transliterate('ສະຫລະ')
        self.assertEqual(tr, 'sala')

    def test_khuangmaysam(self):
        tr = self.epi.transliterate('ເຄ່ຶອງໝາຍຊ້ຳ')
        self.assertEqual(tr, 'kʰɯəŋmaːjsam')

    def test_am(self):
        tr = self.epi.transliterate('ຳ')
        self.assertEqual(tr, 'am')

    def test_peet(self):
        tr = self.epi.transliterate('ແປດ')
        self.assertEqual(tr, 'pɛːt')
