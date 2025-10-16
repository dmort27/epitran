"""Basic Epitran class for G2P in most languages."""
import logging
import os.path
import sys
import csv
import unicodedata
from collections import defaultdict
from typing import DefaultDict, Callable, Any

from importlib import resources
import regex

import panphon
from jamo import h2j, j2hcj
from epitran.exceptions import DatafileError, MappingError, FeatureValueError
from epitran.ligaturize import ligaturize
from epitran.ppprocessor import PrePostProcessor
from epitran.puncnorm import PuncNorm
from epitran.stripdiacritics import StripDiacritics

logger = logging.getLogger('epitran')


class SimpleEpitran(object):
    """The backend object epitran uses for most languages.

    Parameters
    ----------
    code : str
        ISO 639-3 code and ISO 15924 code joined with a hyphen.
    preproc : bool, optional
        If True, apply preprocessor. Default is True.
    postproc : bool, optional
        If True, apply postprocessors. Default is True.
    ligatures : bool, optional
        If True, use phonetic ligatures for affricates instead of standard IPA. 
        Default is False.
    rev : bool, optional
        If True, load reverse transliteration. Default is False.
    rev_preproc : bool, optional
        If True, apply preprocessor when reverse transliterating. Default is True.
    rev_postproc : bool, optional
        If True, apply postprocessor when reverse transliterating. Default is True.
    tones : bool, optional
        Handle tone information. Default is False.
    """

    def __init__(self, code: str, preproc: bool = True, postproc: bool = True, ligatures: bool = False,
                 rev: bool = False, rev_preproc: bool = True, rev_postproc: bool = True, tones: bool = False):
        """Initialize SimpleEpitran transliterator.

        Parameters
        ----------
        code : str
            ISO 639-3 code and ISO 15924 code joined with a hyphen.
        preproc : bool, optional
            If True, apply preprocessor. Default is True.
        postproc : bool, optional
            If True, apply postprocessors. Default is True.
        ligatures : bool, optional
            If True, use phonetic ligatures for affricates instead of standard IPA. 
            Default is False.
        rev : bool, optional
            If True, load reverse transliteration. Default is False.
        rev_preproc : bool, optional
            If True, apply preprocessor when reverse transliterating. Default is True.
        rev_postproc : bool, optional
            If True, apply postprocessor when reverse transliterating. Default is True.
        tones : bool, optional
            Handle tone information. Default is False.
        """
        self.rev = rev
        self.tones = tones
        self.g2p = self._load_g2p_map(code, False)
        self.regexp = self._construct_regex(self.g2p.keys())
        self.puncnorm = PuncNorm()
        self.ft = panphon.FeatureTable()
        self.num_panphon_fts = len(self.ft.names)
        self.preprocessor = PrePostProcessor(code, 'pre', False)
        self.postprocessor = PrePostProcessor(code, 'post', False)
        self.strip_diacritics = StripDiacritics(code)
        self.preproc = preproc
        self.postproc = postproc
        self.ligatures = ligatures
        self.rev_preproc = rev_preproc
        self.rev_postproc = rev_postproc
        if rev:
            self.rev_g2p = self._load_g2p_map(code, True)
            self.rev_regexp = self._construct_regex(self.rev_g2p.keys())
            self.rev_preprocessor = PrePostProcessor(code, 'pre', True)
            self.rev_postprocessor = PrePostProcessor(code, 'post', True)

        self.nils: "defaultdict[str, int]" = defaultdict(int)

    def get_tones(self) -> bool:
        """Returns True if support for tones is turned on.

        :return: True if tone support is activated
        :rtype: bool
        """
        return self.tones

    def __enter__(self) -> "SimpleEpitran":
        return self

    def __exit__(self, _type_: Any, _val: Any, _trace_back: Any) -> None:
        for nil, count in self.nils.items():
            sys.stderr.write(
                f'Unknown character "{nil}" occured {count} times.\n')

    # def _one_to_many_gr_by_line_map(self, gr_by_line: "dict[str, list[int]]") -> "tuple[str, list[int]]":
    #     for g, ls in gr_by_line.items():
    #         if len(ls) > 0:
    #             return (g, ls)
    #     return ("", [])

    def _non_deterministic_mappings(self, gr_by_line: "dict[str, list[int]]") -> "list[tuple[str, list[int]]]":
        return [(g, ls) for (g, ls) in gr_by_line.items() if len(ls) > 1]

    def _load_g2p_map(self, code: str, rev: bool) -> "DefaultDict[str, list[str]]":
        """Load the code table for the specified language.

        Parameters
        ----------
        code : str
            ISO 639-3 code plus "-" plus ISO 15924 code for the language/script 
            to be loaded.
        rev : bool
            If True, reverse the table (for reverse transliterating).

        Returns
        -------
        DefaultDict[str, list[str]]
            A mapping from graphemes to phonemes.

        Raises
        ------
        DatafileError
            If appropriately-named mapping is not found in data/maps directory.
        """
        g2p = defaultdict(list)
        gr_by_line = defaultdict(list)
        code += '_rev' if rev else ''
        try:
            path = os.path.join('data', 'map', code + '.csv')
            with resources.files(__package__).joinpath(path).open(encoding='utf-8') as f:
                reader = csv.reader(f)
                orth, phon = next(reader)
                if orth != 'Orth' or phon != 'Phon':
                    raise DatafileError(
                        f'Header is ["{orth}", "{phon}"] instead of ["Orth", "Phon"].')
                for (i, fields) in enumerate(reader):
                    try:
                        graph, phon = fields
                    except ValueError as malformed_data_file:
                        raise DatafileError(
                            f'Map file is not well formed at line {i + 2}.') from malformed_data_file
                    graph = unicodedata.normalize('NFD', graph)
                    phon = unicodedata.normalize('NFD', phon)
                    if not self.tones:
                        phon = regex.sub('[˩˨˧˦˥]', '', phon)
                    g2p[graph].append(phon)
                    gr_by_line[graph].append(i)
        except (FileNotFoundError, IndexError) as malformed_data_file:
            raise DatafileError(
                'Add an appropriately-named mapping to the data/maps directory.') from malformed_data_file
        nondeterminisms = self._non_deterministic_mappings(gr_by_line)
        if nondeterminisms:
            message = ""
            for graph, lines in nondeterminisms:
                lines = [line + 2 for line in lines]
                delim = ', '
                message += '\n' + \
                    f'One-to-many G2P mapping for "{graph}" on lines {delim.join(map(str, lines))}'
            raise MappingError(f'Invalid mapping for {code}:\n{message}')
        return g2p

    def _load_punc_norm_map(self) -> "dict[str, str]":
        """Load the map table for normalizing 'down' punctuation."""
        path = os.path.join('data', 'puncnorm.csv')
        with resources.files(__package__).joinpath(path).open(encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            next(reader)
            return {punc: norm for (punc, norm) in reader}

    def _construct_regex(self, g2p_keys: Any) -> Any:
        """Build a regular expression that will greadily match segments from
           the mapping table.
        """
        graphemes = sorted(g2p_keys, key=len, reverse=True)
        return regex.compile(f"({r'|'.join(graphemes)})", regex.I)

    def general_trans(self, text: str, filter_func: "Callable[[tuple[str, bool]], bool]",
                      normpunc: bool = False, ligatures: bool = False):
        """Transliterate a word into IPA, filtering with filter_func.

        Parameters
        ----------
        text : str
            Word to transcribe.
        filter_func : Callable[[tuple[str, bool]], bool]
            Function for filtering segments; takes a <segment, is_ipa> tuple 
            and returns a boolean.
        normpunc : bool, optional
            Normalize punctuation. Default is False.
        ligatures : bool, optional
            Use precomposed ligatures instead of standard IPA. Default is False.

        Returns
        -------
        str
            IPA string corresponding to the orthographic input `text`.
        """
        text = unicodedata.normalize('NFD', text.lower())
        logger.debug('(after norm) text=%s', repr(list(text)))
        text = self.strip_diacritics.process(text)
        logger.debug('(after strip) text=%s', repr(list(text)))
        if self.preproc:
            text = self.preprocessor.process(text)
        logger.debug('(after preproc) text=%s', repr(list(text)))
        tr_list = []
        while text:
            logger.debug('text=%s', repr(list(text)))
            m = self.regexp.match(text)
            if m:
                source = m.group(0)
                try:
                    target = self.g2p[source][0]
                except KeyError:
                    logger.debug("source = '%s''", source)
                    logger.debug("self.g2p[source] = %s'", self.g2p[source])
                    target = source
                except IndexError:
                    logger.debug("self.g2p[source]= %s", self.g2p[source])
                    target = source
                tr_list.append((target, True))
                text = text[len(source):]
            else:
                tr_list.append((text[0], False))
                self.nils[text[0]] += 2
                text = text[1:]
        text = ''.join([s for (s, _) in filter(filter_func, tr_list)])
        if self.postproc:
            text = self.postprocessor.process(text)
        if ligatures or self.ligatures:
            text = ligaturize(text)
        if normpunc:
            text = self.puncnorm.norm(text)
        return unicodedata.normalize('NFC', text)

    # Korean exception handling in transliterate
    def is_korean(self, text: str) -> bool:
        """Check if the text contains any Korean characters."""
        for char in text:
            if '\uAC00' <= char <= '\uD7A3':  # Checking Korean Unicode
                return True
        return False

    def transliterate(self, text: str, normpunc: bool = False, ligatures: bool = False):
        """Transliterate/transcribe a word into IPA.
        
        Passes unmapped characters through to output unchanged.

        Parameters
        ----------
        text : str
            Word to transcribe.
        normpunc : bool, optional
            If True, normalize punctuation. Default is False.
        ligatures : bool, optional
            If True, use precomposed ligatures instead of standard IPA. 
            Default is False.

        Returns
        -------
        str
            IPA string corresponding to the orthographic string `text`.
            All unrecognized characters are included.
        """
        try:
            if self.is_korean(text):
                text = j2hcj(h2j(text))
        except Exception as e:
            print(f"Error during Korean transliteration: {e}")

        return self.general_trans(text, lambda x: True,
                                  normpunc, ligatures)

    def general_reverse_trans(self, text: str):
        """Reconstruct word from IPA. Does the reverse of transliterate().
        
        Ignores unmapped characters.

        Parameters
        ----------
        text : str
            Transcription to render in orthography.

        Returns
        -------
        str
            Orthographic string corresponding to `text`.
        """
        if self.rev_preproc:
            text = self.rev_preprocessor.process(text)
        tr_list = []
        while text:
            m = self.rev_regexp.match(text)
            if m:
                source = m.group(0)
                try:
                    target = self.rev_g2p[source][0]
                except KeyError:
                    logger.debug("source = '%s'", source)
                    logger.debug(
                        "self.rev_g2p[source] = '%s'", self.g2p[source])
                    target = source
                tr_list.append((target, True))
                text = text[len(source):]
            else:
                tr_list.append((text[0], False))
                self.nils[text[0]] += 2
                text = text[1:]
        text = ''.join([s for (s, _) in tr_list])
        if self.rev_postproc:
            text = self.rev_postprocessor.process(text)
        return unicodedata.normalize('NFC', text)

    def reverse_transliterate(self, ipa: str) -> str:
        """Reconstruct word from IPA. Does the reverse of transliterate().

        Parameters
        ----------
        ipa : str
            Word transcription in IPA.

        Returns
        -------
        str
            Reconstructed word in orthography.

        Raises
        ------
        ValueError
            If this Epitran object was initialized with no reverse 
            transliteration loaded.
        """
        if not self.rev:
            raise ValueError('This Epitran object was initialized' +
                             'with no reverse transliteration loaded')
        return self.general_reverse_trans(ipa)

    def strict_trans(self, text: str, normpunc: bool = False, ligatures: bool = False) -> str:
        """Transliterate/transcribe a word into IPA, ignoring unmapped characters.

        Parameters
        ----------
        text : str
            Word to transcribe.
        normpunc : bool, optional
            Normalize punctuation. Default is False.
        ligatures : bool, optional
            Use precomposed ligatures instead of standard IPA. Default is False.

        Returns
        -------
        str
            IPA string corresponding to orthographic `text`, ignoring 
            out-of-mapping characters.
        """
        return self.general_trans(text, lambda x: x[1],
                                  normpunc, ligatures)

    def word_to_tuples(self, text: str, normpunc: bool = False) -> "list[tuple[str, int, str, str, list[tuple[str, list[int]]]]]":
        """Convert a word to a list of tuples corresponding to IPA segments.

        The "feature vectors" form a list consisting of (segment, vector)
        pairs. For IPA segments, segment is a substring of phonetic_form such
        that the concatenation of all segments in the list is equal to
        the phonetic_form. The vectors are a sequence of integers drawn from
        the set {-1, 0, 1} where -1 corresponds to '-', 0 corresponds to '0',
        and 1 corresponds to '+'.

        Parameters
        ----------
        text : str
            Word to transcribe.
        normpunc : bool, optional
            Normalize punctuation. Default is False.

        Returns
        -------
        list of tuple
            Word represented as (category, lettercase, orthographic_form,
            phonetic_form, feature_vectors) tuples.
        """
        def cat_and_cap(category: str) -> "tuple[str, int]":
            cat, case_char = tuple(unicodedata.category(category))
            case = 1 if case_char == 'u' else 0
            return cat, case

        def recode_ft(feature: str) -> int:
            try:
                return {'+': 1, '0': 0, '-': -1}[feature]
            except KeyError:
                raise FeatureValueError(
                    f'Unknown feature value "{feature}"') from KeyError

        def vec2bin(vec: "list[str]") -> "list[int]":
            return list(map(recode_ft, vec))

        def to_vector(seg: str) -> "tuple[str, list[int]]":
            return seg, vec2bin(self.ft.segment_to_vector(seg))

        def to_vectors(phon: str) -> "list[tuple[str, list[int]]]":
            if phon == '':
                return [('', [0] * self.num_panphon_fts)]
            else:
                return [to_vector(seg) for seg in self.ft.ipa_segs(phon)]

        tuples = []
        word = self.strip_diacritics.process(text)
        word = unicodedata.normalize('NFD', word)
        if self.preproc:
            word = self.preprocessor.process(word)
        while word:
            match = self.regexp.match(word)
            if match:
                span: str = match.group(1)
                cat, case = cat_and_cap(span[0])
                phon: str = self.g2p[span.lower()][0]
                vecs: "list[tuple[str, list[int]]]" = to_vectors(phon)
                tuples.append(('L', case, span, phon, vecs))
                word = word[len(span):]
            else:
                span = word[0]
                span = self.puncnorm.norm(span) if normpunc else span
                cat, case = cat_and_cap(span)
                cat = 'P' if normpunc and cat in self.puncnorm else cat
                phon = ''
                vecs = to_vectors(phon)
                tuples.append((cat, case, span, phon, vecs))
                word = word[1:]
        return tuples

    def ipa_segs(self, ipa: str) -> "list[str]":
        """Decompose an IPA string into a list of segments.

        Parameters
        ----------
        ipa : str
            A phonetic representation in IPA.

        Returns
        -------
        list of str
            A list of words corresponding to the segments in `ipa`.
        """
        return self.ft.ipa_segs(ipa)
