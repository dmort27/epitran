#!/usr/bin/env Python


import csv
import glob
import re


def build_rule(fields: list[str]) -> str | None:
    try:
        a, b, X, Y = fields
        b = "0" if not b else b
        a = "0" if not a else a
        return f'{a} -> {b} / {X} _ {Y}'
    except ValueError:
        print('Malformed rule: {}'.format(','.join(fields)))
        return None


def main() -> None:
    for csv_file in glob.glob('*.csv'):
        match = re.match('[A-Za-z-]+', csv_file)
        if match:
            txt = match.group(0) + '.txt'
        else:
            continue
        with open(csv_file, 'r', encoding='utf-8') as f, open(txt, 'w', encoding='utf-8') as g:
            reader = csv.reader(f)
            next(reader)
            for fields in reader:
                if re.match(r'\s*%', fields[0]):
                    print(','.join([x for x in fields if x]), file=g)
                else:
                    rule = build_rule(fields)
                    if rule is not None:
                        rule = re.sub('[ ]+', ' ', rule)
                        rule = re.sub('[ ]$', '', rule)
                        print(rule, file=g)


if __name__ == '__main__':
    main()
