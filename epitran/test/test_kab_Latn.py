import epitran
import pytest

epi = epitran.Epitran('kab-Latn')

@pytest.mark.parametrize("orth, ipa", [
    ("taqcict", "taqʃiʃt"),
    ("axxam", "aχːam"),
    ("Nniɣ", "nniɣ"),
    ("abrid", "abrid"),
    ("tuwiḍ", "tuwidˤ"),
])
def test_kab_latn_basic_words(orth, ipa):
    assert epi.transliterate(orth) == ipa
