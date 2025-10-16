# -*- coding: utf-8 -*-

from typing import List, Optional, Union
import regex as re
from . import _epitran
import panphon.featuretable
from epitran.puncnorm import PuncNorm
from epitran.xsampa import XSampa
from epitran.stripdiacritics import StripDiacritics


class Backoff(object):
    """Implements rudimentary language ID and backoff."""

    def __init__(self, lang_script_codes: List[str], cedict_file: Optional[str] = None) -> None:
        """Construct a Backoff object.

        Parameters
        ----------
        lang_script_codes : list
            Codes for languages to try, starting with the highest priority 
            languages.
        cedict_file : str, optional
            Path to the CC-CEdict dictionary file (necessary only when 
            cmn-Hans or cmn-Hant are used). Default is None.
        """
        self.langs = [_epitran.Epitran(c, cedict_file=cedict_file)
                      for c in lang_script_codes]
        self.num_re = re.compile(r'\p{Number}+')
        self.ft = panphon.featuretable.FeatureTable()
        self.xsampa = XSampa()
        self.puncnorm = PuncNorm()
        self.dias = [StripDiacritics(c) for c in lang_script_codes]

    def transliterate(self, token: str) -> str:
        """Return IPA transliteration given by first acceptable mode.

        Parameters
        ----------
        token : str
            Orthographic text.

        Returns
        -------
        str
            Transliteration as Unicode IPA string.
        """
        tr_list = []
        while token:
            is_outside_lang = True
            for dia, lang in zip(self.dias, self.langs):
                source = ''
                while True:
                    m = lang.epi.regexp.match(dia.process(token))
                    if not m:
                        break
                    s = m.group()
                    token = token[len(s):]
                    source += s
                    is_outside_lang = False
                tr_list.append(lang.transliterate(source))
            if is_outside_lang:
                m = re.match(r'\p{Number}+', token)
                if m:
                    source = m.group()
                    tr_list.append(source)
                    token = token[len(source):]
                else:
                    tr_list.append(token[0])
                    token = token[1:]
        return ''.join(tr_list)

    def trans_list(self, token: str) -> List[str]:
        """Transliterate/transcribe a word into list of IPA phonemes.

        Parameters
        ----------
        token : str
            Word to transcribe.

        Returns
        -------
        list
            List of IPA unicode strings, each corresponding to a segment.
        """
        return self.ft.segs_safe(self.transliterate(token))

    def xsampa_list(self, token: str) -> Union[str, List[str]]:
        """Transcribe a word into a list of X-SAMPA phonemes.

        Parameters
        ----------
        token : str
            Word to transcribe.

        Returns
        -------
        list
            List of X-SAMPA strings, each corresponding to a segment.
        """
        if re.match(r'^\p{Number}+$', token):
            return ''
        else:
            ipa_segs = self.ft.ipa_segs(self.transliterate(token))
            return list(map(self.xsampa.ipa2xs, ipa_segs))
