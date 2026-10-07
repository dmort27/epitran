

import unittest

import epitran


class TestJapanese(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'jpn-Hira')

    def test_longvowels(self):
        tr = self.epi.transliterate('とうきょう')
        self.assertEqual(tr, 'toːkʲoː')
