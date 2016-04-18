#!/usr/bin/env python

import argparse
import epitran
import codecs
from collections import Counter


def add_file(epi, fn):
    space = Counter()
    with codecs.open(fn, 'r', 'utf-8') as f:
        for line in f:
            fields = line.split(u'\t')
            if len(fields) == 2:
                orth, tag = fields
                try:
                    ipa = epi.transliterate(orth)
                    segs = epi.ipa_segs(ipa)
                    for s in segs:
                        space[s] += 1
                except KeyError:
                    ipa = orth
                    for c in ipa:
                        space[c] += 1
    return space


def print_space(space):
    pairs = enumerate(sorted(space.keys()))
    for i, char in pairs:
        char = char.replace('"', r'\"')
        print u'"{}","{}"'.format(i, char)


def main(code, infiles):
    epi = epitran.Epitran(code)
    space = Counter()
    for fn in infiles:
        space.update(add_file(epi, fn))
    print_space(space)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--code', help='Script code for CONNL files.')
    parser.add_argument('infiles', nargs='+', help='CONLL files serving as basis for segment space.')
    args = parser.parse_args()
    main(args.code, args.infiles)
