# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran

class TestIrish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'gle-Latn')

    # Test broad vowels
    def test_broad(self):
        tr = self.epi.transliterate('saol')
        self.assertEqual(tr,u'sˠiːlˠ')
        ...

    # Test normalization of spelling
    def test_spelling(self):
        ...

if __name__ == '__main__':
    unittest.main()