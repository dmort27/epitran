#!/usr/bin/env python

import csv
import sys
import unicodedata


def main(fns: list[str], fnn: str) -> None:
    punc = set()
    for fn in fns:
        with open(fn, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for _, s in reader:
                if len(s) == 1 and unicodedata.category(s)[0] == u'P':
                    punc.add(s)
    with open(fnn, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for mark in sorted(list(punc)):
            writer.writerow([mark])


if __name__ == '__main__':
    main(sys.argv[1:-1], sys.argv[-1])
