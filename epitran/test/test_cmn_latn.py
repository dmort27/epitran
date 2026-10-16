import unittest

import epitran


class TestMandarinPinyinUe(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('cmn-Latn')

    def test_ue_after_jqx_and_l_n(self):
        for word, expected in [
            ('jue', 't͡ɕy̯ɛ'),
            ('que', 't͡ɕʰy̯ɛ'),
            ('xue', 'ɕy̯ɛ'),
            ('lüe', 'ly̯ɛ'),
            ('nüe', 'ny̯ɛ'),
        ]:
            with self.subTest(word=word):
                self.assertEqual(self.epi.transliterate(word), expected)
        self.assertEqual(self.epi.transliterate('yue'), 'y̯ɛ')
