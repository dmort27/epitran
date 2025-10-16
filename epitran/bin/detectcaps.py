#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata
import fileinput


def main() -> None:
    for line in fileinput.input():
        token = line.strip()
        if len(token) > 1 and unicodedata.category(token[1]) == 'Lu':
            is_cap = 0
        elif len(token) > 0 and unicodedata.category(token[0]) == 'Lu':
            is_cap = 1
        else:
            is_cap = 0
        line = '{}\t{}'.format(is_cap, token)
        print(line)


if __name__ == '__main__':
    main()
