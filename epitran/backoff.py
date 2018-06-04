# -*- coding: utf-8 -*-
from __future__ import print_function

import regex as re
from . import _epitran


class Backoff(object):
    """Implements rudimentary language ID and backoff"""

    def __init__(self, lang_script_codes, cedict_file=None):
        self.langs = [_epitran.Epitran(c, cedict_file=cedict_file)
                      for c in lang_script_codes]
        self.num_re = re.compile(r'\p{Number}+')

    def transliterate(self, token):
        for lang in self.langs:
            if ''.join(lang.epi.regexp.findall(token)) == token:
                return lang.transliterate(token)
        if re.match(r'^\p{Number}+$'):
            return token
        else:
            return ''
