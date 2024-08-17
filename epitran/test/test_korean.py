# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import epitran

class TestKorean(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('kor-Hang')

    ## Aspiration
    def test_anta(self):
        tr = self.epi.transliterate('않다')
        self.assertEqual(tr, 'antʰa')

    def test_silchi(self):
        tr = self.epi.transliterate('싫지')
        self.assertEqual(tr, 'silt͡ɕʰi')

    def test_tsohta(self):
        tr = self.epi.transliterate('좋다')
        self.assertEqual(tr, 't͡ɕotʰa')

    def test_chukha(self):
        tr = self.epi.transliterate('축하')
        self.assertEqual(tr, 't͡ɕʰukʰa')

    def test_palphida(self):
        tr = self.epi.transliterate('밟히다')
        self.assertEqual(tr, 'palpʰita')

    def test_hayathta(self):
        tr = self.epi.transliterate('하얗다')
        self.assertEqual(tr, 'hajatʰa')

    ## Simplification of consonant cluster codas
    def test_talk(self):
        tr = self.epi.transliterate('닭')
        self.assertEqual(tr, 'tak')

    def test_salm(self):
        tr = self.epi.transliterate('삶')
        self.assertEqual(tr, 'sam')

    def test_nok(self):
        tr = self.epi.transliterate('넋')
        self.assertEqual(tr, 'nʌk')

    ## Seven consonant constraints for codas
    def test_pak(self):
        tr = self.epi.transliterate('밖')
        self.assertEqual(tr, 'pak')

    def test_sut(self):
        tr = self.epi.transliterate('숯')
        self.assertEqual(tr, 'sut')

    def test_pich(self):
        tr = self.epi.transliterate('빚')
        self.assertEqual(tr, 'pit')

    def test_pit(self):
        tr = self.epi.transliterate('빗')
        self.assertEqual(tr, 'pit')

    ## Tensification
    def test_kukpap(self):
        tr = self.epi.transliterate('국밥')
        self.assertEqual(tr, 'kukp͈ap')

    def test_kkakta(self):
        tr = self.epi.transliterate('깎다')
        self.assertEqual(tr, 'k͈akt͈a')

    def test_kapchida(self):
        tr = self.epi.transliterate('값지다')
        self.assertEqual(tr, 'kapt͈͡ɕita')

    def test_deopkae(self):
        tr = self.epi.transliterate('덮개')
        self.assertEqual(tr, 'tʌpk͈ɛ')

    def test_ipko(self):
        tr = self.epi.transliterate('입고')
        self.assertEqual(tr, 'ipk͈o')

    def test_nokpadi(self):
        tr = self.epi.transliterate('넋받이')
        self.assertEqual(tr, 'nʌkp͈at͡ɕi')

    def test_sakdon(self):
        tr = self.epi.transliterate('삯돈')
        self.assertEqual(tr, 'sakt͈on')

    def test_padatda(self):
        tr = self.epi.transliterate('받았다')
        self.assertEqual(tr, 'patatt͈a')

    ## Nasalization
    def test_kungmul(self):
        tr = self.epi.transliterate('국물')
        self.assertEqual(tr, 'kuŋmul')

    def test_doklip(self):
        tr = self.epi.transliterate('독립')
        self.assertEqual(tr, 'toŋnip')

    def test_yeoklyu(self):
        tr = self.epi.transliterate('역류')
        self.assertEqual(tr, 'jʌŋnju')

    def test_kamri(self):
        tr = self.epi.transliterate('감리')
        self.assertEqual(tr, 'kamni')

    def test_ipron(self):
        tr = self.epi.transliterate('입론')
        self.assertEqual(tr, 'imnon')

    def test_jeongri(self):
        tr = self.epi.transliterate('정리')
        self.assertEqual(tr, 't͡ɕʌŋni')

    def test_heuknaemsae(self):
        tr = self.epi.transliterate('흙냄새')
        self.assertEqual(tr, 'hɯŋnɛmsɛ')

    ## Liquidization
    def test_umunron(self):
        tr = self.epi.transliterate('음운론')
        self.assertEqual(tr, 'ɯmullon')

    def test_silla(self):
        tr = self.epi.transliterate('신라')
        self.assertEqual(tr, 'silla')

    def test_kalnal(self):
        tr = self.epi.transliterate('칼날')
        self.assertEqual(tr, 'kʰallal')

    def test_tallneun(self):
        tr = self.epi.transliterate('닳는')
        self.assertEqual(tr, 'tallɯn')

    ## Check ll sequence
    def test_ppalli(self):
        tr = self.epi.transliterate('빨리')
        self.assertEqual(tr, 'p͈alli')

    ## Palatalization
    def test_kutsi(self):
        tr = self.epi.transliterate('굳이')
        self.assertEqual(tr, 'kut͡ɕi')

    def test_katsi(self):
        tr = self.epi.transliterate('같이')
        self.assertEqual(tr, 'kat͡ɕʰi')

    def test_putida(self):
        tr = self.epi.transliterate('붙이다')
        self.assertEqual(tr, 'put͡ɕʰita')

    ## Check linking sounds
    def test_nala(self):
        tr = self.epi.transliterate('날아')
        self.assertEqual(tr, 'nala')

    def test_boasseo(self):
        tr = self.epi.transliterate('봤어')
        self.assertEqual(tr, 'pwas͈ʌ')

    # ## Exceptions: Tensification (verb stems that ends with -n or -m)
    # def test_anta(self):
    #     tr = self.epi.transliterate('앉다')
    #     self.assertEqual(tr, 'ant͈a')

    # def test_anta(self):
    #     tr = self.epi.transliterate('심다')
    #     self.assertEqual(tr, 'simt͈a')

    # ## Exceptions: Tensification (after the adnominal ending -l)
    # def test_hal_su_itta(self):
    #     tr = self.epi.transliterate('할 수 있다')
    #     self.assertEqual(tr, 'hal s͈u itt͈a')

    # ## Exceptions: Tensification (verbs)
    # def test_palpda(self):
    #     tr = self.epi.transliterate('밟다')
    #     self.assertEqual(tr, 'papt͈a')

    # def test_malge(self):
    #     tr = self.epi.transliterate('맑게')
    #     self.assertEqual(tr, 'malk͈e')

    # ## Exceptions: -n insertion in compound words
    # def test_saeknyeonpil(self):
    #     tr = self.epi.transliterate('색연필')
    #     self.assertEqual(tr, 'sɛŋnjʌnʰpil')

    # def test_namunip(self):
    #     tr = self.epi.transliterate('나뭇잎')
    #     self.assertEqual(tr, 'namunnip')

    # def test_ha_deu_reot_il(self):
    #     tr = self.epi.transliterate('허드렛일')
    #     self.assertEqual(tr, 'hʌdɯrɛnnil')

    # ## etc (historical sound change)
    # def test_mulkogi(self):
    #     tr = self.epi.transliterate('물고기')
    #     self.assertEqual(tr, 'mulk͈ogi')

    # def test_bulkogi(self):
    #     tr = self.epi.transliterate('불고기')
    #     self.assertEqual(tr, 'pulkogi')