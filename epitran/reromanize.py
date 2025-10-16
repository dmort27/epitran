
import os.path
import sys
from unicodedata import normalize
from typing import Dict, List, Optional

from importlib import resources

import epitran
import csv


class ReRomanizer(object):
    """Converts IPA representations to a readable roman form."""

    def __init__(self, code: str, table: str, decompose: bool = True, cedict_file: Optional[str] = None) -> None:
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

    def _load_reromanizer(self, table: str, decompose: bool) -> Dict[str, str]:
        path_str = os.path.join('data', 'reromanize', table + '.csv')
        path = resources.files(__package__).joinpath(path_str)
        if path.is_file():
            mapping = {}
            with path.open('r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                for ipa, rom in reader:
                    rom = normalize('NFD', rom) if decompose else normalize('NFC', rom)
                    mapping[ipa] = rom
            return mapping
        else:
            print('File {} does not exist.'.format(path), file=sys.stderr)
            return {}

    def reromanize_ipa(self, tr_list: List[str]) -> List[str]:
        re_rom_list = []
        for seg in tr_list:
            if seg in self.mapping:
                re_rom_list.append(self.mapping[seg])
            else:
                re_rom_list.append(seg)
        return re_rom_list

    def reromanize(self, text: str) -> str:
        """Convert orthographic text to romanized text

        Arg:
            text (str): orthographic text

        Returns:
            str: romanized text
        """
        tr_list = self.epi.trans_list(text)
        return ''.join(self.reromanize_ipa(tr_list))
