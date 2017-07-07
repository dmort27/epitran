# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import io
import logging
import unicodedata

import regex as re
from epitran.exceptions import DatafileError

logging.basicConfig(level=logging.DEBUG)

def none2str(x):
    return x if x else ''


class RuleFileError(Exception):
    pass


class Rules(object):
    def __init__(self, rule_files):
        """Construct an object encoding context-sensitive rules

        Args:
            rule_files (list): list of names of rule files
        """
        self.rules = []
        self.symbols = {}
        for rule_file in rule_files:
            rules = self._read_rule_file(rule_file)
            self.rules = self.rules + rules

    def _read_rule_file(self, rule_file):
        rules = []
        with io.open(rule_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if not re.match('\s*%', line):
                    rules.append(self._read_rule(i, line))
        return [rule for rule in rules if rule is not None]

    def _sub_symbols(self, line):
        while re.search(r'::\w+::', line):
            s = re.search(r'::\w+::', line).group(0)
            if s in self.symbols:
                line = line.replace(s, self.symbols[s])
            else:
                raise RuleFileError('Undefined symbol: {}'.format(s))
        return line

    def _read_rule(self, i, line):
        line = line.strip()
        if line:
            line = unicodedata.normalize('NFC', unicodedata.normalize('NFD', line))
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

    def _fields_to_function_metathesis(self, a, X, Y):
        left = r'(?P<X>{}){}(?P<Y>{})'.format(X, a, Y)
        regexp = re.compile(left)

        def rewrite(m):
            d = {k: none2str(v) for k, v in m.groupdict().items()}
            return '{}{}{}{}'.format(d['X'], d['sw2'], d['sw1'], d['Y'])

        return lambda w: regexp.sub(rewrite, w, re.U)

    def _fields_to_function(self, a, b, X, Y):
        left = r'(?P<X>{})(?P<a>{})(?P<Y>{})'.format(X, a, Y)
        regexp = re.compile(left)

        def rewrite(m):
            d = {k: none2str(v) for k, v in m.groupdict().items()}
            return '{}{}{}'.format(d['X'], b, d['Y'])

        return lambda w: regexp.sub(rewrite, w, re.U)

    def apply(self, text):
        """Apply rules to input text

        Args:
            text (unicode): input text (e.g. Pinyin)

        Returns:
            unicode: output text (e.g. IPA)
        """
        for rule in self.rules:
            text = rule(text)
        return text
