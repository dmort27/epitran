from __future__ import print_function, unicode_literals, division, absolute_import

import os.path
import sys
from unicodedata import normalize

import pkg_resources

import epitran
import unicodecsv as csv


class ReRomanizer(object):
    """Converts IPA representations to a readable roman form."""

    def __init__(self, code, table, decompose=True, cedict_file=None):
        """Construct object for re-romanizing Epitran output.

        This class converts orthographic input, via Epitran, to a more
        conventional romanization that should be more readable to most humans.

        Args:
            code (str): ISO 639-3 code and ISO 15924 code joined with a hyphen
            table (str): Name of re-romanization table
            decompose (bool): apply decomposing normalization
        """
        self.epi = epitran.Epitran(code, cedict_file=cedict_file)
        self.mapping = self._load_reromanizer(table, decompose)

    def _load_reromanizer(self, table, decompose):
        path = os.path.join('data', 'reromanize', table + '.csv')
        path = pkg_resources.resource_filename(__name__, path)
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
        """Convert orthographic text to romanized text

        Arg:
            text (unicode): orthographic text

        Returns:
            unicode: romanized text
        """
        tr_list = self.epi.trans_list(text)
        return ''.join(self.reromanize_ipa(tr_list))
