import epitran

epi = epitran.Epitran('pbu-Arab')

def t(x, y):
    assert epi.transliterate(x) == y

def test_core():
    t('پښتو', 'paxto')         # PBU merger ښ→x
    t('کور', 'kor')            # و→o in C_و_C by postrule
    t('ګل', 'ɡul')             # و→u in C_و_C default
    t('څنګه', 'səŋɡə')         # څ→s; n→ŋ/_{ɡ}
    t('ژوند', 'd͡ʒund')        # ژ→d͡ʒ (PBU), cluster handling
    t('مینه', 'mina')          # ی→i; final ه→a (or ə if spelledۀ)
    t('ونه', 'wuna')           # و onset → w
    t('او', 'aw')              # diphthong
    t('ستړی', 'staɽai')        # ړۍ→ɽ + final ی as ai in this form if spelled ی/ۍ
