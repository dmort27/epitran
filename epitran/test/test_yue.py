# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import epitran


class TestYue(unittest.TestCase):
    

    def setUp(self):
        self.epi = epitran.Epitran('yue-Latn')
        
        # wikipedia derived test cases 
        self.tester_exs = [
            ('sam1','sɐm˥'), #心 
            ('sau2','sɐw˨˥'), #手
            ('jat1','jɐt̚˥'), #一
            ('jau5','jɐw˨˧'), #有
            ('zyu1','tsy˥'), #猪
            ('waa6','wa˨'), #话
            ('jan4','jɐn˨˩'), #人
            ('goe3','kœ˧'), #鋸
            ('tin1','tʰin˥'), #天
            ('hou2','hɔw˨˥'), #好
            ('dou1','tɔw˥'), #都
            ('maa5','ma˨˧') #马，妈
        ]


    def test(self):
        
        for ex in self.tester_exs: 
            jyuping, ipa = ex
            pred = self.epi.transliterate(jyuping)
            self.assertEqual(pred, ipa)
            # if pred != ipa: 
            #     print(f'{pred} - {ipa}')
