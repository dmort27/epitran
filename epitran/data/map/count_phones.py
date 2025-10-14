#!/usr/bin/env

import epitran.xsampa
import panphon
import csv


def main(fn):
    ft = panphon.FeatureTable()
    xs = epitran.xsampa.XSampa()
    with open(fn, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        phones = set()
        for orth, phon in reader:
            phones = phones.union(set(ft.segs_safe(phon)))
    print(len(phones))
    print(sorted(list(map(xs.ipa2xs, phones))))

if __name__ == '__main__':
    main('tir-Ethi-red.csv')
