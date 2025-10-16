#!/usr/bin/env python

import argparse
import codecs
import logging
from collections import Counter
from typing import List

import csv

import epitran
import epitran.flite
import panphon

logger = logging.getLogger('epitran')


def normpunc(flite: epitran.flite.Flite, s: str) -> str:
    def norm(c: str) -> str:
        if c in flite.puncnorm:
            return flite.puncnorm[c]
        else:
            return c
    return ''.join(map(norm, s))


def add_record(flite: epitran.flite.Flite, ft: panphon.FeatureTable, orth: str) -> Counter[str]:
    space: Counter[str] = Counter()
    orth = normpunc(flite, orth)
    trans = flite.transliterate(orth)
    while trans:
        pref = ft.longest_one_seg_prefix(trans)
        if pref != '':
            space[pref] += 1
            trans = trans[len(pref):]
        else:
            if trans[0] in flite.puncnorm.puncnorm:
                space[trans[0]] += 1
            else:
                space[trans[0]] += 1
            trans = trans[1:]
    return space


def add_file(flite: epitran.flite.Flite, ft: panphon.FeatureTable, fn: str) -> Counter[str]:
    space: Counter[str] = Counter()
    with codecs.open(fn, 'r', 'utf-8') as f:
        for line in f:
            fields = line.split(u'\t')
            if len(fields) > 0:
                orth = fields[0]
                space.update(add_record(flite, ft, orth))
    logger.debug(u'Length of counter:\t{}'.format(len(space)))
    return space


def print_space(output: str, space: Counter[str]) -> None:
    pairs = enumerate(sorted(filter(lambda x: x, space.keys())))
    with open(output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i, char in pairs:
            writer.writerow((i, char))


def main(infiles: List[str], output: str) -> None:
    flite = epitran.flite.Flite()
    ft = panphon.FeatureTable()
    space: Counter[str] = Counter()
    for fn in infiles:
        logger.debug(u'Scanning:\t{}'.format(fn).encode('utf-8'))
        space.update(add_file(flite, ft, fn))
    print_space(output, space)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='Output file.')
    parser.add_argument('infiles', nargs='+', help='CONLL files serving as basis for segment space.')
    args = parser.parse_args()
    main(args.infiles, args.output)
