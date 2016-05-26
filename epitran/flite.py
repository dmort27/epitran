from __future__ import print_function, unicode_literals

import subprocess
import os.path
import unicodecsv as csv
import unicodedata
import string

import pkg_resources


class Flite(object):
    def __init__(self, darpabet='darpabet'):
        darpabet = pkg_resources.resource_filename(__name__, os.path.join('data', darpabet + '.csv'))
        self.darpa_map = self._read_darpabet(darpabet)

    def _read_darpabet(self, darpabet):
        darpa_map = {}
        with open(darpabet, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            for darpa, ipa in reader:
                darpa_map[darpa] = ipa
        return darpa_map

    def normalize(self, text):
        text = unicodedata.normalize('NFD', text)
        text = ''.join(filter(lambda x: x in string.printable, text))
        return text

    def darpa_to_ipa(self, darpa_text):
        darpa_text = darpa_text.strip()
        darpa_list = darpa_text.split(' ')[1:-1]  # remove pauses
        ipa_list = map(lambda d: self.darpa_map[d], darpa_list)
        return ''.join(ipa_list)

    def english_g2p(self, text):
        text = self.normalize(text)
        darpa_text = subprocess.check_output(['flite', '-ps', '-o', '/dev/null', '-t', '"{}"'.format(text)])
        return self.darpa_to_ipa(darpa_text)
