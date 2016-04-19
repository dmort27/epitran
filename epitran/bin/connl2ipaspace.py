#!/usr/bin/env python

import argparse
import epitran
import panphon
import codecs
from collections import Counter


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
            if len(fields) == 2:
                orth, _ = fields
                space.update(add_record_gen(epi, ft, orth))
    return space


def add_record_op(epi, ft, fn):
    pass


def add_file_op(epi, ft, fn):
    space = Counter()
    with codecs.open(fn, 'r', 'utf-8') as f:
        for line in f:
            fields = line.split(u'\t')
            if len(fields) == 2:
                orth, tag = fields
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
    return space


def print_space(space):
    print(u'"Index","Segment"'.encode('utf-8'))
    pairs = enumerate(sorted(space.keys()))
    for i, char in pairs:
        char = char.replace('"', r'\"')
        record = u'"{}","{}"'.format(i, char)
        record = record.encode('utf-8')
        print(record)


def main(code, op, infiles):
    epi = epitran.Epitran(code)
    ft = panphon.FeatureTable()
    space = Counter()
    for fn in infiles:
        add_file = add_file_op if op else add_file_gen
        space.update(add_file(epi, ft, fn))
    print_space(space)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--op', action='store_true', help='Script uses punctuation as (parts of) letters.')
    parser.add_argument('-c', '--code', help='Script code for CONNL files.')
    parser.add_argument('infiles', nargs='+', help='CONLL files serving as basis for segment space.')
    args = parser.parse_args()
    main(args.code, args.op, args.infiles)
