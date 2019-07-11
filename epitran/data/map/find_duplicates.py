#!/usr/bin/env python3

import csv
import sys
from collections import defaultdict

def main(fn):
    mappings = defaultdict(list)
    with open(fn, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for orth, phon in reader:
            mappings[orth].append(phon)
    print(mappings)
    for orth, phons in mappings.items():
        if len(phons) > 1:
            print(orth)

if __name__ == '__main__':
    main(sys.argv[1])
