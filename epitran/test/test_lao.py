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

    def test_suun(self):
        tr = self.epi.transliterate('ສູນ')
        self.assertEqual(tr, 'suːn')

    def test_nung(self):
        tr = self.epi.transliterate('ໜ່ຶງ')
        self.assertEqual(tr, 'nɯŋ')

    def test_soong(self):
        tr = self.epi.transliterate('ສອງ')
        self.assertEqual(tr, 'sɔːŋ')

    def test_saam(self):
        tr = self.epi.transliterate('ສາມ')
        self.assertEqual(tr, 'saːm')

    def test_sii(self):
        tr = self.epi.transliterate('ສີ')
        self.assertEqual(tr, 'siː')

    def test_haa(self):
        tr = self.epi.transliterate('ຫ້າ')
        self.assertEqual(tr, 'haː')

    def test_cet(self):
        tr = self.epi.transliterate('ເຈັດ')
        self.assertEqual(tr, 't͡ɕet')

    def test_peet(self):
        tr = self.epi.transliterate('ແປດ')
        self.assertEqual(tr, 'pɛːt')

    def test_kaw(self):
        tr = self.epi.transliterate('ເກ້ົາ')
        self.assertEqual(tr, 'kaw')
