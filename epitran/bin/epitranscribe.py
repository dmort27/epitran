#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unicodedata
import epitran
import argparse


def main(code):
    epi = epitran.Epitran(code)
    for line in sys.stdin:  # pointless
        line = line.decode('utf-8')
        line = unicodedata.normalize('NFD', line.lower())
        line = epi.transliterate(line)
        line = line.encode('utf-8')
        sys.stdout.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=u'Coverts text from STDIN (in the language specified),' +
        'into Unicode IPA and emits it to STDOUT.')
    parser.add_argument('code', help=u'ISO 639-3 code for conversion language')
    args = parser.parse_args()
    main(args.code)
