#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import unicodedata
import sys
import fileinput

def main():
    for line in fileinput.input():
        line = line.decode('utf-8')
        token = line.strip()
        if len(token) > 0 and unicodedata.category(token[0]) == 'Lu':
            is_upper = 1
        else:
            is_upper = 0
        line = u'{}\t{}'.format(is_upper, token)
        line = line.encode('utf-8')
        print(line)


if __name__ == '__main__':
    main()
