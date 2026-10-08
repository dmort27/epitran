#!/usr/bin/env python

import fileinput

import epitran

epi = epitran.Epitran('uig-Arab')
with fileinput.input() as f:
    for line in f:
        s = epi.transliterate(line.strip())
        print(s)
