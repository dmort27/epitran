#!/usr/bin/env python

import fileinput
import unicodedata


def main() -> None:
    with fileinput.input() as f:
        for line in f:
            token = line.strip()
            if len(token) > 1 and unicodedata.category(token[1]) == 'Lu':
                is_cap = 0
            elif len(token) > 0 and unicodedata.category(token[0]) == 'Lu':
                is_cap = 1
            else:
                is_cap = 0
            line = f'{is_cap}\t{token}'
            print(line)


if __name__ == '__main__':
    main()
