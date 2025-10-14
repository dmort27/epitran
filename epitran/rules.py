# -*- coding: utf-8 -*-

import io
import logging
import unicodedata
from typing import List, Dict, Optional, Callable, Any

import regex as re

from epitran.exceptions import DatafileError

logger = logging.getLogger('epitran')


def none2str(x: Optional[str]) -> str:
    return x if x else ''


class RuleFileError(Exception):
    pass


class Rules(object):
    def __init__(self, rule_files: List[str]) -> None:
        """Construct an object encoding context-sensitive rules

        Args:
            rule_files (list): list of names of rule files
        """
        self.rules: List[Callable[[str], str]] = []
        self.symbols: Dict[str, str] = {}
        for rule_file in rule_files:
            rules = self._read_rule_file(rule_file)
            self.rules = self.rules + rules

    def _read_rule_file(self, rule_file: str) -> List[Callable[[str], str]]:
        rules = []
        with io.open(rule_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                # Normalize the line to decomposed form
                line = line.strip()
                line = unicodedata.normalize('NFD', line)
                if not re.match(r'\s*%', line):
                    rules.append(self._read_rule(i, line))
        return [rule for rule in rules if rule is not None]

    def _sub_symbols(self, line: str) -> str:
        while re.search(r'::\w+::', line):
            s = re.search(r'::\w+::', line).group(0)
            if s in self.symbols:
                line = line.replace(s, self.symbols[s])
            else:
                raise RuleFileError('Undefined symbol: {}'.format(s))
        return line

    def _read_rule(self, i: int, line: str) -> Optional[Callable[[str], str]]:
        line = line.strip()
        if line:
            line = unicodedata.normalize('NFD', line)
            s = re.match(r'(?P<symbol>::\w+::)\s*=\s*(?P<value>.+)', line)
            if s:
                self.symbols[s.group('symbol')] = s.group('value')
            else:
                line = self._sub_symbols(line)
                r = re.match(r'(\S+)\s*->\s*(\S+)\s*/\s*(\S*)\s*[_]\s*(\S*)', line)
                try:
                    a, b, X, Y = r.groups()
                except AttributeError:
                    raise DatafileError('Line {}: "{}" cannot be parsed.'.format(i + 1, line))
                X, Y = X.replace('#', '^'), Y.replace('#', '$')
                a, b = a.replace('0', ''), b.replace('0', '')
                try:
                    if re.search(r'[?]P[<]sw1[>].+[?]P[<]sw2[>]', a):
                        return self._fields_to_function_metathesis(a, X, Y)
                    else:
                        return self._fields_to_function(a, b, X, Y)
                except Exception as e:
                    raise DatafileError('Line {}: "{}" cannot be compiled as regex: ̪{}'.format(i + 1, line, e))

    def _fields_to_function_metathesis(self, a: str, X: str, Y: str) -> Callable[[str], str]:
        left = r'(?P<X>{}){}(?P<Y>{})'.format(X, a, Y)
        regexp = re.compile(left)

        def rewrite(m: Any) -> str:
            d = {k: none2str(v) for k, v in m.groupdict().items()}
            return '{}{}{}{}'.format(d['X'], d['sw2'], d['sw1'], d['Y'])

        return lambda w: regexp.sub(rewrite, w, re.U)

    def _fields_to_function(self, a: str, b: str, X: str, Y: str) -> Callable[[str], str]:
        left = r'(?P<X>{})(?P<a>{})(?P<Y>{})'.format(X, a, Y)
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
