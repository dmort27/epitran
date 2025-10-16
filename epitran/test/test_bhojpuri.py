# -*- coding: utf-8 -*-


import unicodedata
import unittest

import epitran


class TestBhojpuriHalant(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran("bho-Deva")

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize("NFD", trans)
        src = unicodedata.normalize("NFD", trans)
        self.assertEqual(trans, tar)

    def test_knay(self):
        self._assert_trans("क्नय्", "knəj")


class TestBhojpuri(unittest.TestCase):
    def setUp(self):
        # Initialize Epitran with the Bhojpuri (Devanagari) model
        self.epi = epitran.Epitran("bho-Deva")
        self.epi_hin = epitran.Epitran("hin-Deva")

    def _assert_trans(self, src, tar):
        trans = self.epi.transliterate(src)
        trans = unicodedata.normalize("NFD", trans)
        src = unicodedata.normalize("NFD", src)
        self.assertEqual(trans, tar)

    def test_ham(self):
        """Common Bhojpuri first-person singular 'हम'."""
        self._assert_trans("हम", "ɦəm")

    def test_bhojpuri(self):
        """Tests the word 'भोजपुरी' itself."""
        self._assert_trans("भोजपुरी", "b̤od͡ʒpuriː")

    def test_tu(self):
        """Common second-person singular 'तू'."""
        self._assert_trans("तू", "tuː")

    def test_raura(self):
        """Second-person honorific 'रउरा'."""
        self._assert_trans("रउरा", "rəuraː")

    def test_babujee(self):
        """A polite or affectionate address 'बाबूजी'."""
        self._assert_trans("बाबूजी", "baːbuːd͡ʒiː")

    def test_hamni(self):
        """
        'हमनी' (hamni) - a first-person plural (or inclusive) form.
        """
        self._assert_trans("हमनी", "ɦəmniː")

    def test_bhojpuria(self):
        """
        'भोजपुरिया' (bhojpuriyā) - a colloquial adjective for 'Bhojpuri'.
        """
        self._assert_trans("भोजपुरिया", "b̤od͡ʒpurijaː")

    def test_kehu(self):
        """
        'केहू' (kehū) - means 'someone/anyone' in Bhojpuri.
        """
        self._assert_trans("केहू", "keɦuː")

    def test_aisan(self):
        """
        'अइसन' (aisan) - meaning 'like this/that'.
        """
        self._assert_trans("अइसन", "aisən")

    def test_kaisan(self):
        """
        'कइसन' (kaisan) - 'how is/are ... ?' (colloquial greeting or question).
        """
        self._assert_trans("कइसन", "kəisən")

    def test_bhaiya(self):
        """
        'भैया' (bhaiyā) - 'brother', a common term of address.
        """
        self._assert_trans("भैया", "b̤æːjaː")

    def test_roti(self):
        """
        'रोटी' (roṭī) - 'bread/flatbread'.
        """
        self._assert_trans("रोटी", "roʈiː")

    def test_laika(self):
        """
        'लइका' (laikā) - 'child' (often a boy); can vary by region.
        """
        self._assert_trans("लइका", "ləikaː")

    def test_hariyar(self):
        """
        'हरियर' (hariyar) - means 'green' or 'fresh' in many Bhojpuri dialects.
        """
        self._assert_trans("हरियर", "ɦərijər")

    def test_madiya(self):
        """
        'मड़इया' (maṛaiyā) - 'hut' (also spelled मड़ैया).
        """
        self._assert_trans("मड़इया", "məɽəijaː")

    def test_tani(self):
        """
        'तनी' (tanī) - polite softener meaning 'a little / kindly'.
        """
        self._assert_trans("तनी", "təniː")

    def test_na(self):
        """
        'ना' (nā) - emphatic particle or negative marker.
        """
        self._assert_trans("ना", "naː")

    def test_chali(self):
        """
        'चली' (chalī) - polite imperative form of 'go' or future form (e.g., she will go).
        """
        self._assert_trans("चली", "t͡ʃəliː")

    def test_khaibu(self):
        """
        'खइबू' (khaibū) - future tense, second person 'you will eat'.
        """
        self._assert_trans("खइबू", "kʰəibuː")

    def test_jani(self):
        """
        'जानी' (jānī) - polite imperative negative ('please don't').
        """
        self._assert_trans("जानी", "d͡ʒaːniː")

    def test_okara(self):
        """
        'ओकरा' (okarā) - 'to him/her', 'of him/her'.
        """
        self._assert_trans("ओकरा", "okraː")

    def test_gaila(self):
        """
        'गइला' (gailā) - a colloquial past tense form meaning 'went'.
        """
        self._assert_trans("गइला", "ɡəilaː")

    def test_gyan(self):
        """
        'ज्ञान' (gyān) - 'knowledge' (borrowed from Sanskrit).
        """
        self._assert_trans("ज्ञान", "d͡ʒɲaːn")

    def test_chhota(self):
        """
        'छोटा' (chhoṭā) - 'small'.
        """
        self._assert_trans("छोटा", "t͡ʃʰoʈaː")

    def test_lakshmi(self):
        """
        'लक्ष्मी' (lakshmī) - 'Lakshmi' or 'wealth' in a broader sense.
        """
        self._assert_trans("लक्ष्मी", "ləkʂmiː")

    def test_pakauda(self):
        """
        'पकौड़ा' (pakauṛā) - 'fritter' (common snack).
        """
        self._assert_trans("पकौड़ा", "pəkɔːɽaː")

    def test_dhela(self):
        """
        'ढेला' (ḍhelā) - 'clod' or 'clump of earth'.
        """
        self._assert_trans("ढेला", "ɖ̤elaː")

    def test_hansi(self):
        """
        'हँसी' (hãsī) - 'laughter'.
        """
        self._assert_trans("हँसी", "ɦə̃siː")

    def test_bahut(self):
        """
        'बहुत' (bahut) - 'very'.
        """
        self._assert_trans("बहुत", "bəɦut")

    def test_tumhar(self):
        """
        'तुम्हार' (tumhār) - 'your (possessive)'.
        """
        self._assert_trans("तुम्हार", "tumɦaːr")

    def test_kadhai(self):
        """
        'कढ़ाई' (kaḍhāī) - 'wok', a cooking utensil.
        """
        self._assert_trans("कढ़ाई", "kəɽ̥aːiː")
