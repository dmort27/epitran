#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import glob
import os.path

from lxml import etree
import unicodecsv as csv

import epitran
import panphon.featuretable


def read_tokens(fn):
    tree = etree.parse(fn)
    root = tree.getroot()
    return [tok.text for tok in root.findall('.//TOKEN')]


def read_input(input_, langscript):
    space = set()
    epi = epitran.Epitran(langscript)
    ft = panphon.featuretable.FeatureTable()
    for dirname in input_[0]:
        for fn in glob.glob(os.path.join(dirname, '*.ltf.xml')):
            for token in read_tokens(fn):
                ipa = epi.transliterate(token)
                for seg in ft.segs_safe(ipa):
                    space.add(seg)
    return space


def write_output(output, space):
    with open(output, 'wb') as f:
        writer = csv.writer(f, encoding='utf-8')
        for n, ch in enumerate(sorted(list(space))):
            writer.writerow((n, ch))


def main(langscript, input_, output):
    space = read_input(input_, langscript)
    write_output(output, space)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--code', help='language-script code')
    parser.add_argument('-i', '--input', nargs='+', action='append', help='Directories where input LTF files are found')
    parser.add_argument('-o', '--output', help='Output file')
    args = parser.parse_args()
    main(args.code, args.input, args.output)
