import os
import requests
import gzip
import zipfile
from io import BytesIO

CEDICT_URL='https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.txt.gz'
CC_CANTO_URL='https://cccanto.org/cccanto-170202.zip'

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

def get_cc_canto_file():
    return os.path.join(get_dir(), 'cc_canto', 'cccanto-webdist.txt')

def cc_canto_exists():
    return os.path.exists(get_cc_canto_file())

def cc_canto():
    cc_canto_dir = os.path.join(get_dir(), 'cc_canto')
    r = requests.get(CC_CANTO_URL)
    with zipfile.ZipFile(BytesIO(r.content)) as zip_ref:
        zip_ref.extractall(cc_canto_dir)
    print('cc canto dir', cc_canto_dir)



