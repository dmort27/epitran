#!/usr/bin/env python
#
import re
import glob
import csv

RE_DERIVATION = re.compile(r"""self\._?derivation\(u?['"]([^'"]+)['"], u?['"]([^'"]+)['"]\)""", re.M | re.S)
RE_TR = re.compile(r"""self\.epi\.transliterate\(['"]([^'"]+)['"]\).+?self\.assertEqual\(tr, ['"]([^'"]+)['"]\)""", re.M | re.S)
RE_RES = re.compile(r"""self\.epi\.transliterate\(['"]([^'"]+)['"]\).+?self\.assertEqual\(res, ['"]([^'"]+)['"]\)""", re.M | re.S)
RE_ASSERT_TRANS = re.compile(r"""self\._assert_trans\(['"]([^'"]+)['"],\s*['"]([^'"]+)['"]\)""", re.M | re.S)
RE_TUPLE = re.compile(r"""\(['"]([^'"]+)['"],\s*['"]([^'"]+)['"]\)""", re.M | re.S)
RE_CODE = re.compile("""["']([a-z]{3}-[A-Z][a-z]{3})["']""")

def extract_code(code: str) -> str:
    if match := RE_CODE.search(code):
        return match.group(1)
    else:
        print("No code found.")
        return ""

def extract_pairs(code: str) -> list[tuple[str, str]]:
    derivation_type: list[tuple[str, str]] = RE_DERIVATION.findall(code)
    tr_type: list[tuple[str, str]] = RE_TR.findall(code)
    assert_trans_type: list[tuple[str, str]] = RE_ASSERT_TRANS.findall(code)
    tuple_type: list[tuple[str, str]] = RE_TUPLE.findall(code)
    typs = [(x, len(x)) for x in [derivation_type, tr_type, assert_trans_type, tuple_type]]
    pairs = max(typs, key=lambda x: x[1])[0]
    print(f'len(pairs)={len(pairs)}')
    return pairs

def main():
    for filename in glob.glob("../test/*test*.py"):
        with open(filename) as f:
            code = f.read()
            iso639 = extract_code(code)
            iso639 = iso639.replace('-', '_')
            print(f'iso639-3={iso639}')
            pairs = extract_pairs(code)

            with open(f'{iso639}-tests.csv', 'w') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(['input', 'output'])
                writer.writerows(pairs)

if __name__ == "__main__":
    main()
