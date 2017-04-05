#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals, absolute_import)

import glob
import re
import codecs

import unicodecsv


def build_rule(fields):
    try:
        a, b, X, Y = fields
    except ValueError:
        print('Malformed rule: {}'.format(','.join(fields)))
    return '{} -> {} / {} _ {}'.format(a, b, X, Y)


def main(globex):
    for csv in glob.glob('*.csv'):
        txt = csv[:-4] + '.txt'
        with open(csv, 'rb') as f, codecs.open(txt, 'w', 'utf-8') as g:
            reader = unicodecsv.reader(f, encoding='utf-8')
            for fields in reader:
                if re.match('\s%', fields[0]):
                    rule = build_rule(fields)
                    print(rule, file=g)


if __name__ == '__main__':
    main()
