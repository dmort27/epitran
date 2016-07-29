from __future__ import print_function

import os.path
import sys
from unicodedata import normalize

import pkg_resources

import epitran
import unicodecsv as csv


class ReRomanizer(object):
    def __init__(self, code, table, decompose=False):
        self.epi = epitran.Epitran(code)
        self.mapping = self._load_reromanizer(table, decompose)

    def _load_reromanizer(self, table, decompose):
        path = os.path.join('data', 'reromanize', table + '.csv')
        try:
            path = pkg_resources.resource_filename(__name__, path)
        except:
            print('Could not locate {}.'.format(path), file=sys.stderr)
        if os.path.isfile(path):
            mapping = {}
            with open(path, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                next(reader)
                for ipa, rom in reader:
                    rom = normalize('NFD', rom) if decompose else normalize('NFC', rom)
                    mapping[ipa] = rom
            return mapping
        else:
            print('File {} does not exist.'.format(path), file=sys.stderr)
            return {}

    def reromanize_ipa(self, tr_list):
        re_rom_list = []
        for seg in tr_list:
            if seg in self.mapping:
                re_rom_list.append(self.mapping[seg])
            else:
                re_rom_list.append(seg)
        return re_rom_list

    def reromanize(self, text):
        tr_list = self.epi.trans_list(text)
        return ''.join(self.reromanize_ipa(tr_list))
