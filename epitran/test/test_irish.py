# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran

class TestIrish(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran(u'gle-Latn')

    def _assert_transcription_match(self,orth,phon):
        #print(f"Individual test: {orth}")
        pred = self.epi.transliterate(orth)
        self.assertEqual(pred,phon)

    # Test broad vowels
    def test_ao_ae(self):
        pairs = [
            ('saol',u'siːl'),
            ('gaois',u'giːʃ'),
            ('naoi',u'niː'),
            ('Gaelach',u'geːlax'),
            ('Gaeilge',u'geːlʲɟe'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)
    
    def test_a_ai(self):
        pairs = [
            (u'baile',u'balʲe'),
            (u'airne',u'aːɾnʲe'),
            (u'airde',u'aːɾdʲe'),
            (u'caillte',u'kalʲtʲe'),
            (u'crainn',u'kɾanʲ'),
            (u'eolais',u'oːlaʃ'),
            (u'maígh',u'miːj'),
            (u'gutaí',u'gutiː'),
            (u'naíonán',u'niːnaːn'),
            (u'beannaíonn',u'bʲaniːn')
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)
        
    def test_eo_standard(self):
        pairs = [
            (u'ceol',u'coːl'),
            (u'dreoilín',u'dʲɾʲoːlʲiːnʲ'),
            (u'eolais',u'oːlaʃ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)
        
    def test_eo_exceptions(self):
        ...

    def test_e_ea(self):
        pairs = [
            (u'te',u'tʲe'),
            (u'ceist',u'ceʃtʲ'),
            (u'eirleach',u'eːɾlʲax'),
            (u'ceirnín',u'ceːɾnʲiːnʲ'),
            (u'ceird','ceːɾdʲ'),
            #(u'creimeadh',u''), # final <dh>
            (u'sceimhle',u'ʃcivʲlʲe'),
            #(u'seinm',u'ʃinʲəmʲ'), # epenthesis
            (u'greim',u'ɟɾʲimʲ'),
            (u'sé',u'ʃeː'),
            (u'déanamh',u'dʲeːnaw'),
            (u'buidéal',u'bidʲeːl'),
            (u'scéimh',u'ʃceːvʲ'),
            (u'páipéir',u'paːpʲeːɾʲ'),
            (u'bean',u'bʲan'),
            (u'veain',u'vʲanʲ'),
            (u'ceardaí',u'caːɾdiː'),
            (u'bearna',u'bʲaːɾna'),
            (u'fearr',u'fʲaːɾ'),
            (u'feall',u'fʲal'),
            (u'feanntach',u'fʲantax'),
            (u'seisean',u'ʃeʃan'),
            (u'taoiseach',u'tiːʃax'),
            (u'Seán',u'ʃaːn'),
            (u'caisleán',u'kaʃlʲaːn'),
            (u'meáin',u'mʲaːnʲ'),
            (u'caisleáin',u'kaʃlʲaːnʲ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_i_io(self):
        pairs = [
            (u'pic',u'pʲic'),
            (u'ifreann',u'ifʲɾʲan'),
            (u'cill',u'cilʲ'),
            (u'cinnte',u'cinʲtʲe'),
            (u'im',u'imʲ'),
            (u'faoistin',u'fiːʃtʲinʲ'),
            (u'gnímh',u'ɟnʲiːvʲ'),
            (u'cailín',u'kalʲiːnʲ'),
            (u'síol',u'ʃiːl'),
            (u'fios',u'fʲis'),
            (u'bior',u'bʲiɾ'),
            (u'cion',u'cin'),
            (u'giota',u'ɟita'),
            (u'giodam',u'ɟidam'),
            (u'friotháil',u'fʲɾʲihaːlʲ'),
            (u'siopa',u'ʃipa'),
            (u'liom',u'lʲim'),
            #(u'tiocfaidh',u'tʲikiː'), # verb ending containing <f>
            (u'Siobhán',u'ʃiwaːn'),
            (u'briogáid',u'bʲɾʲigaːdʲ'),
            (u'tiomáin',u'tʲimaːnʲ'),
            (u'fionn',u'fʲin'),
            (u'sióg',u'ʃiːoːg'),
            (u'pióg',u'pʲiːoːg'),
            (u'grióir',u'ɟɾʲiːoːɾʲ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_ia(self):
        pairs = [
            (u'Diarmaid',u'dʲiəɾmadʲ'),
            (u'bliain',u'bʲlʲiənʲ'),
            (u'bián',u'bʲiːaːn'),
            (u'liáin',u'lʲiːaːnʲ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_iu(self):
        pairs = [
            (u'fliuch',u'fʲlʲux'),
            (u'siúl',u'ʃuːl'),
            (u'bailiú',u'balʲuː'),
            (u'ciúin',u'cuːnʲ'),
            (u'inniúil',u'inʲuːlʲ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_o(self):
        pairs = [
            (u'post',u'post'),
            (u'bord',u'boːɾd'),
            (u'orlach',u'oːɾlax'),
            #(u'conradh',u'konɾa'), #final <dh>
            (u'cromóg',u'kɾomoːg'),
            (u'fonn',u'fon'),
            (u'trom',u'tɾom'),
            (u'long',u'loŋg'),
            (u'mo',u'mo'),
            #(u'cothrom',u'koɾom'), #disappearing /h/
            (u'póg',u'poːg'),
            #(u'armónach',u'aɾəmoːnax'), #schwa-epenthesis
            (u'móin',u'moːnʲ'),
            (u'bádóir',u'baːdoːɾʲ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)
        

    def test_oi(self):
        pairs = [
            (u'scoil',u'skelʲ'),
            (u'troid',u'tɾedʲ'),
            (u'toitín',u'tetʲiːnʲ'),
            (u'oibre',u'ebʲɾʲe'),
            (u'thoir',u'heɾʲ'),
            (u'cloiche',u'kleçe'),
            (u'cois',u'koʃ'),
            #(u'cloisfidh',u'kloʃiː'), # final <dh>
            (u'boicht',u'boxtʲ'),
            (u'doirse',u'doɾʃe'),
            (u'goirt',u'goɾtʲ'),
            (u'oirthear',u'oɾhaɾ'),
            (u'coirnéal',u'koːɾnʲeːl'),
            (u'oird',u'oːɾdʲ'),
            (u'anois',u'aniʃ'),
            (u'gloine',u'glinʲe'),
            (u'cnoic',u'knic'),
            (u'roimh',u'ɾivʲ'),
            (u'coimeád',u'kimʲaːd'),
            (u'loinge',u'liɲɟe'),
            (u'foinn',u'finʲ'),
            (u'droim',u'dɾimʲ'),
            (u'goill',u'gilʲ'),
            (u'coillte',u'kilʲtʲe'),
        ]

        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)


    def test_u(self):
        pairs = [
            (u'dubh',u'duw'),
            (u'burla',u'buːɾla'),
            (u'murnán',u'muːɾnaːn'),
            (u'agus',u'agus'),
            (u'tús',u'tuːs'),
            (u'súil',u'suːlʲ'),
            (u'cosúil',u'kosuːlʲ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_ua_uo(self):
        pairs = [
            (u'fuar',u'fuəɾ'),
            (u'fuair',u'fuəɾʲ'),
            (u'ruán',u'ɾuːaːn'),
            (u'duán',u'duːaːn'),
            (u'fuáil',u'fuːaːlʲ'),
            (u'cruóg',u'kɾuːoːg'),
            (u'luóige',u'luːoːɟe'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_ui(self):
        pairs = [
            (u'duine',u'dinʲe'),
            #(u'duirling',u'diɾlʲinʲ'), # pronunciation unverified, seems dubious
            (u'tuirne',u'tiɾnʲe'),
            (u'tuillteanach',u'tilʲtʲanax'),
            (u'puinn',u'pinʲ'),
            (u'suim',u'simʲ'),
            (u'aguisín',u'agiʃiːnʲ'),
            (u'buígh',u'biːj'),
            (u'buíon',u'biːn'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    # Test normalization of spelling
    def test_spelling(self):
        ...

# Any individual test cases (eg. batch testing multiple words that contain
# a certain pattern) can be defined here
individual_tests = None

if individual_tests is not None:
    for pair in individual_tests:
        orth,phon = pair[:]
        def test_local(self,o=orth,p=phon):
            self._assert_transcription_match(o,p)

    setattr(TestIrish,f'test_{orth}',test_local)


if __name__ == '__main__':
    unittest.main()