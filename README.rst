Epitran
=======

A library and tool for transliterating orthographic text as IPA
(International Phonetic Alphabet).

Usage
-----

The principle script for transliterating orthographic text as IPA is
``epitranscriber.py``. It takes one argument, the ISO 639-3 code for the
language of the orthographic text, takes orthographic text at standard
in and writes Unicode IPA to standard out.

::

    $ echo "Düğün olur bayram gelir" | epitranscribe.py "tur-Latn" dyɰyn oluɾ bajɾam ɟeliɾ
    $ epitranscribe.py "tur-Latn" < orthography.txt > phonetic.txt

Additionally, the small Python modules ``epitran`` and
``epitran.vector`` can be used to easily write more sophisticated Python
programs for deploying the **Epitran** mapping tables. This is
documented below.

Using the ``epitran`` Module
----------------------------

The most general functionality in the ``epitran`` module is encapsulated
in the very simple ``Epitran`` class. Its constructor takes one
argument, ``code``, the ISO 639-3 code of the language to be
transliterated plus a hyphen plus a four letter code for the script
(e.g. 'Latn' for Latin script, 'Cyrl' for Cyrillic script, and 'Arab'
for a Perso-Arabic script).

::

    >>> import epitran
    >>> epi = epitran.Epitran('uig-Arab')  # Uyghur in Perso-Arabic script

The ``Epitran`` class has only a few "public" methods (to the extent
that such a concept exists in Python). The most important are
``transliterate`` and ``word_to_tuples``:

Epitran.\ **transliterate**\ (text): Convert ``text`` (in
Unicode-encoded orthography of the language specified in the
constructor) to IPA, which is returned.

::

    >>> epi.transliterate(u'Düğün')
    u'dy\u0270yn'
    >>> print(epi.transliterate(u'Düğün'))
    dyɰyn

Epitran.\ **word\_to\_tuples**\ (word, normpunc=False): Takes a ``word``
(a Unicode string) in a supported orthography as input and returns a
list of tuples with each tuple corresponding to an IPA segment of the
word. The tuples have the following structure:

::

    (
        character_category :: String,
        is_upper :: Integer,
        orthographic_form :: Unicode String,
        phonetic_form :: Unicode String,
        segments :: List<Tuples>
    )

The codes for ``character_category`` are from the initial characters of
the two character sequences listed in the "General Category" codes found
in `Chapter 4 of the Unicode
Standard <http://www.unicode.org/versions/Unicode8.0.0/ch04.pdf#G134153>`__.
For example, "L" corresponds to letters and "P" corresponds to
production marks. The above data structure is likely to change in
subsequent versions of the library. The structure of ``segments`` is as
follows:

::

    (
        segment :: Unicode String,
        vector :: List<Integer>
    )

Here is an example of an interaction with ``word_to_tuples``:

::

    >>> import epitran
    >>> epi = epitran.Epitran('tur-Latn')
    >>> epi.word_to_tuples(u'Düğün')
    [(u'L', 1, u'D', u'd', [(u'd', [-1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1])]), (u'L', 0, u'u\u0308', u'y', [(u'y', [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1])]), (u'L', 0, u'g\u0306', u'\u0270', [(u'\u0270', [-1, 1, -1, 1, 0, -1, -1, 0, 1, -1, -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, -1])]), (u'L', 0, u'u\u0308', u'y', [(u'y', [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1])]), (u'L', 0, u'n', u'n', [(u'n', [-1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1])])]

Preprocessors and Their Pitfalls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to build a maintainable orthography to phoneme mapper, it is
sometimes necessary to employ preprocessors that make contextual
substitutions of symbols before text is passed to a orthography-to-IPA
mapping system that preserves relationships between input and output
characters. This is particularly true of languages with a poor
sound-symbols correspondence (like French and English). Languages like
French are particularly good targets for this approach because the
pronunication of a given string of letters is highly predictable even
though the individual symbols often do not map neatly into sounds.
(Sound-symbol correspondence is so poor in English that effective
English G2P systems rely heavily on pronouncing dictionaries.)

Preprocessing the inputs words to allow for straightforward
grapheme-to-phoneme mappings (as is done in the current version of
``epitran`` for some languages) is advantaeous because the restricted
regular expression language used to write the preprocessing rules is
more powerful than the language for the mapping rules and allows the
equivalent of many mapping rules to be written with a single rule.
Without them, providing ``epitran`` support for languages like French
and German would not be practical. However, they do present some
problems. Specifically, when using a language with a preprocessor, one
**must** be aware that the input word will not always be identical to
the concatenation of the orthographic strings (``orthographic_form``)
output by ``Epitran.word_to_tuples``. Instead, the output of
``word_to_tuple`` will reflect the output of the preprocessor, which may
delete, insert, and change letters in order to allow direct
orthography-to-phoneme mapping at the next step. The same is true of
other methods that rely on ``Epitran.word_to_tuple`` such as
``VectorsWithIPASpace.word_to_segs`` from the ``epitran.vector`` module.

