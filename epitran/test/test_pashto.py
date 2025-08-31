import epitran

epi = epitran.Epitran('pbu-Arab')

def t(x, y):
    assert epi.transliterate(x) == y

def test_core():
    t('پښتو', 'paxto')         # PBU merger ښ→x, no implicit vowels
    t('کور', 'kor')            # و→o in C_و_C by postrule (Northern Pashto)
    t('ګل', 'ɡul')             # no implicit vowels between ګ and ل
    t('څنګه', 'sanɡa')         # څ→s; n→ŋ/_{ɡ}, final ه→a
    t('ژوند', 'd͡ʒwand')        # ژ→d͡ʒ (PBU), و→w between consonants
    t('مینه', 'mina')          # ی→i; final ه→a (or ə if spelledۀ)
    t('ونه', 'wana')            # و onset → w, no implicit vowels
    t('او', 'ɑw')              # diphthong (correct transliteration)
    t('ستړی', 'staɽai')          # ړۍ→ɽ + final ی as i, no implicit vowels
