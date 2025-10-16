# -*- utf-8 -*-

import os.path

import regex as re

from . import cedict
from . import rules
from . import download
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

    def __init__(self, **kwargs) -> None:
        """Construct epitran object for Chinese

        Args:
            **kwargs: Optional parameters:
                ligatures (bool): if True, use ligatures instead of standard IPA (default: False)
                cedict_file (str): path to CC-CEDict dictionary file (default: None)
                rules_file (str): name of file with rules for converting pinyin to
                                  IPA (default: 'pinyin-to-ipa.txt')
                tones (bool): if True, output tones as Chao tone numbers; overrides
                              `rules_file` (default: False)
        """
        # Extract parameters with defaults
        ligatures = kwargs.get('ligatures', False)
        cedict_file = kwargs.get('cedict_file', None)
        rules_file = kwargs.get('rules_file', 'pinyin-to-ipa.txt')
        tones = kwargs.get('tones', False)
        assert ligatures is False, "Ligatures not supported for cmn-Hans"

        if not cedict_file:
            cedict_file = download.cedict()
        if tones:
            rules_file = os.path.join('data', 'rules', 'pinyin-to-ipa-tones.txt')
        else:
            rules_file = os.path.join('data', 'rules', rules_file)
        rules_file = os.path.join(os.path.dirname(__file__), rules_file)
        self.cedict = cedict.CEDictTrie(cedict_file)
        self.rules = rules.Rules([rules_file])
        self.regexp = re.compile(r'\p{Han}')

    def normalize_punc(self, text: str) -> str:
        """Normalize punctutation in a string

        Args:
            text (str): an orthographic string

        Return:
            str: an orthographic string with punctation normalized to
                     Western equivalents
        """
        for a, b in self.punc:
            text = text.replace(a, b)
        return text

    def transliterate(self, text: str, normpunc: bool = False, ligatures: bool = False) -> str:
        """Transliterates/transcribes a word into IPA

        Args:
            word (str): word to transcribe; Unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            str: Unicode IPA string
        """
        tokens = self.cedict.tokenize(text)
        ipa_tokens = []
        for token in tokens:
            if token in self.cedict.hanzi:
                (pinyin, _) = self.cedict.hanzi[token]
                pinyin_str = u''.join(pinyin).lower()
                ipa = self.rules.apply(pinyin_str)
                ipa_tokens.append(ipa.replace(u',', u''))
            else:
                if normpunc:
                    token = self.normalize_punc(token)
                ipa_tokens.append(token)
        ipa_tokens = list(map(ligaturize, ipa_tokens))\
                if ligatures else ipa_tokens
        return u''.join(ipa_tokens)

    def strict_trans(self, text: str, normpunc: bool = False, ligatures: bool = False) -> str:
        return self.transliterate(text, normpunc, ligatures)


class EpihanTraditional(Epihan):
    def __init__(self, **kwargs) -> None:
        """Construct epitran object for Traditional Chinese

        Args:
            **kwargs: Optional parameters:
                ligatures (bool): if True, use ligatures instead of standard IPA (default: False)
                cedict_file (str): path to CC-CEDict dictionary file (default: None)
                tones (bool): if True, include tone information (default: False)
                rules_file (str): name of file with rules for converting pinyin to
                                  IPA (default: 'pinyin-to-ipa.txt')
        """
        # Extract parameters with defaults
        ligatures = kwargs.get('ligatures', False)
        cedict_file = kwargs.get('cedict_file', None)
        tones = kwargs.get('tones', False)
        rules_file = kwargs.get('rules_file', 'pinyin-to-ipa.txt')
        assert ligatures is False, "Ligatures not supported for cmn-Hant"

        if not cedict_file:
            cedict_file = download.cedict()
        if tones:
            rules_file = os.path.join('data', 'rules', 'pinyin-to-ipa-tones.txt')
        else:
            rules_file = os.path.join('data', 'rules', rules_file)
        rules_file = os.path.join(os.path.dirname(__file__), rules_file)
        self.cedict = cedict.CEDictTrie(cedict_file, traditional=True)
        self.rules = rules.Rules([rules_file])
        self.regexp = re.compile(r'\p{Han}')

class EpiCanto(Epihan):
    def __init__(self, **kwargs) -> None:
        """Construct epitran object for Cantonese

        Args:
            **kwargs: Optional parameters:
                ligatures (bool): if True, use ligatures instead of standard IPA (default: False)
                cedict_file (str): path to CC-Canto dictionary file (default: None)
                tones (bool): if True, include tone information (default: False)
                rules_file (str): name of file with rules for converting jyutping to
                                  IPA (default: 'jyutping-to-ipa.txt')
        """
        # Extract parameters with defaults
        ligatures = kwargs.get('ligatures', False)
        cedict_file = kwargs.get('cedict_file', None)
        tones = kwargs.get('tones', False)
        rules_file = kwargs.get('rules_file', 'jyutping-to-ipa.txt')
        assert ligatures is False, 'Ligatures not supported for yue-Hant'

        if not cedict_file:
            cedict_file = download.cc_canto()
        if tones:
            rules_file = os.path.join('data', 'rules', 'jyutping-to-ipa-tones.txt')
        else:
            rules_file = os.path.join('data', 'rules', rules_file)
        rules_file = os.path.join(os.path.dirname(__file__), rules_file)
        self.cedict = cedict.CEDictTrieForCantonese(cedict_file, traditional=True)
        self.rules = rules.Rules([rules_file])
        self.regexp = re.compile(r'\p{Han}')

class EpiJpan(object):
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

    def __init__(self, **kwargs) -> None:
        """Construct epitran object for Japanese

        Args:
            **kwargs: Optional parameters:
                ligatures (bool): if True, use ligatures instead of standard IPA (default: False)
                cedict_file (str): path to src dictionary file (default: None)
                tones (bool): if True, include tone information (default: False)
        """
        # Extract parameters with defaults
        ligatures = kwargs.get('ligatures', False)
        cedict_file = kwargs.get('cedict_file', None)
        tones = kwargs.get('tones', False)
        assert ligatures is False, 'Ligatures not supported for jpn-Jpan'

        if not cedict_file:
            cedict_file = download.opendict_ja()
        self.cedict = cedict.CEDictTrieForJapanese(cedict_file)
        self.regexp = None
        self.tones = tones

    def normalize_punc(self, text: str) -> str:
        """Normalize punctutation in a string

        Args:
            text (str): an orthographic string

        Return:
            str: an orthographic string with punctation normalized to
                     Western equivalents
        """
        for a, b in self.punc:
            text = text.replace(a, b)
        return text

    def transliterate(self, text: str, normpunc: bool = False, ligatures: bool = False) -> str:
        tokens = self.cedict.tokenize(text)
        ipa_tokens = []
        for token in tokens:
            if token in self.cedict.character:
                ipa = self.cedict.character[token]
                ipas = u''.join(ipa).lower()
                ipa_tokens.append(ipas.replace(u',', u''))
            else:
                if normpunc:
                    token = self.normalize_punc(token)
                ipa_tokens.append(token)
                
        return u''.join(ipa_tokens)
