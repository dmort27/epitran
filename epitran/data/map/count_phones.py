#!/usr/bin/env

import epitran.xsampa
import panphon
import unicodecsv as csv


def main(fn):
    ft = panphon.FeatureTable()
    xs = epitran.xsampa.XSampa()
    with open(fn, 'rb') as f:
        reader = csv.reader(f, encoding='utf-8')
        next(reader)
        phones = set()
        for orth, phon in reader:
            phones = phones.union(set(ft.segs_safe(phon)))
    print(len(phones))
    print(sorted(list(map(xs.ipa2xs, phones))))

if __name__ == '__main__':
    main('tir-Ethi-red.csv')
