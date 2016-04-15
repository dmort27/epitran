# Epitran

A library and tool for transliterating orthographic text as IPA (International Phonetic Alphabet).

## Usage

The principle script for transliterating orthographic text as IPA is `epitranscriber.py`. It takes one argument, the ISO 639-3 code for the language of the orthographic text, takes orthographic text at standard in and writes Unicode IPA to standard out.

```
$ echo "Düğün olur bayram gelir" | epitranscribe.py "tur-Latn"
dyɰyn oluɾ bajɾam ɟeliɾ
$ epitranscribe.py "tur-Latn" < orthography.txt > phonetic.txt


Additionally, the small Python module ```epitran``` can be used to easily write more sophisticated Python programs for deploying the **Epitran** mapping tables. This is documented below.

## Using the `epitran` Module

The functionality in the `epitran` module is encapsulated in the very simple `Epitran` class. Its constructor takes one argument, `code`, the ISO 639-3 code of the language to be transliterated plus a hyphen plus a four letter code for the script (e.g. 'Latn' for Latin script, 'Cyrl' for Cyrillic script, and 'Arab' for a Person-Arabic script).

```
>>> import epitran
>>> epi = epitran.Epitran('tur-Latn')
```

The `Epitran` class has only a few "public" method (to the extent that such a concept exists in Python). The most important are ``transliterate`` and ``word_to_pfvector``:

**transliterate**(text):
Convert `text` (in Unicode-encoded orthography of the language specified in the constructor) to IPA, which is returned.

```
>>> epi.transliterate(u'Düğün')
u'd\xfc\u011f\xfcn'
>>> print(epi.transliterate(u'Düğün'))
düğün
```

**word_to_pfvector**(word):
Takes a `word` (a Unicode string) in a supported orthography as input and returns a list of tuples with each tuple corresponding to an IPA segment of the word. The tuples have the following structure:
```
(
    character_category :: String,
    is_upper :: Integer,
    phonetic_form :: Unicode String,
    id_in_unicode_ipa_space :: Integer,
    phonological_feature_vector :: List<Integer>
)
```
This structure is likely to change in subsequent versions of the library.

## Currently Supported Languages

| Code     | Language         |
|----------|------------------|
| hau-Latn | Hausa            |
| ind-Latn | Indonesian       |
| jav-Latn | Javanese         |
| tur-Latn | Turkish          |
| yor-Latn | Yoruba           |
| uzb-Cyrl | Uzbek (Cyrillic) |
| uzb-Latn | Uzbek (Latin)    |


## Possible Pipelines

### Text

**Epitran** is distributed with a few auxiliary scripts in addition `epitranscribe.py`:

- `detectcaps.py`:  Reads a list of word-length tokens (one per line from STDIN) and outputs (to STDOUT) a tab-delimited file in which the first column indicates capitalization (1 for capitalization, 0 for all-caps or initial lower case). The second column consists of the original word.
- `word2pfvectors.py`: Reads a stream formatted like the output of `detectcaps.py` and writes its output to STDOUT. The first column is left untouched. The second column is replaced by a sequence of comma-delimited pairs, each of which consists of an integer (acting as a unique identifier for the corresponding IPA segment), a colon, and a sequence of 1s and 0s which represents the phonological feature values of the corresponding IPA segment.

These scripts are meant to be piped together in the following fashion:
```
$ detectcaps.py < data.txt | epitranscribe.py 'tur-Latn' | word2pfvectors.py
1       15:001000001001100000000,120:110100001000001100110,87:010100001000000100010,120:110100001000001100110,83:011000101001100000000
0       15:001000001001100000000,120:110100001000001100110,87:010100001000000100010,120:110100001000001100110,83:011000101001100000000
0       118:110100001000000001110,106:011101001001100000000,119:110100001000001101110,99:011100001001100000000
0       13:001000001001001000000,115:110100001000000011010,102:010100001000000100000,99:011100001001100000000,115:110100001000000011010,82:011000101001001000000
0       7:001000001000000100000,116:110100001000000000010,106:011101001001100000000,117:110100001000000100010,99:011100001001100000000
```
These scripts may be more useful in understanding the use of **Epitran**, in conjunction with [**PanPhon**](https://pypi.python.org/pypi/panphon/0.2), than in an actual production pipeline.

### JSON

A more practical pipeline (using a JSON dialect as a data format) is currently under development. Feedback on the data format is appreciated.
