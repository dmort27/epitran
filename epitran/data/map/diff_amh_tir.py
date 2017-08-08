#!/usr/bin/env python3

import unicodecsv as csv
import sys


def main(fn1, fn2):
    with open(fn1, 'rb') as f, open(fn2, 'rb') as g:
        reader1 = csv.reader(f, encoding='utf-8')
        reader2 = csv.reader(g, encoding='utf-8')
        next(reader1)
        next(reader2)
        orth1, orth2 = set(), set()
        for orth, phon in reader1:
            orth1.add(orth)
        for orth, phon in reader2:
            orth2.add(orth)
    print(orth1 - orth2)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
