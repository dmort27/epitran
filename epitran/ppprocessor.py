from __future__ import print_function, unicode_literals, division, absolute_import

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
        rules = []
        fn = os.path.join('data', fix, code + '.csv')
        try:
            abs_fn = pkg_resources.resource_filename(__name__, fn)
        except KeyError:
            return []
        if os.path.isfile(abs_fn):
            with open(abs_fn, 'rb') as f:
                reader = csv.reader(f, encoding='utf-8')
                next(reader)
                for record in reader:
                    if not re.match(r'\s*%', record[0]):
                        assert len(record) == 4
                        record = map(lambda x: unicodedata.normalize('NFC', unicodedata.normalize('NFKD', x)), record)
                        a, b, X, Y = record
                        rules.append(self._fields_to_function(a, b, X, Y))
        return rules

    def _fields_to_function(self, a, b, X, Y):
        # logging.debug('rule-encoding: {} {} {} {}'.format(a, b, X, Y).encode('utf-8'))
        left = r'(?P<X>{}){}(?P<Y>{})'.format(X, a, Y)
        try:
            regexp = re.compile(left)
        except:
            logging.error('"{}" is not a valid regexp.'.format(left))

        def none2string(x):
            if x is None:
                return ''
            else:
                return x

        def rewrite(m):
            d = {k: none2string(v) for k, v in m.groupdict().items()}
            if 'sw1' in d and 'sw2' in d:  # for metathesis
                return r'{}{}{}{}'.format(d['X'], d['sw2'], d['sw1'], d['Y'])
            else:  # for everything else
                return r'{}{}{}'.format(d['X'], b, d['Y'])

        return lambda w: regexp.sub(rewrite, w, re.U)

    def process(self, word):
        word = unicodedata.normalize('NFC', word)
        word = '#{}#'.format(word)
        for rule in self.rules:
            word = rule(word)
            # logging.debug('pre:{}'.format(word).encode('utf-8'))
        return word[1:-1]  # Remove octothorps.
