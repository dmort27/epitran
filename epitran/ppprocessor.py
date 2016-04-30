from __future__ import print_function, unicode_literals

import os.path
import sys

import pkg_resources
import regex as re
import unicodecsv as csv


class PrePostProcessor(object):
    def __init__(self, code, fix):
        self.rules = self._read_file(code, fix)

    def _read_file(self, code, fix):
        assert fix in ['pre', 'post']
        fn = os.path.join('data', fix, code + '.csv')
        abs_fn = pkg_resources.resource_filename(__name__, fn)
        rules = []
        if os.path.isfile(abs_fn):
            with open(abs_fn, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                next(reader)
                for a, b, X, Y in reader:
                    rules.append(self._fields_to_function(a, b, X, Y))
        else:
            print('No {}processor found.'.format(fix), file=sys.stderr)
        return rules

    def _fields_to_function(self, a, b, X, Y):
        left = r'(?P<X>{})(?P<a>{})(?P<Y>{})'.format(X, a, Y)
        regexp = re.compile(left)

        def rewrite(m):
            return '{}{}{}'.format(m.group('X'), b, m.group('Y'))

        return lambda w: regexp.sub(rewrite, w)

    def process(self, word):
        word = '#{}#'.format(word)
        for rule in self.rules:
            word = rule(word)
        return word[1:-1]  # Remove octothorps.
