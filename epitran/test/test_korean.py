# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import epitran

class TestKorean(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('kor-Hang')

    def test_vowels(self):        
        # 제5항 다만3
        for i, o in [
            ("무늬", "muni"), ("희망", "himaŋ"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_consonant_final(self):
        # 제9항
        for i, o in [
            ("닦다", "takt͈a"), ("키읔", "kʰiɯk"), ("키읔과", "kʰiɯkk͈wa"),
            ("옷", "ot"), ("웃다", "utt͈a"), ("있다", "itt͈a"),
            ("젖", "t͡ɕʌt"), ("빚다", "pitt͈a"), ("꽃", "k͈ot"),
            ("쫓다", "t͡ɕ͈ott͈a"), ("솥", "sot"), ("뱉다", "pɛtt͈a"),
            ("앞", "ap"), ("덮다", "tʌpt͈a"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_consonant_cluster_final(self):
        # 제10항, 제11항
        for i, o in [
            ("넋", "nʌk"), ("넋과", "nʌkk͈wa"), ("앉다", "ant͈a"),
            ("여덟", "jʌtʌl"), ("넓다", "nʌlt͈a"), ("외곬", "wekol"),
            ("핥다", "halt͈a"), ("값", "kap"), ("없다", "ʌpt͈a"),
            ("닭", "tak"), ("삶", "sam"), ("읊다", "ɯpt͈a"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_aspiration(self):
        # 제12항 1.
        for i, o in [
            ("놓고", "nokʰo"), ("좋던", "t͡ɕotʰʌn"), ("쌓지", "s͈at͡ɕʰi"),
            ("각하", "kakʰa"), ("밝히다", "palkʰita"), ("맏형", "matʰjuŋ"),
            ("좁히다", "t͡ɕopʰita"), ("넓히다", "nʌlpʰita"), ("꽃히다", "k͈ot͡ɕʰita"),
            ("앉히다", "ant͡ɕʰita"), ("숱하다", "sutʰata")
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_h(self):
        # 제12항 2. 3. 4.
        for i, o in [
            ("닿소", "tas͈o"), ("많소", "mans͈o"), ("싫소", "sils͈o"),
            ("놓는", "nonnɯn"), ("쌓네", "s͈anne"),
            ("낳은", "naɯn"), ("닳아", "tala"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_coda_onset(self):
        # 제13항
        for i, o in [
            ("깎아", "k͈ak͈a"), ("옷이", "osi"), ("있어", "is͈ʌ"),
            ("낮이", "nat͡ɕi"), ("꽃을", "k͈ot͡ɕʰɯl"), ("밭에", "patʰe"),
            ("아프로", "apʰɯro")
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_palatalization(self):
        # 제17항
        for i, o in [
            ("굳이", "kut͡ɕi"), ("밭이", "pat͡ɕʰi"), ("벼훑이", "pjʌhult͡ɕʰi"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_assimilation(self):
        # 제18항
        for i, o in [
            ("먹는", "muŋnɯn"), ("깎는", "k͈aŋnɯn"), ("키읔만", "kʰiɯkman"),
            ("몫몫이", "moŋmoks͈i"), ("긁는", "kɯŋnɯn"), ("닫는", "tannɯn"),
            ("짓는", "t͡ɕinnɯn"), ("있는", "innɯn"), ("맞는", "mannɯn"),
            ("쫓는", "t͡ɕ͈onnɯn"), ("붙는", "punnɯn"), ("놓는", "nonnɯn"),
            ("잡는", "t͡ɕamnɯn"), ("앞마당", "ammataŋ"), ("밟는", "pamnɯn"),
            ("읊는", "ɯmnɯn"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_nasalization(self):
        # 제19항
        for i, o in [
            ("담력", "tamnjʌk"), ("강릉", "kaŋnɯŋ"),
            ("막론", "maŋnon"), ("법리", "pʌmni"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_liquidization(self):
        # 제20항
        for i, o in [
            ("난로", "nallo"), ("칼날", "kʰallal"), ("물난리", "mullalli")
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_tensification(self):
        # 제23항, 제24항, 제25항
        for i, o in [
            ("국밥", "kukp͈ap"), ("깎다", "k͈ak͈t͈a"), ("넋받이", "nʌkp͈at͡ɕi"),
            ("닭장", "takt͡ɕ͈aŋ"),

            ("뻗대다", "p͈ʌtt͈eta"), ("옷고름", "otk͈orɯm"), ("있던", "itt͈ʌn"),
            ("꽂고", "k͈otk͈o"), ("꽃다발", "k͈ott͈apal"), ("낯설다", "nats͈ʌlta"),

            ("밭갈이", "patk͈ari"), ("곱돌", "kopt͈ol"), ("덮개", "tupk͈e"),
            ("넓죽하다", "nʌpt͡ɕ͈ukʰata"), ("읊조리다", "ɯpt͡ɕ͈orita"), ("값지다", "kapt͡ɕ͈ita"),

            ("신고", "sink͈o"), ("얹다", "ʌnt͡ɕ͈a"),
            ("삼고", "samk͈o"), ("더듬지", "tʌtɯmt͡ɕ͈i"),

            ("넓게", "nʌlk͈e"), ("핥다", "halt͈a"),
            ("훑소", "huls͈o"), ("떫지", "t͈ʌlt͡ɕ͈i"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)


    def test_insertion(self):
        # 제30항
        for i, o in [
            ("냇가", "nek͈a"), ("샛길", "sek͈il"), ("콧등", "kʰot͈ɯŋ"),
            ("깃발", "kip͈al"), ("햇살", "hes͈al"), ("고갯짓", "koket͡ɕ͈it"),
            ("콧날", "konnal"), ("뱃머리", "benmʌri"),
            ("배갯잇", "bekennit"), ("깻잎", "k͈ennip"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

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


if __name__ == '__main__':
    unittest.main()
