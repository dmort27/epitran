from __future__ import print_command

from _epitran import *
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
        segs = self.epi.word_to_pfvector(word)
        new_segs = []
        for category, lettercase, phonetic_form, ipa_id, vector in segs:
            ipa_id = self.space[phonetic_form]
            new_segs.append((category,
                            letteracase,
                            phonetic_form,
                            ipa_id,
                            vector))
        return new_segs
