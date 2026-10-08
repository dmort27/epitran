#!/usr/bin/env pythoh

import csv
import glob


def read_map(fn: str) -> list[tuple[str, str]]:
    with open(fn, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        return [(a, b) for [a, b] in reader]


def is_bijection(mapping: list[tuple[str, str]]) -> bool:
    a, b = zip(*mapping)
    distinct_a, distinct_b = set(a), set(b)
    return len(distinct_a) == len(mapping) and len(distinct_b) == len(mapping)


def main(map_fns: list[str]) -> None:
    for fn in map_fns:
        mapping = read_map(fn)
        is_b = is_bijection(mapping)
        print(f'{fn}\t{is_b}')


if __name__ == '__main__':
    map_fns = glob.glob('../data/*.csv')
    main(map_fns)
