#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals, absolute_import)

import glob
import re
import io

import unicodecsv


def build_rule(fields):
    try:
        a, b, X, Y = fields
        b = "0" if not b else b
        a = "0" if not a else a
        return '{} -> {} / {} _ {}'.format(a, b, X, Y)
    except ValueError:
        print('Malformed rule: {}'.format(','.join(fields)))


def main():
    for csv in glob.glob('*.csv'):
        txt = re.match('[A-Za-z-]+', csv).group(0) + '.txt'
        with open(csv, 'rb') as f, io.open(txt, 'w', encoding='utf-8') as g:
            reader = unicodecsv.reader(f, encoding='utf-8')
            next(reader)
            for fields in reader:
                if re.match('\s*%', fields[0]):
                    print(','.join([x for x in fields if x]), file=g)
                else:
                    rule = build_rule(fields)
                    rule = re.sub('[ ]+', ' ', rule)
                    rule = re.sub('[ ]$', '', rule)
                    print(rule, file=g)


if __name__ == '__main__':
    main()
