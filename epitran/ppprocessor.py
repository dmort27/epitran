
import logging
import os.path
from pathlib import Path

from importlib import resources

from epitran.rules import Rules

logging.basicConfig(level=logging.DEBUG)


class PrePostProcessor(object):
    def __init__(self, code: str, fix: str, rev: bool) -> None:
        """Constructs a pre/post-processor for orthographic/IPA strings

        This class reads processor files consisting of context-sensitive rules
        and compiles them into regular expression objects that can then be used
        to perform regex replacements in cascades that capture feeding and
        bleeding.

        Args:
            code (str): ISO 639-3 code and ISO 15924 code joined with a hyphen
            fix (str): 'pre' for preprocessors, 'post' for postprocessors
            rev (boolean): True for reverse transliterating pre/post-processors
        """
        self.rules = self._read_rules(code, fix, rev)

    def _read_rules(self, code: str, fix: str, rev: bool) -> Rules:
        assert fix in ['pre', 'post']
        code += '_rev' if rev else ''
        fn = os.path.join('data', fix, code + '.txt')
        try:
            resource_path = resources.files(__package__).joinpath(fn)
            if resource_path.is_file():
                return Rules([Path(str(resource_path))])
            else:
                return Rules([])
        except (KeyError, FileNotFoundError):
            return Rules([])

    def process(self, word: str) -> str:
        """Apply processor to an input string

        Args:
            word (str): input string (orthographic or IPA)

        Returns:
            str: output string with all rules applied in order
        """
        return self.rules.apply(word)
