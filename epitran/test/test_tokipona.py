# -*- coding: utf-8 -*-


import unittest

import epitran


class TestTokiPona(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('tok-Latn')

    def test_word(self):
        # The Latin spelling of Toki Pona is exactly its IPA represientation
        tr = self.epi.transliterate('kijetesantakalu')
        self.assertEqual(tr, 'kijetesantakalu')

    def test_name(self):
        # Names are the only cases where capitalization is used
        tr = self.epi.transliterate('Misali')
        self.assertEqual(tr, 'misali')

    def test_ku(self):
        # Toki Pona words in common use, according to the Toki Pona Dictionary (ku)
        # Pulled from https://api.linku.la/v1/words on 2025-03-10
        ku = [
            'a', 'akesi', 'ala', 'alasa', 'ale', 'ali', 'anpa', 'ante', 'anu',
            'apeja', 'awen', 'e', 'en', 'epiku', 'esun', 'ijo', 'ike', 'ilo',
            'insa', 'isipin', 'jaki', 'jami', 'jan', 'jasima', 'jelo', 'jo',
            'jonke', 'kala', 'kalama', 'kama', 'kamalawala', 'kapesi', 'kasi',
            'ken', 'kepeken', 'kijetesantakalu', 'kiki', 'kili', 'kin', 'kipisi',
            'kiwen', 'ko', 'kokosila', 'kon', 'konwe', 'ku', 'kule', 'kulijo',
            'kulupu', 'kute', 'la', 'lanpan', 'lape', 'laso', 'lawa', 'leko',
            'len', 'lete', 'li', 'lili', 'linja', 'linluwi', 'lipu', 'loje',
            'lon', 'luka', 'lukin', 'lupa', 'ma', 'majuna', 'mama', 'mani',
            'meli', 'melome', 'meso', 'mi', 'mije', 'mijomi', 'misa', 'misikeke',
            'moku', 'moli', 'monsi', 'monsuta', 'mu', 'mulapisu', 'mun', 'musi',
            'mute', 'n', 'namako', 'nanpa', 'nasa', 'nasin', 'nena', 'ni', 'nimi',
            'nimisin', 'nja', 'noka', 'o', 'ojuta', 'oke', 'oko', 'olin',
            'omekapo', 'ona', 'open', 'owe', 'pakala', 'pake', 'pakola', 'pali',
            'palisa', 'pan', 'pana', 'penpo', 'pi', 'pika', 'pilin', 'pimeja',
            'pini', 'pipi', 'po', 'poka', 'poki', 'pona', 'powe', 'pu', 'puwa',
            'sama', 'san', 'seli', 'selo', 'seme', 'sewi', 'sijelo', 'sike',
            'sin', 'sina', 'sinpin', 'sitelen', 'soko', 'sona', 'soto', 'soweli',
            'su', 'suli', 'suno', 'supa', 'sutopatikuna', 'suwi', 'taki', 'tan',
            'taso', 'tawa', 'te', 'teje', 'telo', 'tenpo', 'to', 'toki', 'tomo',
            'tonsi', 'tu', 'unpa', 'unu', 'usawi', 'uta', 'utala', 'wa', 'walo',
            'wan', 'waso', 'wasoweli', 'wawa', 'weka', 'wekama', 'wile',
            'wuwojiti', 'yupekosi'
        ]

        for nimi in ku:
            # As above, the IPA should match the orthography exactly
            tr = self.epi.transliterate(nimi)
            self.assertEqual(nimi,tr)



