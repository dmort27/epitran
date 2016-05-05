from __future__ import print_function, unicode_literals

import logging
import os.path
import unicodedata

import pkg_resources
import regex as re
import unicodecsv as csv

logging.basicConfig(level=logging.DEBUG)


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
                for record in reader:
                    if not re.match(ur'\s*%', record[0]):
                        record = map(lambda x: unicodedata.normalize('NFC', x), record)
                        a, b, X, Y = record
                        rules.append(self._fields_to_function(a, b, X, Y))
        return rules

    def _fields_to_function(self, a, b, X, Y):
        left = r'(?P<X>{})(?P<a>{})(?P<Y>{})'.format(X, a, Y)
        regexp = re.compile(left)

        def rewrite(m):
            return '{}{}{}'.format(m.group('X'), b, m.group('Y'))

        return lambda w: regexp.sub(rewrite, w, re.U)

    def process(self, word):
        word = unicodedata.normalize('NFC', word)
        word = '#{}#'.format(word)
        for rule in self.rules:
            word = rule(word)
            # logging.debug(word.encode('utf-8'))
        return word[1:-1]  # Remove octothorps.
