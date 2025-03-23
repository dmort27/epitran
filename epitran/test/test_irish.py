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

    # Test broad/slender vowels
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
        pairs = [
            (u'anseo',u'anʃo'),
            (u'deoch',u'dʲox'),
            (u'eochair',u'oxaɾʲ'),
            (u'seo',u'ʃo'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_e_ea(self):
        pairs = [
            (u'te',u'tʲe'),
            (u'ceist',u'ceʃtʲ'),
            (u'eirleach',u'eːɾlʲax'),
            (u'ceirnín',u'ceːɾnʲiːnʲ'),
            (u'ceird','ceːɾdʲ'),
            (u'creimeadh',u'cɾʲimʲəi'), # final <dh>
            (u'sceimhle',u'ʃcivʲlʲe'),
            #(u'seinm',u'ʃinʲəmʲ'), # epenthesis
            (u'greim',u'ɟɾʲimʲ'),
            (u'sé',u'ʃeː'),
            (u'déanamh',u'dʲeːnəu'), # final <mh>
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
            (u'gnímh',u'ɟɾʲiːvʲ'),
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
            (u'conradh',u'konɾəi'), #final <dh>
            (u'cromóg',u'kɾomoːg'),
            (u'fonn',u'fon'),
            (u'trom',u'tɾom'),
            (u'long',u'loŋg'),
            (u'mo',u'mo'),
            (u'cothrom',u'kohɾom'),
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
            #(u'cloisfidh',u'kloʃiː'), # final <dh>, /f/-removal
            (u'boicht',u'boxtʲ'),
            (u'doirse',u'doɾʃe'),
            (u'goirt',u'goɾtʲ'),
            (u'oirthear',u'oɾhaɾ'),
            (u'coirnéal',u'koːɾnʲeːl'),
            (u'oird',u'oːɾdʲ'),
            (u'anois',u'aniʃ'),
            (u'gloine',u'glinʲe'),
            (u'cnoic',u'kɾic'),
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
            (u'dubh',u'duː'),
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

    # Test consonants with predictable changes in pronunciation
    def test_dt(self):
        # <dt> is realized as /d/ as eclipsis, but /t/ elsewhere
        pairs = [
            (u'dtaisce',u'daʃce'),
            (u'greadta',u'ɟɾʲata'),
            (u'dtír',u'dʲiːɾʲ'),
            (u'goidte',u'getʲe'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_dh_gh(self):
        pairs = [
            (u'dhorn',u'ɣoːɾn'),
            (u'ádh',u'aː'),
            #(u'dhearg',u'jaɾəg'), # schwa-epenthesis
            (u'fáidh',u'faːj'),
            (u'ghasúr',u'ɣasuːɾ'),
            (u'Eoghan',u'oːan'),
            (u'gheata',u'jata'),
            (u'dóigh',u'doːj'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_n_clusters(self):
        pairs = [
            (u'naoi',u'niː'),
            (u'nótaí',u'noːtiː'),
            (u'mná',u'mɾaː'),
            (u'cnaipe',u'kɾapʲe'),
            (u'neart',u'nʲaɾt'),
            (u'gnéas',u'ɟɾʲeːs'),
            (u'cníopaire',u'cɾʲiːpaɾʲe'),
            (u'Eoin',u'oːnʲ'),
            (u'ngasúr',u'ŋasuːɾ'),
            (u'teanga',u'tʲaŋga'),
            (u'ngeata',u'ɲata'),
            (u'cuing',u'kiɲɟ'),
            (u'ingear',u'iɲɟaɾ'),
            (u'ceann',u'can'),
            (u'tinneas',u'tʲinʲas'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)
        
    def test_r(self):
        pairs = [
            (u'ruán',u'ɾuːaːn'),
            (u'cumhra',u'kuːɾa'), #final <mh>
            (u'fuar',u'fuəɾ'),
            (u'rí',u'ɾiː'),
            (u'airde',u'aːɾdʲe'),
            #(u'duirling',u'duːɾlʲənʲ'), # no source
            (u'coirnéal',u'koːɾnʲeːl'),
            (u'cuairt',u'kuəɾtʲ'),
            (u'sreang',u'sɾaŋg'),
            (u'tirim',u'tʲiɾʲimʲ'),
            (u'fuair',u'fuəɾʲ'),
            (u'carr',u'kaːɾ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_th(self):
        pairs = [
            #(u'thuaidh',u'huə'), # final <dh>
            (u'thíos',u'hiːs'),
            (u'athair',u'ahaɾʲ'),
            (u'coinnithe',u'kinʲihe'),
            (u'ith',u'ih'),
            #(u'foghlamtha',u'foːlamha'), # final <gh>
            (u'ruaigthe',u'ɾuəce'),
            (u'scuabtha',u'skuəpa'),
            (u'bláth',u'blaː'),
            (u'cliath',u'clʲiə'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_loan_consonants(self):
        pairs = [
            (u'jab',u'd͡ʒab'),
            (u'jíp',u'd͡ʒiːpʲ'),
            (u'vóta',u'woːta'),
            (u'veidhlín',u'vʲeːlʲiːnʲ'), # final <dh>
            (u'zú',u'zuː'),
            (u'Zen',u'ʒenʲ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    # Multigraphs involving <bh>, <dh>, <gh>, <mh>
    def test_xbh_xmh(self):
        pairs = [
            (u'Feabhra',u'fʲəuɾa'),
            (u'leabhair',u'lʲəuɾʲ'),
            (u'sabhall',u'səul'),
            (u'ramhraigh',u'ɾəuɾəi'), #<igh>
            (u'amhantar',u'əuntaɾ'),
            (u'Samhain',u'səunʲ'),
            (u'acadamh',u'akadəu'),
            (u'creideamh',u'cɾʲedʲəu'),
            (u'Domhnach',u'doːnax'),
            (u'comhar',u'koːɾ'),
            (u'domhain',u'doːnʲ'),
            (u'dubh',u'duː'),
            (u'tiubh',u'tʲuː'),
            (u'cumhra',u'kuːɾa'),
            (u'Mumhan',u'muːn'),
            (u'ciumhais',u'cuːʃ'),
            (u'lobhra',u'loːɾa'),
            (u'lobhar',u'loːɾ'),
            (u'lobhair',u'loːɾʲ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    def test_xdh_xgh(self):
        pairs = [
            (u'meadhg',u'mʲəig'),
            (u'adharc',u'əiɾk'),
            (u'adhairt',u'əiɾtʲ'),
            (u'saghsanna',u'səisana'),
            #(u'deagha',u'dəi'), # no source on pronunciation, can't verify that initial is supposed to be broad
            (u'aghaidh',u'əij'),
            #(u'margadh',u'maɾəgəi'), # schwa-epenthesis
            (u'briseadh',u'bʲɾʲiʃəi'),
            (u'aidhleann',u'əilʲan'),
            (u'aidhe',u'əi'),
            (u'aighneas',u'əinʲas'),
            (u'aighe',u'əi'),
            (u'caighean',u'kəin'),
            (u'cleachtaidh',u'clʲaxtəi'),
            (u'bacaigh',u'bakəi'),
            (u'feidhm',u'fʲeːmʲ'),
            (u'eidheann',u'eːn'),
            (u'meidhir',u'mʲeːɾʲ'),
            (u'feighlí',u'fʲeːlʲiː'),
            (u'leigheas',u'lʲeːs'),
            (u'feighil',u'fʲeːlʲ'),
            (u'ligh',u'lʲiː'),
            (u'guigh',u'giː'),
            (u'tuillidh',u'tilʲiː'),
            (u'coiligh',u'kelʲiː'),
            (u'oidhre',u'əiɾʲe'),
            (u'oidheanna',u'əina'),
            (u'oighreach',u'əiɾʲax'),
            (u'oigheann',u'əin'),
            (u'loighic',u'ləic'),
            (u'bodhrán',u'boːɾaːn'),
            (u'bodhar',u'boːɾ'),
            (u'bodhair',u'boːɾʲ'),
            (u'doghra',u'doːɾa'),
            (u'bogha',u'boː'),
            (u'broghais',u'bɾoːʃ'),
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)

    # Schwa-epenthesis
    def test_epenthesis(self):
        pairs = [
            (u'gorm',u'goɾəm'),
            (u'dearg',u'dʲaɾəg'),
            (u'dorcha',u'doɾəxa'),
            (u'ainm',u'anʲəmʲ'),
            (u'deilgneach',u'dʲelʲəɟnʲax'),
            (u'leanbh',u'lʲanəw'),
            (u'airgead',u'aɾʲəɟad'),
            (u'téarma',u'tʲeːɾma'),
            (u'dualgas',u'duəlgas'),
            (u'armónach',u'aɾəmoːnax'), #schwa-epenthesis
            (u'dhearg',u'jaɾəg'), # schwa-epenthesis
            (u'margadh',u'maɾəgəi'), # schwa-epenthesis
        ]
        for orth,phon in pairs:
            pred = self.epi.transliterate(orth)
            self.assertEqual(pred,phon)
        ...

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