from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import logging
import os.path
import unicodedata

import pkg_resources

from epitran.rules import Rules

logging.basicConfig(level=logging.DEBUG)


class PrePostProcessor(object):
    def __init__(self, code, fix):
        """Constructs a pre/post-processor for orthographic/IPA strings

        This class reads processor files consisting of context-sensitive rules
        and compiles them into regular expression objects that can then be used
        to perform regex replacements in cascades that capture feeding and
        bleeding.

        Args:
            code (str): ISO 639-3 code and ISO 15924 code joined with a hyphen
            fix (str): 'pre' for preprocessors, 'post' for postprocessors
        """
        self.rules = self._read_rules(code, fix)

    def _read_rules(self, code, fix):
        assert fix in ['pre', 'post']
        fn = os.path.join('data', fix, code + '.txt')
        try:
            abs_fn = pkg_resources.resource_filename(__name__, fn)
        except KeyError:
            return Rules([])
        if os.path.isfile(abs_fn):
            return Rules([abs_fn])
        else:
            return Rules([])

    def process(self, word):
        """Apply processor to an input string

        Args:
            word (unicode): input string (orthographic or IPA)

        Returns:
            unicode: output string with all rules applied in order
        """
        word = unicodedata.normalize('NFC', word)
        return self.rules.apply(word)
