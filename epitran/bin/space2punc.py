#!/usr/bin/env python

import sys
import unicodedata
import unicodecsv as csv


def main(fns, fnn):
    punc = set()
    for fn in fns:
        print fn
        with open(fn, 'rb') as f:
            reader = csv.reader(f, encoding='utf-8')
            for _, s in reader:
                if len(s) == 1 and unicodedata.category(s)[0] == u'P':
                    punc.add(s)
    with open(fnn, 'wb') as f:
        writer = csv.writer(f, encoding='utf-8')
        for mark in sorted(list(punc)):
            writer.writerow([mark])


if __name__ == '__main__':
    main(sys.argv[1:-1], sys.argv[-1])
