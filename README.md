# Epitran

A library and tool for transliterating orthographic text as IPA (International Phonetic Alphabet).

## Usage

The principle script for transliterating orthographic text as IPA is `epitranscriber.py`. It takes one argument, the ISO 639-3 code for the language of the orthographic text, takes orthographic text at standard in and writes Unicode IPA to standard out.

```
$ echo "Düğün olur bayram gelir" | epitranscribe.py "tur-Latn"
dyɰyn oluɾ bajɾam ɟeliɾ
$ epitranscribe.py "tur-Latn" < orthography.txt > phonetic.txt
```

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
The codes for `character_category` are from the initial characters of the two character sequences listed in the "General Category" codes found in [Chapter 4 of the Unicode Standard](http://www.unicode.org/versions/Unicode8.0.0/ch04.pdf#G134153). For example, "L" corresponds to letters and "P" corresponds to production marks. The above data structure is likely to change in subsequent versions of the library. Here is an example of an interaction with it:

```
>>> import epitran
>>> epi = epitran.Epitran('tur-Latn')
>>> epi.word_to_pfvector(u'Düğün')
[('L', 1, u'd', 15, [-1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1]), ('L', 0, '', -1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ('L', 0, '', -1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ('L', 0, '', -1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ('L', 0, u'n', 83, [-1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1])]
```

## Using the ```epitran.vector``` Module

The ```epitran.vector``` module is also very simple. It contains one class, ```VectorWithIPASpace```, including one method of interest, ```word_to_segs```:

```
>>> import epitran.vector
>>> >>> vwis = epitran.vector.VectorWithIPASpace('uzb-Latn', 'uzb-with_attached_suffixes-space')
>>> vwis.word_to_segs(u'bugan')
[('L', 0, u'b', u'b', 13, [-1, -1, 1, -1, -1, -1, -1, 0, 1, -1, -1, 1, -1, 0, 1, -1, -1, -1, -1, 0, -1]), ('L', 0, u'u', u'u', 119, [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1]), ('L', 0, u'g', u'\u0261', 3, [-1, -1, 1, -1, -1, -1,
-1, 0, 1, -1, -1, -1, -1, 0, -1, 1, -1, 1, -1, 0, -1]), ('L', 0, u'a', u'a', 115, [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1]), ('L', 0, u'n', u'n', 83, [-1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1
])]
```

## Language Support

### Transliteration Languages

| Code     | Language         |
|----------|------------------|
| hau-Latn | Hausa            |
| ind-Latn | Indonesian       |
| jav-Latn | Javanese         |
| tur-Latn | Turkish          |
| yor-Latn | Yoruba           |
| uzb-Cyrl | Uzbek (Cyrillic) |
| uzb-Latn | Uzbek (Latin)    |

### Language "Spaces"

| Code                                | Language | Note                                 |
|-------------------------------------|----------|--------------------------------------|
| tur-with_attached_suffixes-space    | Turkish  | Based on data with suffixes attached |
| tur-without_attached_suffixes-space | Turkish  | Based on data with suffixes removed  |
| uzb-with_attached_suffixes-space    | Uzbek    | Based on data with suffixes attached |
