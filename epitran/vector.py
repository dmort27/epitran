from _epitran import Epitran
import os.path
import pkg_resources
import unicodecsv as csv


class VectorWithIPASpace(object):
    def __init__(self, code, space_name):
        self.epi = Epitran(code)
        self.space = self._load_space(space_name)

    def _load_space(self, space_name):
        space_fn = os.path.join('data', space_name + '.csv')
        space_fn = pkg_resources.resource_filename(__name__, space_fn)
        with open(space_fn, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            return {seg: num for (num, seg) in reader}

    def word_to_pfvecter(self, word):
        """Returns feature vectors, etc. for segments and punctuation in a word.

        word -- Unicode string representing a word in the orthography specified
                when the class is instantiated.
        return -- a list of tuples, each representing an IPA segment or a
                  punctuation character. Tuples consist of <category, lettercase,
                  orthographic_form, phonetic_form, feature_vector>.
        """
        segs = self.epi.plus_vector_tuples(word)
        new_segs = []
        for case, cat, orth, phon, vec in segs:
            if phon:
                id_ = self.space[phon]
            else:
                if orth in self.epi.puncnorm:
                    orth = self.epi.puncnorm[orth]
                id_ = self.space[orth]
            new_segs.append((cat, case, orth, phon, id_, vec))
        return new_segs
