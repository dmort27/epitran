# Epitran

A library and tool for transliterating orthographic text as IPA (International Phonetic Alphabet).

## Usage

The principle script for transliterating orthographic text as IPA is `epitranscriber.py`. It takes one argument, the ISO 639-3 code for the language of the orthographic text, takes orthographic text at standard in and writes Unicode IPA to standard out.

```
$ echo "Düğün olur bayram gelir" | epitranscribe.py "tur-Latn"
dyɰyn oluɾ bajɾam ɟeliɾ
$ epitranscriber.py "tur-Latn" < orthography.txt > phonetic.txt
```

Additionally, the small Python module ```epitran``` can be used to easily write more sophisticated Python programs for deploying the **epitran** mapping tables. This is documented below.

## Using the `epitran` Module

The functionality in the `epitran` module is encapsulated in the very simple `Epitran` class. Its constructor takes one argument, `code`, the ISO 639-3 code of the language to be transliterated plus a hyphen plus a four letter code for the script (e.g. 'Latn' for Latin script, 'Cyrl' for Cyrillic script, and 'Arab' for a Person-Arabic script).

```
>>> import epitran
>>> epi = epitran.Epitran('tur-Latn')
```

The `Epitran` class has only one "public" method (to the extent that such a concept exists in Python): the `transliterate` method:

**transliterate**(text):
Convert `text` (in orthography of the language specified in the constructor) to IPA, which is returned.

```
>>> epi.transliterate(u'Düğün')
u'd\xfc\u011f\xfcn'
>>> print(epi.transliterate(u'Düğün'))
düğün
```

## Currently Supported Languages

| Code     | Language   |
|----------|------------|
| hau-Latn | Hausa      |
| ind-Latn | Indonesian |
| jav-Latn | Javanese   |
| tur-Latn | Turkish    |
| yor-Latn | Yoruba     |


## Possible Pipelines
