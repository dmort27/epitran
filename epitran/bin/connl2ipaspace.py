#!/usr/bin/env python

import argparse
import codecs
import logging
from collections import Counter

import epitran
import panphon
import unicodecsv as csv

logging.basicConfig(level=logging.DEBUG)


def normpunc(epi, s):
    def norm(c):
        if c in epi.puncnorm:
            return epi.puncnorm[c]
        else:
            return c
    return ''.join(map(norm, s))


def add_record_gen(epi, ft, orth):
    space = Counter()
    orth = normpunc(epi, orth)
    trans = epi.transliterate(orth)
    while trans:
        pref = ft.longest_one_seg_prefix(trans)
        if pref != '':
            space[pref] += 1
            trans = trans[len(pref):]
        else:
            if trans[0] in epi.puncnorm_vals:
                space[trans[0]] += 1
            else:
                space[trans[0]] += 1
            trans = trans[1:]
    return space


def add_file_gen(epi, ft, fn):
    space = Counter()
    with codecs.open(fn, 'r', 'utf-8') as f:
        for line in f:
            fields = line.split(u'\t')
            if len(fields) > 0:
                orth = fields[0]
                space.update(add_record_gen(epi, ft, orth))
    logging.debug(u'Length of counter:\t{}'.format(len(space)))
    return space


def add_file_op(epi, ft, fn):
    space = Counter()
    with codecs.open(fn, 'r', 'utf-8') as f:
        for line in f:
            fields = line.split(u'\t')
            if len(fields) > 0:
                orth = fields[0]
                trans = epi.transliterate(orth)
                while trans:
                    pref = ft.longest_one_seg_prefix(trans)
                    if pref != '':
                        space[pref] += 1
                        trans = trans[len(pref):]
                    else:
                        if trans[0] in epi.puncnorm:
                            space[epi.puncnorm[trans[0]]] += 1
                        else:
                            space[trans[0]] += 1
                        trans = trans[1:]
    logging.debug(u'Length of counter:\t{}'.format(len(space)))
    return space


def print_space(output, space):
    pairs = enumerate(sorted(filter(lambda x: x, space.keys())))
    with open(output, 'wb') as f:
        writer = csv.writer(f, encoding='utf-8')
        for i, char in pairs:
            writer.writerow((i, char))


def main(code, op, infiles, output):
    epi = epitran.Epitran(code)
    ft = panphon.FeatureTable()
    space = Counter()
    for fn in infiles:
        logging.debug(u'Scanning:\t{}'.format(fn).encode('utf-8'))
        add_file = add_file_op if op else add_file_gen
        space.update(add_file(epi, ft, fn))
    print_space(output, space)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--op', action='store_true', help='Script uses punctuation as (parts of) letters.')
    parser.add_argument('-c', '--code', help='Script code for CONNL files.')
    parser.add_argument('-o', '--output', help='Output file.')
    parser.add_argument('infiles', nargs='+', help='CONLL files serving as basis for segment space.')
    args = parser.parse_args()
    main(args.code, args.op, args.infiles, args.output)
