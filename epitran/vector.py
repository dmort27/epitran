
import logging
from typing import List, Tuple, Optional, cast

from epitran import Epitran
from epitran.space import Space

logger = logging.getLogger('epitran')


class VectorsWithIPASpace(object):
    def __init__(self, code: str, space_names: List[str]) -> None:
        """Constructs VectorWithIPASpace object

        A VectorWithIPASpace object takes orthographic words, via the
        word_to_segs method, and returns a list of tuples consisting of category
        (letter or punctuation), lettercaase, orthographic form, phonetic form,
        id within an IPA space, and articulatory feature vector.

        Args:
            code (str): ISO 639-3 code joined to ISO 15924 code with "-"
            space_names (list): list of space names consisting of ISO 639-3
                                codes joined to ISO 15924 codes with "-"
        """
        self.epi = Epitran(code)
        self.space = Space(code, space_names)

    def word_to_segs(self, word: str, normpunc: bool = False) -> List[Tuple[str, int, str, str, int, List[Optional[int]]]]:
        """Returns feature vectors, etc. for segments and punctuation in a word

        Args:
            word (str): Unicode string representing a word in the
                            orthography specified when the class is
                            instantiated
            normpunc (bool): normalize punctuation

        Returns:
            list: a list of tuples, each representing an IPA segment or a
                  punctuation character. Tuples consist of <category, lettercase,
                  orthographic_form, phonetic_form, id, feature_vector>.

                  Category consists of the standard Unicode classes (e.g. 'L'
                  for letter and 'P' for punctuation). Case is binary: 1 for
                  uppercase and 0 for lowercase.
        """
        segs = self.epi.word_to_tuples(word, normpunc)
        new_segs: List[Tuple[str, int, str, str, int, List[Optional[int]]]] = []
        for cat, case, orth, phon, id_vec_list in segs:
            if not phon and normpunc:
                if orth in self.epi.puncnorm:
                    orth = self.epi.puncnorm[orth]
            for s, vector in id_vec_list:
                vector_typed = cast(List[Optional[int]], vector)
                if s in self.space:
                    id_ = int(self.space[s])
                elif orth in self.space:
                    id_ = int(self.space[orth])
                else:
                    id_ = -1
                new_segs.append((cat, case, orth, phon, id_, vector_typed))
        return new_segs
