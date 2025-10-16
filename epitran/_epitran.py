# -*- coding: utf-8 -*-
import logging

import panphon.featuretable
from epitran.epihan import Epihan, EpihanTraditional, EpiJpan, EpiCanto
from epitran.flite import FliteLexLookup
from epitran.puncnorm import PuncNorm
from epitran.simple import SimpleEpitran
from epitran.xsampa import XSampa

logger = logging.getLogger('epitran')
logger.setLevel(logging.WARNING)

class Epitran(object):
    """Unified interface for IPA transliteration/transcription.

    Parameters
    ----------
    code : str
        ISO 639-3 plus "-" plus ISO 15924 code of the language/script pair 
        that should be loaded.
    preproc : bool, optional
        Apply preprocessors. Default is True.
    postproc : bool, optional
        Apply postprocessors. Default is True.
    ligatures : bool, optional
        Use precomposed ligatures instead of standard IPA. Default is False.
    cedict_file : str or None, optional
        Path to file containing the CC-CEDict dictionary. Default is None.
    rev : bool, optional
        Use reverse transliteration. Default is False.
    rev_preproc : bool, optional
        If True, apply preprocessors when reverse transliterating. Default is True.
    rev_postproc : bool, optional
        If True, apply postprocessors when reverse transliterating. Default is True.
    tones : bool, optional
        Handle tone information. Default is False.
    """
    @final
    special = {'eng-Latn': FliteLexLookup,
               'cmn-Hans': Epihan,
               'cmn-Hant': EpihanTraditional,
               'jpn-Jpan': EpiJpan,
               'yue-Hant': EpiCanto,
               }

    def __init__(self, code: str, preproc: bool=True, postproc: bool=True, ligatures: bool=False,
                cedict_file: Union[bool, None]=None, rev: bool=False, 
                rev_preproc: bool=True, rev_postproc: bool=True, tones: bool=False):
        """Initialize Epitran transliterator.

        Parameters
        ----------
        code : str
            ISO 639-3 plus "-" plus ISO 15924 code of the language/script pair.
        preproc : bool, optional
            Apply preprocessors. Default is True.
        postproc : bool, optional
            Apply postprocessors. Default is True.
        ligatures : bool, optional
            Use precomposed ligatures instead of standard IPA. Default is False.
        cedict_file : bool or None, optional
            Path to CC-CEDict dictionary file. Default is None.
        rev : bool, optional
            Use reverse transliteration. Default is False.
        rev_preproc : bool, optional
            Apply preprocessors when reverse transliterating. Default is True.
        rev_postproc : bool, optional
            Apply postprocessors when reverse transliterating. Default is True.
        tones : bool, optional
            Handle tone information. Default is False.
        """
        if code in self.special:
            self.epi = self.special[code](**kwargs)
        else:
            self.epi = SimpleEpitran(code, **kwargs)
        self.ft = panphon.featuretable.FeatureTable()
        self.xsampa = XSampa()
        self.puncnorm = PuncNorm()

    def transliterate(self, word: str, normpunc: bool=False, ligatures: bool=False) -> str:
        """Transliterate/transcribe a word into IPA.

        Parameters
        ----------
        word : str
            Word to transcribe.
        normpunc : bool, optional
            If True, normalize punctuation. Default is False.
        ligatures : bool, optional
            If True, use precomposed ligatures instead of standard IPA. 
            Default is False.

        Returns
        -------
        str
            An IPA string corresponding to the input orthographic string.
        """
        return self.epi.transliterate(word, normpunc, ligatures)

    def reverse_transliterate(self, ipa: str) -> str:
        """Reconstruct word from IPA. Does the reverse of transliterate().

        Parameters
        ----------
        ipa : str
            An IPA representation of a word.

        Returns
        -------
        str
            An orthographic representation of the word.
        """
        return self.epi.reverse_transliterate(ipa)

    def strict_trans(self, word: str, normpunc:bool =False, ligatures: bool=False) -> str:
        """Transliterate a word into IPA, ignoring unrecognized characters.

        Parameters
        ----------
        word : str
            Word to transcribe.
        normpunc : bool, optional
            If True, normalize punctuation. Default is False.
        ligatures : bool, optional
            If True, use precomposed ligatures instead of standard IPA. 
            Default is False.

        Returns
        -------
        str
            An IPA string corresponding to the input orthographic string, 
            with all unconverted characters omitted.
        """
        return self.epi.strict_trans(word, normpunc, ligatures)

    def trans_list(self, word: str, normpunc: bool=False, ligatures: bool=False) -> "list[str]":
        """Transliterate/transcribe a word into list of IPA phonemes.

        Parameters
        ----------
        word : str
            Word to transcribe.
        normpunc : bool, optional
            If True, normalize punctuation. Default is False.
        ligatures : bool, optional
            If True, use precomposed ligatures instead of standard IPA. 
            Default is False.

        Returns
        -------
        list of str
            List of IPA strings, each corresponding to a segment.
        """
        return self.ft.segs_safe(self.epi.transliterate(word, normpunc, ligatures))

    def trans_delimiter(self, text: str, delimiter: str=str(' '), normpunc: bool=False, ligatures: bool=False):
        """Return IPA transliteration with a delimiter between segments.

        Parameters
        ----------
        text : str
            An orthographic text.
        delimiter : str, optional
            A string to insert between segments. Default is ' '.
        normpunc : bool, optional
            If True, normalize punctuation. Default is False.
        ligatures : bool, optional
            If True, use precomposed ligatures instead of standard IPA. 
            Default is False.

        Returns
        -------
        str
            String of IPA phonemes separated by `delimiter`.
        """
        return delimiter.join(self.trans_list(text, normpunc=normpunc,
                                              ligatures=ligatures))

    def xsampa_list(self, word: str, normpunc: bool=False, ligaturize: bool=False):
        """Transliterate/transcribe a word as X-SAMPA.

        Parameters
        ----------
        word : str
            An orthographic word.
        normpunc : bool, optional
            If True, normalize punctuation. Default is False.
        ligaturize : bool, optional
            If True, use precomposed ligatures instead of standard IPA. 
            Default is False.

        Returns
        -------
        list of str
            List of X-SAMPA strings corresponding to `word`.
        """
        ipa_segs = self.ft.ipa_segs(self.epi.strict_trans(word, normpunc,
                                                          ligaturize))
        return list(map(self.xsampa.ipa2xs, ipa_segs))

    def word_to_tuples(self, word: str, normpunc: bool=False, _ligaturize: bool=False):
        """Convert a word to a list of tuples corresponding to IPA segments.

        The "feature vectors" form a list consisting of (segment, vector) pairs.
        For IPA segments, segment is a substring of phonetic_form such that the
        concatenation of all segments in the list is equal to the phonetic_form.
        The vectors are a sequence of integers drawn from the set {-1, 0, 1}
        where -1 corresponds to '-', 0 corresponds to '0', and 1 corresponds to '+'.

        Parameters
        ----------
        word : str
            An orthographic word.
        normpunc : bool, optional
            If True, normalize punctuation. Default is False.
        _ligaturize : bool, optional
            If True, use precomposed ligatures instead of standard IPA. 
            Default is False.

        Returns
        -------
        list of tuple
            A list of tuples corresponding to IPA segments.

        Raises
        ------
        AttributeError
            If method is not implemented for this language-script pair.
        """
        try:
            return self.epi.word_to_tuples(word, normpunc)
        except AttributeError:
            raise AttributeError('Method word_to_tuples not yet implemented for this language-script pair!') from AttributeError
