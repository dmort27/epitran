
import logging
import unicodedata
from collections.abc import Callable
from pathlib import Path
from typing import Any

import regex as re

from epitran.exceptions import DatafileError

logger = logging.getLogger('epitran')


def none2str(x: str | None) -> str:
    return x if x else ''


class RuleFileError(Exception):
    pass


class Rules:
    def __init__(self, rule_files: list[str | Path]) -> None:
        """Construct an object encoding context-sensitive rules

        Args:
            rule_files (list): list of names of rule files or Path objects
        """
        self.rules: list[Callable[[str], str]] = []
        self.symbols: dict[str, str] = {}
        for rule_file in rule_files:
            rules = self._read_rule_file(rule_file)
            self.rules = self.rules + rules

    def _read_rule_file(self, rule_file: str | Path) -> list[Callable[[str], str]]:
        rules = []
        # Handle both string paths and importlib.resources Path objects
        if hasattr(rule_file, 'open'):
            # This is an importlib.resources Path object
            with rule_file.open('r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    # Normalize the line to decomposed form
                    line = line.strip()
                    line = unicodedata.normalize('NFD', line)
                    if not re.match(r'\s*%', line):
                        rules.append(self._read_rule(i, line))
        else:
            # This is a regular string path
            with open(rule_file, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    # Normalize the line to decomposed form
                    line = line.strip()
                    line = unicodedata.normalize('NFD', line)
                    if not re.match(r'\s*%', line):
                        rules.append(self._read_rule(i, line))
        return [rule for rule in rules if rule is not None]

    def _expand_symbol_references(self, line: str) -> str:
        """Replace ::symbol:: references with their defined values."""
        while re.search(r'::\w+::', line):
            s = re.search(r'::\w+::', line).group(0)
            if s in self.symbols:
                line = line.replace(s, self.symbols[s])
            else:
                raise RuleFileError(f'Undefined symbol: {s}')
        return line

    def _read_rule(self, i: int, line: str) -> Callable[[str], str] | None:
        line = line.strip()
        if line:
            line = unicodedata.normalize('NFD', line)
            s = re.match(r'(?P<symbol>::\w+::)\s*=\s*(?P<value>.+)', line)
            if s:
                self.symbols[s.group('symbol')] = s.group('value')
            else:
                line = self._expand_symbol_references(line)
                r = re.match(r'(\S+)\s*->\s*(\S+)\s*/\s*(\S*)\s*[_]\s*(\S*)', line)
                try:
                    a, b, X, Y = r.groups()
                except AttributeError:
                    raise DatafileError(f'Line {i + 1}: "{line}" cannot be parsed.')
                X, Y = X.replace('#', '^'), Y.replace('#', '$')
                a, b = a.replace('0', ''), b.replace('0', '')
                try:
                    if re.search(r'[?]P[<]sw1[>].+[?]P[<]sw2[>]', a):
                        return self._compile_metathesis_rule(a, X, Y)
                    else:
                        return self._compile_replacement_rule(a, b, X, Y)
                except Exception as e:
                    raise DatafileError(f'Line {i + 1}: "{line}" cannot be compiled as regex: ̪{e}')
        return None

    def _compile_metathesis_rule(self, a: str, X: str, Y: str) -> Callable[[str], str]:
        """Compile a metathesis (swap) rule: swap two captured groups within context."""
        left = rf'(?P<X>{X}){a}(?P<Y>{Y})'
        regexp = re.compile(left)

        def rewrite(m: Any) -> str:
            d = {k: none2str(v) for k, v in m.groupdict().items()}
            return '{}{}{}{}'.format(d['X'], d['sw2'], d['sw1'], d['Y'])

        return lambda w: regexp.sub(rewrite, w, re.U)

    def _compile_replacement_rule(self, a: str, b: str, X: str, Y: str) -> Callable[[str], str]:
        """Compile a context-sensitive replacement rule into a regex substitution."""
        left = rf'(?P<X>{X})(?P<a>{a})(?P<Y>{Y})'
        regexp = re.compile(left)

        def rewrite(m: Any) -> str:
            d = {k: none2str(v) for k, v in m.groupdict().items()}
            return '{}{}{}'.format(d['X'], b, d['Y'])

        return lambda w: regexp.sub(rewrite, w, re.U)

    def apply(self, text: str) -> str:
        """Apply rules to input text

        Args:
            text (str): input text (e.g. Pinyin)

        Returns:
            str: output text (e.g. IPA)
        """
        for i, rule in enumerate(self.rules):
            text = rule(text)
            # print(i, text)
        # return unicodedata.normalize('NFD', text)
        return text
