#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import unicodedata
import fileinput


def main():
    for line in fileinput.input():
        line = line.decode('utf-8')
        token = line.strip()
        if len(token) > 1 and unicodedata.category(token[1]) == 'Lu':
            is_cap = 0
        elif len(token) > 0 and unicodedata.category(token[0]) == 'Lu':
            is_cap = 1
        else:
            is_cap = 0
        line = u'{}\t{}'.format(is_cap, token)
        line = line.encode('utf-8')
        print(line)


if __name__ == '__main__':
    main()
