

import unittest
import unicodedata

import epitran


class TestGalician(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('glg-Latn')

    def test_niño(self):
        tr = self.epi.transliterate('niño')
        self.assertEqual(tr, 'niɲʊ')

    def test_cruz(self):
        tr = self.epi.transliterate('cruz')
        self.assertEqual(tr, 'kɾuθ')

    def test_coller(self):
        tr = self.epi.transliterate('coller')
        self.assertEqual(tr, 'koʎeɾ')

    def test_rato(self):
        tr = self.epi.transliterate('rato')
        self.assertEqual(tr, 'ratʊ')

    def test_vida(self):
        tr = self.epi.transliterate('vida')
        self.assertEqual(tr, 'bidɐ')

    def test_c_context(self):
        cases = {
            'escola': 'eskolɐ',
            'cena': 'θenɐ',
            'coco': 'kokʊ',
            'acción': 'akθjón',
            'cos': 'kos',
            'cima': 'θimɐ',
            'cero': 'θeɾʊ',
            'café': 'kafɛ',
            'cubo': 'kubʊ',
            'cruz': 'kɾuθ',
            'claro': 'klaɾʊ',
            'cé': 'θɛ',
            'cí': 'θi',
            'chave': 'tʃ͡abɪ',
            'pechar': 'petʃ͡aɾ',
        }
        for word, expected in cases.items():
            for form in ('NFC', 'NFD'):
                with self.subTest(word=word, form=form):
                    self.assertEqual(
                        self.epi.transliterate(unicodedata.normalize(form, word)),
                        expected,
                    )

    def test_c_in_phrases(self):
        # Use consonant-final words to isolate c from final-vowel rules.
        for word, expected in (('cos', 'kos'), ('cruz', 'kɾuθ'),
                               ('pechar', 'petʃ͡aɾ')):
            for phrase, position in ((word + ' amigos', 0),
                                     ('Hoxe quero estudar ' + word + ' meus amigos', 3),
                                     ('Hoxe quero estudar ' + word, -1)):
                with self.subTest(phrase=phrase):
                    self.assertEqual(self.epi.transliterate(word), expected)
                    self.assertEqual(
                        self.epi.transliterate(phrase).split()[position], expected,
                    )

    def test_word_initial_r(self):
        for text, expected in (
            ('rato', 'ratʊ'),
            ('o rato', 'ʊ ratʊ'),
            ('(RATO)', '(ratʊ)'),
            ('rato-rato', 'ratʊ-ratʊ'),
            ('rato\nrato', 'ratʊ\nratʊ'),
            ('caro', 'kaɾʊ'),
            ('carro', 'karʊ'),
        ):
            with self.subTest(text=text):
                self.assertEqual(self.epi.transliterate(text), expected)

    def test_final_vowels_at_word_boundaries(self):
        for word, expected in (('escola', 'eskolɐ'), ('chave', 'tʃ͡abɪ'),
                               ('coco', 'kokʊ')):
            for separator in (' ', '\t', '\n', ', ', '. ', '—', '-'):
                with self.subTest(word=word, separator=separator):
                    self.assertEqual(
                        self.epi.transliterate(word + separator + word),
                        expected + separator + expected,
                    )
            with self.subTest(word=word, punctuation=True):
                self.assertEqual(self.epi.transliterate('«' + word + '.»'),
                                 '«' + expected + '.»')

    def test_boundary_rules_preserve_accented_vowels(self):
        # A decomposed accent belongs to the vowel, not to a word boundary.
        for text, expected in (('café café.', 'kafɛ kafɛ.'),
                               ('avó avó.', 'abɔ abɔ.'),
                               ('está está.', 'esta esta.'),
                               ('árido', 'aɾidʊ')):
            for form in ('NFC', 'NFD'):
                with self.subTest(text=text, form=form):
                    self.assertEqual(
                        self.epi.transliterate(unicodedata.normalize(form, text)),
                        expected,
                    )
