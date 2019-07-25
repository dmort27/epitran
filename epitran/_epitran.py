# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import logging
import sys

import panphon.featuretable
from epitran.epihan import Epihan, EpihanTraditional
from epitran.flite import FliteLexLookup
from epitran.puncnorm import PuncNorm
from epitran.simple import SimpleEpitran
from epitran.xsampa import XSampa

if sys.version_info[0] == 3:
    def unicode(x):
        return x

logging.disable(logging.DEBUG)

class Epitran(object):
    """Unified interface for IPA transliteration/transcription"""
    special = {'eng-Latn': FliteLexLookup,
               'cmn-Hans': Epihan,
               'cmn-Hant': EpihanTraditional}

    def __init__(self, code, preproc=True, postproc=True, ligatures=False, cedict_file=None,
                 rev=False, rev_preproc=True, rev_postproc=True):
        """Construct Epitran transliteration/transcription object

        Args:
            code (str): ISO 639-3 plus "-" plus ISO 15924 code of the
                        language/script pair that should be loaded
            preproc (bool): apply preprocessors
            postproc (bool): apply prostprocessors
            ligatures (bool): use precomposed ligatures instead of standard IPA
            cedict_filename (str): path to file containing the CC-CEDict
                                   dictionary; relevant only for Chinese
            rev (boolean): if True, load reverse transliteration
            rev_preproc (bool): if True, apply preprocessor when reverse transliterating
            rev_postproc (bool): if True, apply postprocessor when reverse transliterating
        """
        if code in self.special:
            self.epi = self.special[code](ligatures=ligatures, cedict_file=cedict_file)
        else:
            self.epi = SimpleEpitran(code, preproc, postproc, ligatures, rev, rev_preproc, rev_postproc)
        self.ft = panphon.featuretable.FeatureTable()
        self.xsampa = XSampa()
        self.puncnorm = PuncNorm()

    def transliterate(self, word, normpunc=False, ligatures=False):
        """Transliterates/transcribes a word into IPA

        Args:
            word (str): word to transcribe; unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            unicode: IPA string
        """
        return self.epi.transliterate(word, normpunc, ligatures)

    def reverse_transliterate(self, ipa):
        """Reconstructs word from IPA. Does the reverse of transliterate()

        Args:
            ipa (str): word transcription in ipa; unicode string

        Returns:
            unicode: reconstructed word
        """
        return self.epi.reverse_transliterate(ipa)

    def strict_trans(self, word, normpunc=False, ligatures=False):
        return self.epi.strict_trans(word, normpunc, ligatures)

    def trans_list(self, word, normpunc=False, ligatures=False):
        """Transliterates/transcribes a word into list of IPA phonemes

        Args:
            word (str): word to transcribe; unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            list: list of IPA strings, each corresponding to a segment
        """
        return self.ft.segs_safe(self.epi.transliterate(word, normpunc, ligatures))

    def trans_delimiter(self, text, delimiter=str(' '), normpunc=False, ligatures=False):
        """Return IPA transliteration with a delimiter between segments

        Args:
            text (unicode): orthographic text
            delimiter (str): string to insert between segments
            normpunc (bool): if True, normalize punctation down
            ligatures (bool): if True, use phonetic ligatures for affricates
                              instead of standard IPA
        Returns:
            unicode: transliteration with segments delimited by `delimiter`
        """
        return delimiter.join(self.trans_list(text, normpunc=normpunc,
                                              ligatures=ligatures))

    def xsampa_list(self, word, normpunc=False, ligaturize=False):
        """Transliterates/transcribes a word as X-SAMPA

        Args:
            word (str): word to transcribe; unicode string
            normpunc (bool): normalize punctuation
            ligatures (bool): use precomposed ligatures instead of standard IPA

        Returns:
            list: X-SAMPA strings, each corresponding to a segment
        """
        ipa_segs = self.ft.ipa_segs(self.epi.strict_trans(word, normpunc,
                                                          ligaturize))
        return list(map(self.xsampa.ipa2xs, ipa_segs))

    def word_to_tuples(self, word, normpunc=False, ligaturize=False):
        """Given a word, returns a list of tuples corresponding to IPA segments.

        Args:
            word (unicode): word to transliterate
            normpunc (bool): If True, normalizes punctuation to ASCII inventory

        Returns:
        list: A list of (category, lettercase, orthographic_form, phonetic_form,
              fecture_vectors) tuples.

        The "feature vectors" form a list consisting of (segment, vector) pairs.
        For IPA segments, segment is a substring of phonetic_form such that the
        concatenation of all segments in the list is equal to the phonetic_form.
        The vectors are a sequence of integers drawn from the set {-1, 0, 1}
        where -1 corresponds to '-', 0 corresponds to '0', and 1 corresponds to
        '+'.
        """
        try:
            return self.epi.word_to_tuples(word, normpunc)
        except AttributeError:
            raise AttributeError('Method word_to_tuples not yet implemented for this language-script pair!')
