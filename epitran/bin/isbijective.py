#!/usr/bin/env pythoh

import glob

import csv


def read_map(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        return [(a, b) for [a, b] in reader]


def is_bijection(mapping):
    a, b = zip(*mapping)
    distinct_a, distinct_b = set(a), set(b)
    return len(distinct_a) == len(mapping) and len(distinct_b) == len(mapping)


def main(map_fns):
    for fn in map_fns:
        mapping = read_map(fn)
        is_b = is_bijection(mapping)
        print('{}\t{}'.format(fn, is_b))


if __name__ == '__main__':
    map_fns = glob.glob('../data/*.csv')
    main(map_fns)
