#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import fileinput
import panphon


def token2vectors(ft, token):
    if ft.filter_string(token) == token:
        for vector in ft.word_to_vector_list(token):
            pass
        return ''
    else:
        return ''


def main():
    ft = panphon.FeatureTable()
    for line in fileinput.input():
        line = line.decode('utf-8')
        cap, token = line.strip().split('\t')
        vectors = token2vectors(ft, token)
        line = '\t'.join([cap, vectors])
        line = line.encode('utf-8')
        print(line)

if __name__ == '__main__':
    main()
