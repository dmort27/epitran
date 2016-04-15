#!/usr/bin/env Python
from __future__ import print_function

import sys
import json
import panphon
import epitran
import argparse

def process_sent(sent):
    return sent

def main(code, infile, outfile):
    sents = json.loads(infile.read())
    sents = [process_sent(s) for s in sents]
    outfile.write(json.dumps(sents))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('code', help='Language and script code.')
    parser.add_argument('infile', nargs='?',
                        type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?',
                        type=argparse.FileType('w'),
                        default=sys.stdout)
    args = parser.parse_args()
    main(args.code, args.infile, args.outfile)
