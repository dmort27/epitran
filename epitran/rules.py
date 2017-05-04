# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

import unicodedata
import codecs

import regex as re


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
        with codecs.open(rule_file, 'r', 'utf-8') as f:
            for line in f:
                if not re.match('\s*%', line):
                    rules.append(self._read_rule(line))
        return [rule for rule in rules if rule is not None]

    def _sub_symbols(self, line):
        while re.match('::\w+::', line):
            s = re.match('::\w+::', line).group(0)
            if s in self.symbols:
                line = line.replace(s, self.symbols[s])
            else:
                raise RuleFileError('Undefined symbol: {}'.format(s))
        return line

    def _read_rule(self, line):
        line = line.strip()
        if line:
            line = unicodedata.normalize('NFC', line)
            s = re.match(r'(?P<symbol>::\w+::)\s*=\s*(?P<value>.+)', line)
            r = re.match(r'(?P<a>\S+)\s*->\s*(?P<b>\S+)\s*/\s*(?P<X>\S*)\s*[_]\s*(?P<Y>\S*)', line)
            if s:
                self.symbols[s.group('symbol')] = s.group('value')
            elif r:
                a, b, X, Y = r.groups()
                X, Y = X.replace('#', '^'), Y.replace('#', '$')
                X, Y = self._sub_symbols(X), self._sub_symbols(Y)
                a = a.replace('0', '')
                b = b.replace('0', '')
                if re.search(r'[?]P[<]sw1[>].+[?]P[<]sw2[>]', a):
                    return self._fields_to_function_metathesis(a, X, Y)
                else:
                    return self._fields_to_function(a, b, X, Y)
            else:
                print('Line "{}" contains an error.'.format(line))

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
