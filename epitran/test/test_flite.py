#!/usr/bin/env Python
from __future__ import unicode_literals, print_function

import unittest
import flite
import types


class TestVectorWithIPASpace(unittest.TestCase):
    def setUp(self):
        self.vwis = flite.VectorsWithIPASpace()

    def test_data_structure1(self):
        for seg in self.vwis.word_to_segs('DRY-dipped'):
            self.assertEqual(len(seg), 6)
            self.assertIsInstance(seg[0], types.StringTypes)
            self.assertIsInstance(seg[1], types.IntType)
            self.assertIsInstance(seg[2], types.StringTypes)
            self.assertIsInstance(seg[3], types.StringTypes)
            self.assertIsInstance(seg[4], types.IntType)
            self.assertIsInstance(seg[5], types.ListType)
            self.assertTrue(len(seg[5]) == self.vwis.num_panphon_fts)
            for v in seg[5]:
                self.assertIn(v, [-1, 0, 1])

    def test_data_structure2(self):
        for seg in self.vwis.word_to_segs('$variable'):
            self.assertEqual(len(seg), 6)
            self.assertIsInstance(seg[0], types.StringTypes)
            self.assertIsInstance(seg[1], types.IntType)
            self.assertIsInstance(seg[2], types.StringTypes)
            self.assertIsInstance(seg[3], types.StringTypes)
            self.assertIsInstance(seg[4], types.IntType)
            self.assertIsInstance(seg[5], types.ListType)
            self.assertTrue(len(seg[5]) == self.vwis.num_panphon_fts)
            for v in seg[5]:
                self.assertIn(v, [-1, 0, 1])

    def test_data_structure3(self):
        for seg in self.vwis.word_to_segs('San Leandro'):
            self.assertEqual(len(seg), 6)
            self.assertIsInstance(seg[0], types.StringTypes)
            self.assertIsInstance(seg[1], types.IntType)
            self.assertIsInstance(seg[2], types.StringTypes)
            self.assertIsInstance(seg[3], types.StringTypes)
            self.assertIsInstance(seg[4], types.IntType)
            self.assertIsInstance(seg[5], types.ListType)
            self.assertTrue(len(seg[5]) == self.vwis.num_panphon_fts)
            for v in seg[5]:
                self.assertIn(v, [-1, 0, 1])
