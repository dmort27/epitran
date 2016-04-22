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
                print(u"WORD: {}".format(word))
                segs = vec.word_to_segs(word)
                print(segs)
                for record in segs:
                    cat, case, orth, phon, id_, vector = record
                    print(u"Category: {}".format(cat))
                    print(u"Case: {}".format(case))
                    print(u"Orthographic: {}".format(orth))
                    print(u"Phonetic: {}".format(phon))
                    print(u"Vector: {}".format(vector))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--code', help='Script code.')
    parser.add_argument('-s', '--space', help='Space.')
    parser.add_argument('-i', '--infile', help='Input file.')
    args = parser.parse_args()
    main(args.code, args.space, args.infile)
