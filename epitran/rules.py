# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

import unicodedata
import codecs
import os.path

import pkg_resources

import regex as re


class Rules(object):
    def __init__(self, rule_files):
        self.rules = []
        for rule_file in rule_files:
            # rule_file = os.path.join('data', rule_file + '.txt')
            # rule_file = pkg_resources.resource_filename(__name__, rule_file)
            rules = self._read_rule_file(rule_file)
            self.rules = self.rules + rules

    def _read_rule_file(self, rule_file):
        rules = []
        with codecs.open(rule_file, 'r', 'utf-8') as f:
            for line in f:
                if not re.match('\s*!', line):
                    rules.append(self._read_rule(line))
        return [rule for rule in rules if rule is not None]

    def _read_rule(self, line):
        line = line.strip()
        m = re.match(r'(?P<a>\S+)\s*->\s*(?P<b>\S+)\s*/\s*(?P<X>\S*)\s*[_]\s*(?P<Y>\S*)', line)
        if line and m:
            line = unicodedata.normalize('NFC', line)
            a, b, X, Y = m.groups()
            X, Y = X.replace('#', '^'), Y.replace('#', '$')
            b = b.replace('0', '')
            return self._fields_to_function(a, b, X, Y)
        else:
            print('Line "{}" contains an error.'.format(line))

    def _fields_to_function(self, a, b, X, Y):
        left = r'(?P<X>{})(?P<a>{})(?P<Y>{})'.format(X, a, Y)
        regexp = re.compile(left)

        def rewrite(m):
            return '{}{}{}'.format(m.group('X'), b, m.group('Y'))

        return lambda w: regexp.sub(rewrite, w, re.U)

    def apply(self, text):
        for rule in self.rules:
            text = rule(text)
        return text
