#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import logging
import unittest

import epitran

logger = logging.getLogger('epitran')


def assemble_ipa(xs):
    return ''.join([x[3] for x in xs])


class TestGermanDuden(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('deu-Latn')

    def _derivation(self, orth, correct):
        attempt = self.epi.transliterate(orth)
        self.assertEqual(attempt, correct)

    def test_da(self):
        self._derivation('da', 'daː')

    def test_abend(self):
        self._derivation('Abend', 'aːbn̩t')

    def test_sprache(self):
        self._derivation('Sprache', 'ʃpraːxə')

    def test_pass(self):
        self._derivation('Pass', 'pas')

    def test_qualaen(self):
        self._derivation('quälen', 'kvɛːlən')

    def test_gaeste(self):
        self._derivation('Gäste', 'ɡɛstə')

    def test_aal(self):
        self._derivation('Aal', 'aːl')

    def test_stahl(self):
        self._derivation('Stahl', 'ʃtaːl')

    def test_baer(self):
        self._derivation('Baer', 'bɛːɐ̯')

    def test_mai(self):
        self._derivation('Mai', 'maɪ̯')

    def test_auto(self):
        self._derivation('Auto', 'aʊ̯to')

    def test_hauser(self):
        self._derivation('Häuser', 'hɔɪ̯zɐ')

    def test_sauce(self):
        self._derivation('Soße', 'zoːsə')

    def test_bach(self):
        self._derivation('Bach', 'bax')

    def test_gelb(self):
        self._derivation('gelb', 'ɡɛlp')

    def test_schrubb(self):
        self._derivation('schrubb', 'ʃrʊp')

    def test_cafe(self):
        self._derivation('Café', 'kafeː')

    def test_city(self):
        self._derivation('City', 'sɪti')

    def test_broccoli(self):
        self._derivation('Broccoli', 'brɔkoli')

    def test_gnocchi(self):
        self._derivation('Gnocchi', 'njɔki')

    def test_gespraech(self):
        self._derivation('Gespräch', 'ɡəʃprɛç')

    def test_sprach(self):
        self._derivation('Sprache', 'ʃpraːxə')

    def test_fuchs(self):
        self._derivation('Fuchs', 'fʊks')

    def test_knicks(self):
        self._derivation('Knicks', 'knɪks')

    def test_drei(self):
        self._derivation('drei', 'draɪ̯')

    def test_gelt(self):
        self._derivation('geld', 'ɡɛlt')

    def test_knuddeln(self):
        self._derivation('knuddeln', 'knʊdl̩n')

    def test_dschungel(self):
        self._derivation('Dschungel', 'd͡ʒʊŋl̩')

    def test_staedte(self):
        self._derivation('Städte', 'ʃtɛːtə')

    def test_ego(self):
        self._derivation('ego', 'eːgo')

    def test_jedoch(self):
        self._derivation('jedoch', 'jedɔx')

    def test_area(self):
        self._derivation('Area', 'aːrea')

    def test_destructive(self):
        self._derivation('destructive', 'destrʊktiːf')

    def test_des(self):
        self._derivation('des', 'dɛs')

    def test_brechen(self):
        self._derivation('brechen', 'brɛçn̩')

    def test_menthol(self):
        self._derivation('Menthol', 'mɛntoːl')

    def test_erfassen(self):
        self._derivation('erfassen', 'ɛɐ̯fasn̩')

    def test_alte(self):
        self._derivation('Alte', 'altə')

    def test_liberal(self):
        self._derivation('liberal', 'libəraːl')

    def test_rohem(self):
        self._derivation('rohem', 'roːəm')

    def test_idee(self):
        self._derivation('Idee', 'ideː')

    def test_meer(self):
        self._derivation('Meer', 'meːɐ̯')

    def test_lehm(self):
        self._derivation('lehm', 'leːm')

    def test_(self):
        self._derivation('bei', 'baɪ̯')

    def test_teuer(self):
        self._derivation('teuer', 'tɔɪ̯ɐ')

    def test_meyer(self):
        self._derivation('Meyer', 'maɪ̯ɐ')

    def test_fisch(self):
        self._derivation('Fisch', 'fɪʃ')

    def test_affe(self):
        self._derivation('Affe', 'afə')

    def test_gas(self):
        self._derivation('Gas', 'ɡaːs')

    def test_weg(self):
        self._derivation('weg', 'vɛk')

    def test_koenig(self):
        self._derivation('König', 'køːnɪç')

    def test_egge(self):
        self._derivation('Egge', 'ɛɡə')

    def test_brigg(self):
        self._derivation('Brigg', 'brɪk')

    def test_bango(self):
        self._derivation('Bagno', 'banjo')

    def test_geheim(self):
        self._derivation('geheim', 'gəhaɪ̯m')

    def test_ruhe(self):
        self._derivation('Ruhe', 'ruːə')

    def test_bibel(self):
        self._derivation('Bibel', 'biːbl̩')

    def test_benzin(self):
        self._derivation('Benzin', 'bɛnt͡siːn')

    def test_likoer(self):
        self._derivation('Likör', 'likøːɐ̯')

    def test_mild(self):
        self._derivation('mild', 'mɪlt')

    def test_die(self):
        self._derivation('die', 'diː')

    def test_vielleicht(self):
        self._derivation('vielleicht', 'filaɪ̯çt')

    def test_ihn(self):
        self._derivation('ihn', 'iːn')

    def test_jagd(self):
        self._derivation('Jagd', 'jaːkt')

    def test_kalt(self):
        self._derivation('kalt', 'kalt')

    def test_brokkoli(self):
        self._derivation('brokkoli', 'brɔkoli')

    def test_liebe(self):
        self._derivation('Liebe', 'liːbə')

    def test_nadel(self):
        self._derivation('Nadel', 'naːdl̩')

    def test_alle(self):
        self._derivation('alle', 'alə')

    def test_man(self):
        self._derivation('man', 'man')

    def test_groesstem(self):
        self._derivation('größtem', 'ɡrøːstm̩')

    def test_kamm(self):
        self._derivation('Kamm', 'kam')

    def test_nacht(self):
        self._derivation('Nacht', 'naxt')

    def test_angst(self):
        self._derivation('Angst', 'aŋst')

    def test_lachend(self):
        self._derivation('lachend', 'laxn̩t')

    def test_bannt(self):
        self._derivation('bannt', 'bant')

    def test_logisch(self):
        self._derivation('logisch', 'loːɡɪʃ')

    def test_boa(self):
        self._derivation('Boa', 'boːa')

    def test_tumor(self):
        self._derivation('Tumor', 'tuːmoːɐ̯')

    def test_sozial(self):
        self._derivation('sozial', 'zot͡si̯aːl')

    def test_grog(self):
        self._derivation('Grog', 'grɔk')

    def test_toxin(self):
        self._derivation('Toxin', 'tɔksiːn')

    def test_boe(self):
        self._derivation('Bö', 'bøː')

    def test_foederal(self):
        self._derivation('föderal', 'fødəraːl')

    def test_bischoefe(self):
        self._derivation('Bischöfe', 'bɪʃœfə')

    def test_goethe(self):
        self._derivation('Goethe', 'ɡøːtə')

    def test_roh(self):
        self._derivation('roh', 'roː')

    def test_hoehe(self):
        self._derivation('Höhe', 'høːə')

    def test_boiler(self):
        self._derivation('Boiler', 'bɔɪ̯lɐ')

    def test_boot(self):
        self._derivation('Boot', 'boːt')

    def test_route(self):
        self._derivation('Route', 'ruːtə')

    def test_panne(self):
        self._derivation('Panne', 'panə')

    def test_apfel(self):
        self._derivation('apfel', 'ap͡fl̩')

    def test_phi(self):
        self._derivation('Phi', 'fiː')

    def test_suppe(self):
        self._derivation('Suppe', 'zʊpə')

    def test_qual(self):
        self._derivation('Qual', 'kvaːl')

    def test_rabe(self):
        self._derivation('Rabe', 'raːbə')

    def test_sehr(self):
        self._derivation('sehr', 'zeːɐ̯')

    def test_erleben(self):
        self._derivation('erleben', 'ɛɐ̯leːbn̩')

    def test_anders(self):
        self._derivation('anders', 'andɐs')

    def test_star(self):
        self._derivation('Star', 'ʃtaː')

    def test_kost(self):
        self._derivation('kost', 'kɔst')

    def test_(self):
        self._derivation('', '')

    def test_stigma(self):
        self._derivation('Stigma', 'ʃtɪɡma')

    def test_schule(self):
        self._derivation('Schule', 'ʃuːlə')

    def test_mass(self):
        self._derivation('Maß', 'maːs')

    def test_pass(self):
        self._derivation('Pass', 'pas')

    def test_treu(self):
        self._derivation('treu', 'trɔɪ̯')

    def test_athlet(self):
        self._derivation('Athlet', 'atleːt')

    def test_mitte(self):
        self._derivation('Mitte', 'mɪtə')

    def test_du(self):
        self._derivation('du', 'duː')

    def test_musik(self):
        self._derivation('Musik', 'muziːk')

    def test_brust(self):
        self._derivation('Brust', 'brʊst')

    def test_minus(self):
        self._derivation('minus', 'miːnʊs')

    def test_suess(self):
        self._derivation('süß', 'zyːs')

    def test_buero(self):
        self._derivation('Büro', 'byroː')

    def test_huebsch(self):
        self._derivation('hübsch', 'hʏpʃ')

    def test_mueller(self):
        self._derivation('Mueller', 'mʏlɐ')

    def test_frueh(self):
        self._derivation('früh', 'fryː')

    def test_vogel(self):
        self._derivation('Vogel', 'foːɡl̩')

    def test_watt(self):
        self._derivation('Watt', 'vat')

    def test_loew(self):
        self._derivation('Löw', 'løːf')

    def test_hexe(self):
        self._derivation('Hexe', 'hɛksə')

    def test_lyrik(self):
        self._derivation('Lyrik', 'lyːrɪk')

    def test_hymn(self):
        self._derivation('Hymne', 'hʏmnə')

    def test_zar(self):
        self._derivation('Zar', 't͡saː')

    def test_quiz(self):
        self._derivation('Quiz', 'kvɪs')

if __name__ == '__main__':
    unittest.main()