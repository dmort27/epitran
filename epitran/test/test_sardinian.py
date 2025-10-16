
import unittest
import epitran

class TestSardinian(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('sro-Latn')

    def test_vowels(self):
        for i, o in [
            ("ogu", "oɣu"), ("giòbia", "d͡ʒɔβja"), ("aturai", "atːuɾai"),
            ("letu", "letːu"), ("pedra", "pɛðra"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_consonant(self):
        for i, o in [
            ("dzigarru", "d͡ʒiɣarːu"), ("cibudda", "t͡ʃiβuɖːa"), ("casciali", "kaʃːali"),
            ("sballiai", "zbalːiai"), ("cuatru", "kwatːru"), ("moddi", "moɖːi") #exception: mɔɖːi
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)
    
    def test_acrossword(self):
        for i, o in [
            ("custu certu", "kustu ʒertu"), ("de terra", "de ðɛrːa"), ("a terra", "a tːɛrːa"),
            ("at postu", "a pːostu"), ("tres litros", "trɛ lːitːrɔs"), ("non galu", "nɔɲ ɡalu")
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

if __name__ == '__main__':
    unittest.main()