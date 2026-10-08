#!/usr/bin/env python


import argparse
import codecs

import epitran.vector


def main(code: str, space: list[str], infile: str) -> None:
    vec = epitran.vector.VectorsWithIPASpace(code, space)
    with codecs.open(infile, 'r', 'utf-8') as f:
        for line in f:
            fields = line.split('\t')
            if len(fields) > 1:
                word = fields[0]
                print(f"WORD: {word}".encode())
                segs = vec.word_to_segs(word)
                for record in segs:
                    cat, case, orth, phon, _id, vector = record
                    print(f"Category: {cat}".encode())
                    print(f"Case: {case}".encode())
                    print(f"Orthographic: {orth}".encode())
                    print(f"Phonetic: {phon}".encode())
                    print(f"Vector: {vector}".encode())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--code', required=True, help='Script code.')
    parser.add_argument('-s', '--space', required=True, help='Space.')
    parser.add_argument('-i', '--infile', required=True, help='Input file.')
    args = parser.parse_args()
    main(args.code, args.space, args.infile)
