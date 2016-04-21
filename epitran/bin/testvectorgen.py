#!/usr/bin/env python

from __future__ import print_function

import argparse
import codecs
import epitran.vector


def main(code, space, infile):
    vec = epitran.vector.VectorWithIPASpace(code, space)
    with codecs.open(infile, 'r', 'utf-8') as f:
        for line in f:
            fields = line.split('\t')
            if len(fields) > 1:
                word = fields[0]
                cat, case, orth, phon, vec = vec.word_to_pfvecter(word)
                print("Category: {}".format(cat))
                print("Case: {}".format(case))
                print("Orthographic: {}".format(orth))
                print("Phonetic: {}".format(phon))
                print("Vector: {}".format(vec))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--code', help='Script code.')
    parser.add_argument('-s', '--space', help='Space.')
    parser.add_argument('-i', '--infile', help='Input file.')
    args = parser.parse_args()
    main(args.code, args.space, args.infile)
