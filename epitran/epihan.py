# -*- utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

import os.path

import pkg_resources
import regex as re

from . import cedict
from . import rules
from epitran.ligaturize import ligaturize


class MissingData(Exception):
    pass


class Epihan(object):
    punc = [(u'\uff0c', u','),
            (u'\uff01', u'!'),
            (u'\uff1f', u'?'),
            (u'\uff1b', u';'),
            (u'\uff1a', u':'),
            (u'\uff08', u'('),
            (u'\uff09', u')'),
            (u'\uff3b', u'['),
            (u'\uff3d', u']'),
            (u'\u3010', u'['),
            (u'\u3011', u']'),
            ]

    def __init__(self, ligatures=False, cedict_file=None,
                 rules_file='pinyin-to-ipa.txt'):
        """Construct epitran object for Chinese

        Args:
            ligatures (bool): if True, use ligatures instead of standard IPA
            cedict_file (str): path to CC-CEDict dictionary file
            rules_file (str): name of file with rules for converting pinyin to
                              IPA
        """
        # If no cedict_file is specified, raise and error
        if not cedict_file:
            raise MissingData('Please specify a location ' +
                              'for the CC-CEDict file.')
        rules_file = os.path.join('data', 'rules', rules_file)
        rules_file = pkg_resources.resource_filename(__name__, rules_file)
        self.cedict = cedict.CEDictTrie(cedict_file)
        self.rules = rules.Rules([rules_file])
        self.regexp = re.compile(r'\p{Han}')

    def normalize_punc(self, text):
        """Normalize punctutation in a string

        Args:
            text (unicode): an orthographic string

        Return:
            unicode: an orthographic string with punctation normalized to
                     Western equivalents
        """
        for a, b in self.punc:
            text = text.replace(a, b)
        return text

    def transliterate(self, text, normpunc=False, ligatures=False):
        """Transliterates/transcribes a word into IPA

        Args:
            word (str): word to transcribe; unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            unicode: IPA string
        """
        tokens = self.cedict.tokenize(text)
        ipa_tokens = []
        for token in tokens:
            if token in self.cedict.hanzi:
                (pinyin, _) = self.cedict.hanzi[token]
                pinyin = u''.join(pinyin).lower()
                ipa = self.rules.apply(pinyin)
                ipa_tokens.append(ipa.replace(u',', u''))
            else:
                if normpunc:
                    token = self.normalize_punc(token)
                ipa_tokens.append(token)
            ipa_tokens = map(ligaturize, ipa_tokens)\
                if ligatures else ipa_tokens
        return u''.join(ipa_tokens)

    def strict_trans(self, text, normpunc=False, ligatures=False):
        return self.transliterate(text, normpunc, ligatures)


class EpihanTraditional(Epihan):
    def __init__(self, ligatures=False, cedict_file=None, rules_file='pinyin-to-ipa.txt'):
        """Construct epitran object for Traditional Chinese

        Args:
            ligatures (bool): if True, use ligatures instead of standard IPA
            cedict_file (str): path to CC-CEDict dictionary file
            rules_file (str): name of file with rules for converting pinyin to
                              IPA
        """
        if not cedict_file:
            raise MissingData('Please specify a location for the CC-CEDict file.')
        rules_file = os.path.join('data', 'rules', rules_file)
        rules_file = pkg_resources.resource_filename(__name__, rules_file)
        self.cedict = cedict.CEDictTrie(cedict_file, traditional=True)
        self.rules = rules.Rules([rules_file])
