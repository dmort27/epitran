# -*- coding: utf-8 -*-
from __future__ import (print_function, absolute_import,
                        unicode_literals)

import regex as re
from . import _epitran
import panphon.featuretable
from epitran.puncnorm import PuncNorm
from epitran.xsampa import XSampa


class Backoff(object):
    """Implements rudimentary language ID and backoff"""

    def __init__(self, lang_script_codes, cedict_file=None):
        self.langs = [_epitran.Epitran(c, cedict_file=cedict_file)
                      for c in lang_script_codes]
        self.num_re = re.compile(r'\p{Number}+')
        self.ft = panphon.featuretable.FeatureTable()
        self.xsampa = XSampa()
        self.puncnorm = PuncNorm()

    def transliterate(self, token):
        """Return IPA transliteration given by first acceptable mode

        Args:
            token (unicode): orthographic text

        Returns:
            unicode: transliteration as Unicode IPA string
        """
        for lang in self.langs:
            if ''.join(lang.epi.regexp.findall(token)) == token:
                return lang.transliterate(token)
        if re.match(r'^\p{Number}+$'):
            return token
        else:
            return ''

    def trans_list(self, token):
        """Transliterates/transcribes a word into list of IPA phonemes

        Args:
            token (unicode): word to transcribe; unicode string

        Returns:
            list: list of IPA strings, each corresponding to a segment
        """
        return self.ft.segs_safe(self.transliterate(token))

    def xsampa_list(self, token):
        if re.match(r'^\p{Number}+$', token):
            return ''
        else:
            ipa_segs = self.ft.ipa_segs(self.transliterate(token))
            return list(map(self.xsampa.ipa2xs, ipa_segs))
