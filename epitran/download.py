import os
import requests
import gzip

CEDICT_URL='https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.txt.gz'

def get_dir():
    data_dir = os.path.expanduser('~/epitran_data/')
    os.makedirs(data_dir, exist_ok=True)
    return data_dir

def get_cedict_file():
    return os.path.join(get_dir(), 'cedict.txt')

def cedict_exists():
    return os.path.exists(get_cedict_file())

def cedict():
    gzfilename = os.path.join(get_dir(), 'cedict.txt.gz')
    txtfilename = os.path.join(get_dir(), 'cedict.txt')
    r = requests.get(CEDICT_URL)
    with open(gzfilename, 'wb') as f:
        f.write(r.content)
    with gzip.open(gzfilename, 'rb') as ip_byte, open(txtfilename, 'w') as op:
        op.write(ip_byte.read().decode('utf-8'))