The ``epitran`` module also includes the ``Maps`` class, which provides
information about the mapping files (files that specify a mapping
between orthography and IPA) that are available in the current
installation. It has two public methods:

-  ``lang_script_pairs`` takes no arguments and returns a sorted list of
   tuples.
-  ``paths`` returns a list of the paths to the mapping files for a
   given code (e.g. "deu-Latn" or "deu-Latn-np").

Using the ``epitran.vector`` Module
-----------------------------------

The ``epitran.vector`` module is also very simple. It contains one
class, ``VectorsWithIPASpace``, including one method of interest,
``word_to_segs``:

The constructor for ``VectorsWithIPASpace`` takes two arguments: -
``code``: the language-script code for the language to be processed. -
``spaces``: the codes for the punctuation/symbol/IPA space in which the
characters/segments from the data are expected to reside. The available
spaces are listed `below <#language-support>`__.

It's principle method is ``word_to_segs``:

VectorWithIPASpace.\ **word\_to\_segs**\ (word, normpunc=False) Word is
a Unicode string. If the keyword argument *normpunc* is set to True,
punctuation disovered in *word* is normalized to ASCII equivalents.

A typical interaction with the ``VectorsWithIPASpace`` object via the
``word_to_segs`` method is illustrated here:

::

    >>> import epitran.vector
    >>> vwis = epitran.vector.VectorsWithIPASpace('uzb-Latn', 'uzb-with_attached_suffixes-space')
    >>> vwis.word_to_segs(u'darë')
    [(u'L', 0, u'd', u'd\u032a', u'40', [-1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 0, -1]), (u'L', 0, u'a', u'a', u'37', [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1]), (u'L', 0, u'r', u'r', u'54', [-1, 1, 1, 1, 0, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 0, 0, 0, -1, 0, -1]), (u'L', 0, u'e\u0308', u'ja', u'46', [-1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, 0, -1, 1, -1, -1, -1, 0, -1]), (u'L', 0, u'e\u0308', u'ja', u'37', [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1])]

(It is important to note that, though the word that serves as
input--\ *darë*--has four letters, the output contains four tuples
because the last letter in *darë* actually corresponds to two IPA
segments, /j/ and /a/.) The returned data structure is a list of tuples,
each with the following structure:

::

    (
        character_category :: String,
        is_upper :: Integer,
        orthographic_form :: Unicode String,
        phonetic_form :: Unicode String,
        in_ipa_punc_space :: Integer,
        phonological_feature_vector :: List<Integer>
    )

A few notes are in order regarding this data structure: -
``character_category`` is defined as part of the Unicode standard
(`Chapter
4 <http://www.unicode.org/versions/Unicode8.0.0/ch04.pdf#G134153>`__).
It consists of a single, uppercase letter from the set {'L', 'M', 'N',
'P', 'S', 'Z', 'C'}.. The most frequent of these are 'L' (letter), 'N'
(number), 'P' (punctuation), and 'Z' (separator [including separating
white space]). - ``is_upper`` consists only of integers from the set {0,
1}, with 0 indicating lowercase and 1 indicating uppercase. - The
integer in ``in_ipa_punc_space`` is an index to a list of known
characters/segments such that, barring degenerate cases, each character
or segment is assignmed a unique and globally consistant number. In
cases where a character is encountered which is not in the known space,
this field has the value -1. - The length of the list
``phonological_feature_vector`` should be constant for any instantiation
of the class (it is based on the number of features defined in panphon)
but is--in principles--variable. The integers in this list are drawn
from the set {-1, 0, 1}, with -1 corresponding to '-', 0 corresponding
to '0', and 1 corresponding to '+'. For characters with no IPA
equivalent, all values in the list are 0.

Language Support
----------------

