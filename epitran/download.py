import os
import logging
import gzip
import zipfile
import requests
from io import BytesIO

logger = logging.getLogger('epitran')

CEDICT_URL='https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.txt.gz'
CC_CANTO_URL='https://cccanto.org/cccanto-170202.zip'
OPENDICT_JA_URL = 'https://github.com/open-dict-data/ipa-dict/raw/refs/heads/master/data/ja.txt'


def base_dir() -> str:
    data_dir = os.path.join(os.path.dirname(__file__), 'epitran_data')
    os.makedirs(data_dir, exist_ok=True)
    return data_dir

def cedict() -> str:
    txtfilename = os.path.join(base_dir(), 'cedict.txt')

    if not os.path.exists(txtfilename):
        logger.info(f'Downloading CC-CEDICT on {txtfilename}')
        gzfilename = os.path.join(base_dir(), 'cedict.txt.gz')
        r = requests.get(CEDICT_URL)
        with open(gzfilename, 'wb') as f:
            f.write(r.content)
        with gzip.open(gzfilename, 'rb') as ip_byte, open(txtfilename, 'w') as op:
            op.write(ip_byte.read().decode('utf-8'))
        os.remove(gzfilename)

    return txtfilename

def cc_canto() -> str:
    cc_canto_dir = os.path.join(base_dir(), 'cc_canto')
    cc_canto_txt = os.path.join(cc_canto_dir, 'cccanto-webdist.txt')

    if not os.path.exists(cc_canto_txt):
        r = requests.get(CC_CANTO_URL)
        with zipfile.ZipFile(BytesIO(r.content)) as zip_ref:
            zip_ref.extractall(cc_canto_dir)

    return cc_canto_txt

def opendict_ja() -> str:
    txtfilename = os.path.join(base_dir(), 'ja.txt')

    if not os.path.exists(txtfilename):
        logger.info(f'Downloading open-dict-data/ipa-dict JA on {txtfilename}')
        r = requests.get(OPENDICT_JA_URL)
        with open(txtfilename, 'wb') as f:
            f.write(r.content)
    return txtfilename
