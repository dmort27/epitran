# -*- coding: utf-8 -*-


import unicodedata
import unittest

import epitran


class TestNepali(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('npi-Deva')

    def _assert_trans(self, src, tar):
        trans = unicodedata.normalize('NFD', self.epi.transliterate(src))
        self.assertEqual(trans, unicodedata.normalize('NFD', tar))

    def test_words(self):
        pairs = [
            ('तिर', 'tiɾʌ'),
            ('बाट', 'baʈʌ'),
            ('अब', 'ʌbʌ'),
            ('दुख', 'dukʰʌ'),
            ('सुख', 'sukʰʌ'),
            ('काम', 'kam'),
            ('नाम', 'nam'),
            ('हात', 'ɦat'),
            ('मन', 'mʌn'),
            ('घर', 'ɡʱʌɾ'),
            ('रकम', 'ɾʌkʌm'),
            ('किताब', 'kitab'),
            ('सहर', 'sʌɦʌɾ'),
            ('ज्ञान', 'ɡjan'),
            ('गर्छ', 'ɡʌɾt͡sʰʌ'),
            ('जान्छ', 'd͡zant͡sʰʌ'),
            ('भित्र', 'bʱitɾʌ'),
            ('दुखी', 'dukʰi'),
            ('बाटो', 'baʈo'),
            ('तिर्नु', 'tiɾnu'),
            ('नेपाली', 'nepali'),
            ('हुन्छ', 'ɦunt͡sʰʌ'),
            ('घण्टा', 'ɡʱʌnʈa'),
            ('बाण', 'baɳ'),
            ('गणित', 'ɡʌɳit'),
        ]
        for src, tar in pairs:
            with self.subTest(src=src):
                self._assert_trans(src, tar)