Transliteration Language/Script Pairs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+--------------------------+
| Code          | Language (Script)        |
+===============+==========================+
| aar-Latn      | Afar                     |
+---------------+--------------------------+
| amh-Ethi      | Amharic                  |
+---------------+--------------------------+
| aze-Cyrl      | Azerbaijani (Cyrillic)   |
+---------------+--------------------------+
| aze-Latn      | Azerbaijani (Latin)      |
+---------------+--------------------------+
| ben-Beng      | Bengali                  |
+---------------+--------------------------+
| ckb-Arab      | Sorani                   |
+---------------+--------------------------+
| deu-Latn      | German                   |
+---------------+--------------------------+
| deu-Latn-np   | German\*                 |
+---------------+--------------------------+
| fas-Arab      | Farsi (Perso-Arabic)     |
+---------------+--------------------------+
| fra-Latn      | French                   |
+---------------+--------------------------+
| fra-Latn-np   | French\*                 |
+---------------+--------------------------+
| hau-Latn      | Hausa                    |
+---------------+--------------------------+
| hin-Deva      | Hindi                    |
+---------------+--------------------------+
| hun-Latn      | Hungarian                |
+---------------+--------------------------+
| ind-Latn      | Indonesian               |
+---------------+--------------------------+
| jav-Latn      | Javanese                 |
+---------------+--------------------------+
| kaz-Cyrl      | Kazakh (Cyrillic)        |
+---------------+--------------------------+
| kaz-Latn      | Kazakh (Latin)           |
+---------------+--------------------------+
| kir-Arab      | Kyrgyz (Perso-Arabic)    |
+---------------+--------------------------+
| kir-Cyrl      | Kyrgyz (Cyrillic)        |
+---------------+--------------------------+
| kir-Latn      | Kyrgyz (Latin)           |
+---------------+--------------------------+
| krm-Latn      | Kurmanji                 |
+---------------+--------------------------+
| nld-Latn      | Dutch                    |
+---------------+--------------------------+
| orm-Latn      | Oromo                    |
+---------------+--------------------------+
| pan-Guru      | Punjabi (Eastern)        |
+---------------+--------------------------+
| som-Latn      | Somali                   |
+---------------+--------------------------+
| spa-Latn      | Spanish                  |
+---------------+--------------------------+
| tam-Taml      | Tamil                    |
+---------------+--------------------------+
| tel-Telu      | Telugu                   |
+---------------+--------------------------+
| tha-Thai      | Thai                     |
+---------------+--------------------------+
| tir-Ethi      | Tigrinya                 |
+---------------+--------------------------+
| tuk-Cyrl      | Turkmen (Cyrillic)       |
+---------------+--------------------------+
| tuk-Latn      | Turkmen (Latin)          |
+---------------+--------------------------+
| tur-Latn      | Turkish (Latin)          |
+---------------+--------------------------+
| uig-Arab      | Uyghur (Perso-Arabic)    |
+---------------+--------------------------+
| uzb-Cyrl      | Uzbek (Cyrillic)         |
+---------------+--------------------------+
| uzb-Latn      | Uzbek (Latin)            |
+---------------+--------------------------+
| vie-Latn      | Vietnamese               |
+---------------+--------------------------+
| yor-Latn      | Yoruba                   |
+---------------+--------------------------+

\*These language preprocessors and maps naively assume a phonemic
orthography.

Language "Spaces"
~~~~~~~~~~~~~~~~~

+------------------+------------+----------------------------------------+
| Code             | Language   | Note                                   |
+==================+============+========================================+
| deu-Latn         | German     |                                        |
+------------------+------------+----------------------------------------+
| nld-Latn         | Dutch      |                                        |
+------------------+------------+----------------------------------------+
| spa-Latn         | Spanish    |                                        |
+------------------+------------+----------------------------------------+
| tur-Latn-suf     | Turkish    | Based on data with suffixes attached   |
+------------------+------------+----------------------------------------+
| tur-Latn-nosuf   | Turkish    | Based on data with suffixes removed    |
+------------------+------------+----------------------------------------+
| uzb-Latn-suf     | Uzbek      | Based on data with suffixes attached   |
+------------------+------------+----------------------------------------+

Note that major languages, including **French**, are missing from this
table to to a lack of appropriate text data.

Using the ``epitran.flite`` Module
----------------------------------

The ``epitran.flite`` module shells out to the ``flite`` speech
synthesis system to do English G2P.
`Flite <http://www.speech.cs.cmu.edu/flite/>`__ must be installed in
order for this module to function. Because ``flite`` must be loaded each
time ``english_g2p`` is called, performance is quite poor. Usage is
illustrated below:

::

      >>> import epitran.flite
      >>> fl = epitran.flite.Flite()
      >>> print fl.english_g2p(u'San Leandro')
      sænliɑndɹow

