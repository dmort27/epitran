#!/usr/bin/env python

import fileinput
import epitran

epi = epitran.Epitran('uig-Arab')
for line in fileinput.input():
    s = epi.transliterate(line.strip().decode('utf-8'))
    print(s.encode('utf-8'))
