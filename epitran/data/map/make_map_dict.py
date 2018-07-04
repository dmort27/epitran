#!/usr/bin/env python3

import glob
import re
import pprint
from collections import defaultdict


def main():
    modes = defaultdict(list)
    for fn in glob.glob('*.csv'):
        m = re.match(r'(\w{3})-(\w{4}(?:-\w+)?)\.csv', fn)
        modes[m.group(1)].append(m.group(2))
    pprint.pprint(modes, depth=4)


if __name__ == '__main__':
    main()
