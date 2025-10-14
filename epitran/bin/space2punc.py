#!/usr/bin/env python

import sys
import unicodedata
import csv


def main(fns, fnn):
    punc = set()
    for fn in fns:
        with open(fn, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for _, s in reader:
                if len(s) == 1 and unicodedata.category(s)[0] == u'P':
                    punc.add(s)
    with open(fnn, 'wb') as f:
        writer = csv.writer(f)
        for mark in sorted(list(punc)):
            writer.writerow([mark])


if __name__ == '__main__':
    main(sys.argv[1:-1], sys.argv[-1])
