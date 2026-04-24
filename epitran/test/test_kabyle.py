import unittest
import epitran

class TestKabyle(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran("kab-Latn")

    def test_basic_words(self):
        for i, o in [
            ("taqcict", "taqʃiʃt"),
            ("axxam", "aχːam"),
            ("Nniɣ", "nːiɣ"),
            ("abrid", "abrid"),
            ("tuwiḍ", "tuwidˤ"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)
