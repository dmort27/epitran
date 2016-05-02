import os.path

import pkg_resources

import unicodecsv as csv
from _epitran import Epitran


class VectorsWithIPASpace(object):
    def __init__(self, code, space_name):
        self.epi = Epitran(code)
        self.space = self._load_space(space_name)

    def _load_space(self, space_name):
        space_fn = os.path.join('data', 'space', space_name + '.csv')
        space_fn = pkg_resources.resource_filename(__name__, space_fn)
        with open(space_fn, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            return {seg: num for (num, seg) in reader}

    def word_to_segs(self, word, normpunc=False):
        """Returns feature vectors, etc. for segments and punctuation in a word.

        word -- Unicode string representing a word in the orthography specified
                when the class is instantiated.
        return -- a list of tuples, each representing an IPA segment or a
                  punctuation character. Tuples consist of <category, lettercase,
                  orthographic_form, phonetic_form, feature_vector>.

        Category consists of the standard Unicode classes (e.g. 'L' for letter
        and 'P' for punctuation). Case is binary: 1 for uppercase and 0 for
        lowercase.
        """

        segs = self.epi.word_to_tuples(word, normpunc)
        new_segs = []
        for cat, case, orth, phon, id_vec_list in segs:
            if not phon and normpunc:
                if orth in self.epi.puncnorm:
                    orth = self.epi.puncnorm[orth]
            for s, vector in id_vec_list:
                if s in self.space:
                    id_ = self.space[s]
                elif orth in self.space:
                    id_ = self.space[orth]
                else:
                    id_ = -1
                new_segs.append((cat, case, orth, phon, id_, vector))
        return new_segs
