#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import fileinput
import panphon


def vec2bin(vec):
    return ''.join(map(lambda x: '1' if x == '+' else '0', vec))


def token2vectors(ft, token):
    if ft.filter_string(token) == token:
        vectors = []
        for seg in ft.segs(token):
            id_num = ft.seg_seq[seg]
            vec = vec2bin(ft.segment_to_vector(seg))
            vectors.append('{}:{}'.format(id_num, vec))
        return ','.join(vectors)
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
