#!/usr/bin/env python3

import sys
import unicodedata


def main(fn: str) -> None:
    with open(fn, encoding='utf-8') as f:
        print(unicodedata.normalize('NFD', f.read()))


if __name__ == '__main__':
    main(sys.argv[1])
