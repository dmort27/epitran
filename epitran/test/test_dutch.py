
import unittest

import epitran


def assemble_ipa(xs):
    return ''.join([x[3] for x in xs])


class TestDutch(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('nld-Latn')

    def _derivation(self, orth, correct):
        attempt = assemble_ipa(self.epi.word_to_tuples(orth))
        self.assertEqual(attempt, correct)

    def test_bernhard(self):
        self._derivation('Bernhard', 'bɛrnhɑrt')

    def test_utrecht(self):
        self._derivation('Utrecht', 'ʏtrɛxt')

    def test_lodewijk(self):
        self._derivation('Lodewijk', 'loːdeːʋɛjk')

    def test_random(self):
        self._derivation('ertogenbosch', 'ɛrtoːɣɛnbɔs')

    def test_reported_sch_ng_and_ij_contexts(self):
        self._derivation('schreef', 'sxreːf')
        self._derivation('ring', 'rɪŋ')
        self._derivation('bijeenkomst', 'bɛjeːnkɔmst')

    def test_reported_accents_and_trema(self):
        for word, expected in [
            ('oké', 'oːkɛ'),
            ('één', 'ɛɛn'),
            ('vóór', 'voːr'),
            ('reünie', 'reːyniː'),
            ('ideeën', 'iːdeːən'),
        ]:
            with self.subTest(word=word):
                self._derivation(word, expected)
