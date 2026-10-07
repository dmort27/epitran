#!/usr/bin/env python

import argparse
import csv
import glob
import os.path

import panphon.featuretable
from lxml import etree

import epitran


def read_tokens(fn: str) -> list[str]:
    tree = etree.parse(fn)
    root = tree.getroot()
    return [tok.text for tok in root.findall('.//TOKEN')]


def read_input(input_: list[list[str]], langscript: str) -> set[str]:
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


def write_output(output: str, space: set[str]) -> None:
    with open(output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for n, ch in enumerate(sorted(list(space))):
            writer.writerow((n, ch))


def main(langscript: str, input_: list[list[str]], output: str) -> None:
    space = read_input(input_, langscript)
    write_output(output, space)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--code', help='language-script code')
    parser.add_argument('-i', '--input', nargs='+', action='append', help='Directories where input LTF files are found')
    parser.add_argument('-o', '--output', help='Output file')
    args = parser.parse_args()
    main(args.code, args.input, args.output)
