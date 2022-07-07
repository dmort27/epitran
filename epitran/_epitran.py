# -*- coding: utf-8 -*-
import logging
from typing import Union

import panphon.featuretable
from epitran.epihan import Epihan, EpihanTraditional
from epitran.flite import FliteLexLookup
from epitran.puncnorm import PuncNorm
from epitran.simple import SimpleEpitran
from epitran.xsampa import XSampa

logger = logging.getLogger('epitran')
logger.setLevel(logging.WARNING)

class Epitran(object):
    """Unified interface for IPA transliteration/transcription

    :param code str: ISO 639-3 plus "-" plus ISO 15924 code of the language/script pair that should be loaded
    :param preproc bool: apply preprocessors
    :param postproc bool:  apply postprocessors
    :param ligatures bool: use precomposed ligatures instead of standard IPA
    :param cedict_filename str: path to file containing the CC-CEDict dictionary
    :param rev boolean: use reverse transliteration
    :param rev_preproc bool: if True, apply preprocessors when reverse transliterating
    :param rev_postproc bool: if True, apply postprocessors when reverse transliterating 
    """
    special = {'eng-Latn': FliteLexLookup,
               'cmn-Hans': Epihan,
               'cmn-Hant': EpihanTraditional}

    def __init__(self, code: str, preproc: bool=True, postproc: bool=True, ligatures: bool=False,
                cedict_file: Union[bool, None]=None, rev: bool=False, 
                rev_preproc: bool=True, rev_postproc: bool=True, tones: bool=False):
        """Constructor method"""
        if code in self.special:
            self.epi = self.special[code](ligatures=ligatures, cedict_file=cedict_file, tones=tones)
        else:
            self.epi = SimpleEpitran(code, preproc, postproc, ligatures, rev, rev_preproc, rev_postproc, tones=tones)
        self.ft = panphon.featuretable.FeatureTable()
        self.xsampa = XSampa()
        self.puncnorm = PuncNorm()

    def transliterate(self, word: str, normpunc: bool=False, ligatures: bool=False) -> str:
        """Transliterates/transcribes a word into IPA

        :param word str: word to transcribe
        :param normpunc bool: if True, normalize punctuation
        :param ligatures bool: if True, use precomposed ligatures instead of standard IPA
        :return: An IPA string corresponding to the input orthographic string
        :rtype: str
        """
        return self.epi.transliterate(word, normpunc, ligatures)

    def reverse_transliterate(self, ipa: str) -> str:
        """Reconstructs word from IPA. Does the reverse of transliterate()

        :param ipa str: An IPA representation of a word
        :return: An orthographic representation of the word
        :rtype: str
        """
        return self.epi.reverse_transliterate(ipa)

    def strict_trans(self, word: str, normpunc:bool =False, ligatures: bool=False) -> str:
        """Transliterate a word into IPA, ignoring all characters that cannot be recognized.

        :param word str: word to transcribe
        :param normpunc bool, optional: if True, normalize punctuation
        :param ligatures bool, optional: if True, use precomposed ligatures instead of standard IPA
        :return: An IPA string corresponding to the input orthographic string, with all uncoverted characters omitted
        :rtype: str
        """
        return self.epi.strict_trans(word, normpunc, ligatures)

    def trans_list(self, word: str, normpunc: bool=False, ligatures: bool=False) -> "list[str]":
        """Transliterates/transcribes a word into list of IPA phonemes

        :param word str: word to transcribe
        :param normpunc bool, optional: if True, normalize punctuation
        :param ligatures bool, optional: if True, use precomposed ligatures instead of standard IPA
        :return: list of IPA strings, each corresponding to a segment
        :rtype: list[str]
        """
        return self.ft.segs_safe(self.epi.transliterate(word, normpunc, ligatures))

    def trans_delimiter(self, text: str, delimiter: str=str(' '), normpunc: bool=False, ligatures: bool=False):
        """Return IPA transliteration with a delimiter between segments

        :param text str: An orthographic text
        :param delimiter str, optional: A string to insert between segments
        :param normpunc bool, optional: If True, normalize punctuation
        :param ligatures bool, optional: If True, use precomposed ligatures instead of standard IPA
        :return: String of IPA phonemes separated by `delimiter`
        :rtype: str
        """
        return delimiter.join(self.trans_list(text, normpunc=normpunc,
                                              ligatures=ligatures))

    def xsampa_list(self, word: str, normpunc: bool=False, ligaturize: bool=False):
        """Transliterates/transcribes a word as X-SAMPA

        :param word str: An orthographic word
        :param normpunc bool, optional: If True, normalize punctuation
        :param ligatures bool, optional: If True, use precomposed ligatures instead of standard IPA
        :return: List of X-SAMPA strings corresponding to `word`
        :rtype: list[str]
        """
        ipa_segs = self.ft.ipa_segs(self.epi.strict_trans(word, normpunc,
                                                          ligaturize))
        return list(map(self.xsampa.ipa2xs, ipa_segs))

    def word_to_tuples(self, word: str, normpunc: bool=False, _ligaturize: bool=False):
        """Given a word, returns a list of tuples corresponding to IPA segments. The "feature
        vectors" form a list consisting of (segment, vector) pairs.
        For IPA segments, segment is a substring of phonetic_form such that the
        concatenation of all segments in the list is equal to the phonetic_form.
        The vectors are a sequence of integers drawn from the set {-1, 0, 1}
        where -1 corresponds to '-', 0 corresponds to '0', and 1 corresponds to
        '+'.

        :param word str: An orthographic word
        :param normpunc bool, optional: If True, normalize punctuation
        :param ligatures bool, optional: If True, use precomposed ligatures instead of standard IPA
        :return: A list of tuples corresponding to IPA segments
        :rtype: list[tuple[str, str, str, str, list[int]]]
        """
        try:
            return self.epi.word_to_tuples(word, normpunc)
        except AttributeError:
            raise AttributeError('Method word_to_tuples not yet implemented for this language-script pair!') from AttributeError
