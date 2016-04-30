#!/usr/bin/env python

from __future__ import print_function

import argparse
import codecs

import epitran.vector


def main(code, space, infile):
    vec = epitran.vector.VectorsWithIPASpace(code, space)
    with codecs.open(infile, 'r', 'utf-8') as f:
        for line in f:
            fields = line.split('\t')
            if len(fields) > 1:
                word = fields[0]
                print(u"WORD: {}".format(word).encode('utf-8'))
                segs = vec.word_to_segs(word)
                for record in segs:
                    cat, case, orth, phon, id_, vector = record
                    print(u"Category: {}".format(cat).encode('utf-8'))
                    print(u"Case: {}".format(case).encode('utf-8'))
                    print(u"Orthographic: {}".format(orth).encode('utf-8'))
                    print(u"Phonetic: {}".format(phon).encode('utf-8'))
                    print(u"Vector: {}".format(vector).encode('utf-8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--code', required=True, help='Script code.')
    parser.add_argument('-s', '--space', required=True, help='Space.')
    parser.add_argument('-i', '--infile', required=True, help='Input file.')
    args = parser.parse_args()
    main(args.code, args.space, args.infile)
