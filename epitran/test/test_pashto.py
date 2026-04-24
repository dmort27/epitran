import epitran
import unittest

class TestPashto(unittest.TestCase):
    def setUp(self):
      self.epi = epitran.Epitran("pbu-Arab")

    def t(self, x, y):
        tr = self.epi.transliterate(x)
        self.assertEqual(tr, y)

    def test_core(self):
        self.t('پښتو', 'paxto')         # PBU merger ښ→x, no implicit vowels
        self.t('کور', 'kor')            # و→o in C_و_C by postrule (Northern Pashto)
        self.t('ګل', 'ɡul')             # no implicit vowels between ګ and ل
        self.t('څنګه', 'saŋɡa')         # څ→s; n→ŋ/_{ɡ}, final ه→a (with nasal assimilation)
        self.t('ژوند', 'd͡ʒwand')        # ژ→d͡ʒ (PBU), و→w between consonants
        self.t('مینه', 'mi:na')          # ی→i; final ه→a (or ə if spelledۀ)
        self.t('ونه', 'wana')            # و onset → w, no implicit vowels
        self.t('او', 'ɑw')              # diphthong (correct transliteration)
        self.t('ستړی', 'staɽai')          # ړۍ→ɽ + final ی as i, no implicit vowels
        self.t('سړي', 'saɽi:')         # ړۍ→ɽ + final ی as i, no implicit vowels
