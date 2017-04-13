from __future__ import print_function, unicode_literals, division, absolute_import
import os.path
from types import ListType, StringTypes

import pkg_resources

import unicodecsv as csv
from epitran import Epitran


class VectorsWithIPASpace(object):
    def __init__(self, code, space_name):
        self.epi = Epitran(code)
        # This (singelton) usage is Deprectated.
        if isinstance(space_name, StringTypes):
            self.space = self._load_single_space(space_name)
        elif isinstance(space_name, ListType):
            self.space = self._load_union_space(space_name)
        else:
            raise TypeError('Argument space_name must be string or list.')

    def _load_single_space(self, space_name):
        # Deprectated.
        space_fn = os.path.join('data', 'space', space_name + '.csv')
        space_fn = pkg_resources.resource_filename(__name__, space_fn)
        with open(space_fn, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            return {seg: num for (num, seg) in reader}

    def _load_union_space(self, space_names):
        segs = set()
        scripts = [nm.split('-')[1] for nm in space_names]
        punc_fns = ['punc-{}.csv'.format(sc) for sc in scripts]
        for punc_fn in punc_fns:
            punc_fn = os.path.join('data', 'space', punc_fn)
            punc_fn = pkg_resources.resource_filename(__name__, punc_fn)
            with open(punc_fn, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                for (mark,) in reader:
                    segs.add(mark)
        for name in space_names:
            fn = os.path.join('data', name + '.csv')
            fn = pkg_resources.resource_filename(__name__, fn)
            with open(fn, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                for _, to_ in reader:
                    for seg in self.epi.ft.segs(to_):
                        segs.add(seg)
        enum = enumerate(sorted(list(segs)))
        return {seg: num for num, seg in enum}

    def _load_union_space_ternary(self, space_names):

        def recode_ft(ft):
            val2trn = {'+': '2', '0': '1', '-': '0'}
            try:
                return val2trn[ft]
            except KeyError:
                raise ValueError("Feature values must be '+', '-', or '0'.")

        def vec2ternary(vec):
            return ''.join(map(recode_ft, vec))

        def to_int(seg):
            return int(vec2ternary(self.epi.ft.segment_to_vector(seg)), base=3)

        segs = {}
        for name in space_names:
            fn = os.path.join('data', name + '.csv')
            fn = pkg_resources.resource_filename(__name__, fn)
            with open(fn, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                for _, to_ in reader:
                    for seg in self.epi.ft.segs(to_):
                        segs[seg] = to_int(seg)
        return segs

    def word_to_segs(self, word, normpunc=False):
        """Returns feature vectors, etc. for segments and punctuation in a word.

        Args:
            word (unicode): Unicode string representing a word in the
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
        new_segs = []
        for cat, case, orth, phon, id_vec_list in segs:
            if not phon and normpunc:
                if orth in self.epi.puncnorm:
                    orth = self.epi.puncnorm[orth]
            for s, vector in id_vec_list:
                if s in self.space:
                    id_ = int(self.space[s])
                elif orth in self.space:
                    id_ = int(self.space[orth])
                else:
                    id_ = -1
                new_segs.append((cat, case, orth, phon, id_, vector))
        return new_segs
