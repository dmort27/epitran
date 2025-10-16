# -*- coding: utf-8 -*-


import unittest

import epitran

class TestLithuanianAeDisambiguation(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('lit-Latn')

    def test_grazu(self):
        tr = self.epi.transliterate('gražù')
        self.assertEqual(tr, 'ɡrɐʒʊ')

    def test_graza(self):
        tr = self.epi.transliterate('grąžá')
        self.assertEqual(tr, 'ɡraːʒɐ')

    def test_nesi(self):
        tr = self.epi.transliterate('nešì')
        self.assertEqual(tr, 'nʲɛɕɪ')

        tr = self.epi.transliterate('néšì')
        self.assertEqual(tr, 'nʲæːɕɪ')

    def test_tesi(self):
        tr = self.epi.transliterate('tęsì')
        self.assertEqual(tr, 'tʲæːsʲɪ')

    def test_ta1(self):
        tr = self.epi.transliterate('tà')
        self.assertEqual(tr, 'tɐ')

    def test_ta2(self):
        tr = self.epi.transliterate('tą')
        self.assertEqual(tr, 'taː')


class TestLithuanianVowelAdvancement(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('lit-Latn')

    def test_kurti(self):
        tr = self.epi.transliterate('kùrti')
        self.assertEqual(tr, 'kʊrʲtʲɪ')
        tr = self.epi.transliterate('kiùrti')
        self.assertEqual(tr, 'kʲʊ˖rʲtʲɪ')

    def test_zmonu(self):
        tr = self.epi.transliterate('žmonų̃')
        self.assertEqual(tr, 'ʒmoːnuː')
        tr = self.epi.transliterate('žmonių̃')
        self.assertEqual(tr, 'ʒmoːnʲuː˖')

    def test_zaluosius(self):
        tr = self.epi.transliterate('žalúosius')
        self.assertEqual(tr, 'ʒɐɫuɔsʲʊ˖s')
        tr = self.epi.transliterate('žaliúosius')
        self.assertEqual(tr, 'ʒɐlʲuɔ˖sʲʊ˖s')

    def test_zaloji(self):
        tr = self.epi.transliterate('žalóji')
        self.assertEqual(tr, 'ʒɐɫoːjɪ')
        tr = self.epi.transliterate('žalióji')
        self.assertEqual(tr, 'ʒɐlʲoː˖jɪ')

    """
    def test_koksas(self):
        # NOTE: This test will FAIL because we do not account for o -> ɔ (occurs in loanwords)
        tr = self.epi.transliterate('kòksas')
        self.assertEqual(tr, 'koːksɐs')
        tr = self.epi.transliterate('kiòskas')
        self.assertEqual(tr, 'kʲoː˖skɐs')
    """


class TestLithuanianJvVocalization(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('lit-Latn')

    def test_zolej(self):
        tr = self.epi.transliterate('žolėj')
        self.assertEqual(tr, 'ʒoːlʲeːɪ')


class TestLithuanianTkAspiration(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('lit-Latn')

    def test_kasmet(self):
        tr = self.epi.transliterate('kasmẽt')
        self.assertEqual(tr, 'kasʲmʲɛt') # unsure if correct
        tr = self.epi.transliterate('kasmẽt,')
        self.assertEqual(tr, 'kasʲmʲæːtʰ ')

    def test_bek(self):
        tr = self.epi.transliterate('bė́k')
        self.assertEqual(tr, 'bʲeːk')
        tr = self.epi.transliterate('bė́k!')
        self.assertEqual(tr, 'bʲeːkʰ!')


class TestLithuanianMisc(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('lit-Latn')

    def test_senas(self):
        tr = self.epi.transliterate('senès')
        self.assertEqual(tr, 'sʲɛnʲɛs')
        tr = self.epi.transliterate('senàs')
        self.assertEqual(tr, 'sʲɛnɐs')

    def test_pusti(self):
        tr = self.epi.transliterate('pùsti')
        self.assertEqual(tr, 'pʊsʲtʲɪ')
        tr = self.epi.transliterate('pū̃sti')
        self.assertEqual(tr, 'puːsʲtʲɪ')

    def test_kalnas(self):
        tr = self.epi.transliterate('kálnas')
        self.assertEqual(tr, 'kaːɫnɐs')

    def test_atsikele(self):
        tr = self.epi.transliterate('atsikė́lė')
        self.assertEqual(tr, 'ɐt͡sʲɪkʲeːlʲeː')

    def test_pussesere(self):
        tr = self.epi.transliterate('pùsseserė')
        self.assertEqual(tr, 'pʊsʲɛsʲɛrʲeː')

    def test_zemvaldys(self):
        tr = self.epi.transliterate('žemvaldỹs')
        self.assertEqual(tr, 'ʒʲɛɱvɐlʲdʲiːs')