This module also contains a wrapper that takes orthographic English as
an input and returns as an output the same data structure returned by
``epitran.vector.VectorWithIPASpace.word_to_segs``. Usage of this class
and its most useful method is illustrated below:

::

      >>> import epitran.flite
      >>> vwis = epitran.flite.VectorsWithIPASpace()
      >>> vwis.word_to_segs(u'San Leandro')
      [(u'L', 1, u's', u's', 50, [-1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1]), (u'L', 0, u'\xe6', u'\xe6', 58, [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1]), (u'L', 0, u'n', u'n', 47, [-1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1]), (u'Z', 0, u' ', u'', 1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (u'L', 0, u'l', u'l', 45, [-1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1]), (u'L', 0, u'i', u'i', 4 2, [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1]), (u'L', 0, u'\u0251', u'\u0251', 61, [1, 1, -1, 1, 0, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1]), (u'L', 0, u'n', u'n', 47, [-1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1]), (u'L', 0, u'd', u'd', 36, [-1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1]), (u'L', 0, u'\u0279', u'\u0279', 66, [-1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 0, -1]), (u'L', 0, u'o', u'o', 48, [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1]), (u'L', 0, u'w', u'w', 55, [-1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, 0, 1, 1, -1, 1, 1, 0, -1])]

The observant user will note that the interface is the same as that of
the identically-named class in the the ``epitran.vector`` module.

Extending Epitran with map files, preprocessors and postprocessors
------------------------------------------------------------------

Language support in Epitran is provided through map files, which define
mappings between orthographic and phonetic units, preprocessors that run
before the map is applied, and postprocessors that run after the map is
applied. These are all defined in UTF8-encoded, comma-delimited value
(CSV) files. The files are each named -.csv where is the (three letter,
all lowercase) ISO 639-3 code for the language and is the (four letter,
capitalized) ISO 15924 code for the script. These files reside in the
``data`` directory of the Epitran installation under the ``map``,
``pre``, and ``post`` subdirectories, respectively.

Map files (mapping tables)
~~~~~~~~~~~~~~~~~~~~~~~~~~

The map files are simple, two-column files where the first column
contains the orthgraphic characters/sequences and the second column
contains the phonetic characters/sequences. For many languages (most
languages with unambiguous, phonemically adequate orthographies) just
this easy-to-produce mapping file is adequate to produce a serviceable
G2P system.

The first row is a header and is discarded. For consistency, it should
contain the fields "Orth" and "Phon". The following rows by consist of
fields of any length, separated by a comma. The same phonetic form (the
second field) may occur any number of times but an orthographic form may
only occur once. Where one orthograrphic form is a prefix of another
form, the longer form has priority in mapping. In other words, matching
between orthographic units and orthographic strings is greedy. Mapping
works by finding the longest prefix of the orthographic form and adding
the corresponding phonetic string to the end of the phonetic form, then
removing the prefix from the orthographic form and continuing, in the
same manner, until the orthographic form is consumed. If no non-empty
prefix of the orthographic form is present in the mapping table, the
first character in the orthographic form is removed and appended to the
phonetic form. The normal sequence then resumes. This means that
non-phonetic characters may end up in the "phonetic" form, which we
judge to be better than loosing information through an inadequate
mapping table.

Preprocesssors and postprocessors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For language-script pairs with more complicated orthographies, it is
sometimes necessary to manipulate the orthographic form prior to mapping
or to manipulate the phonetic form after mapping. This is done, in
Epitran, with grammars of context-sensitive string rewrite rules. In
truth, these rules would be more than adequate to solve the mapping
problem as well but in practical terms, it is usually easier to let
easy-to-understand and easy-to-maintain mapping files carry most of the
weight of conversion and reserve the more powerful context sensitive
grammar formalism for pre- and post-processing.

To make it easy to edit the files in a spreadsheet (like LibreOffice
Calc), the files are formatted as CSV. Of course, they can be edited in
text editor as well. The first row is a header, which should have the
fields "a", "b", "X", and "Y", corresponding to the parts of "a → b / X
\_ Y", which can be read as "a is rewritten as b in the context between
X and Y". It is equivalent to XaY → XbY. Each subsequent row is a rule
in this format. The symbol "#" matches a word-boundary (at the beginning
and end of a word-length token). For example, a rule that changes "e" to
"ə" at the end of a word, for use in a postprocessor, would have the
following form:

::

    e,ə,,#

Which corresponds to:

::

    e → ə / _ #

The rules apply in order, so earlier rules may "feed" and "bleed" later
rules. Therefore, their sequence is *very important* and can be
leveraged in order to achieve valuable results.
