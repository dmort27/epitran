Epitran
=======

A library and tool for transliterating orthographic text as IPA
(International Phonetic Alphabet).

Usage
-----

The Python modules ``epitran`` and ``epitran.vector`` can be used to
easily write more sophisticated Python programs for deploying the
**Epitran** mapping tables, preprocessors, and postprocessors. This is
documented below.

Using the ``epitran`` Module
----------------------------

The Epitran class
~~~~~~~~~~~~~~~~~

The most general functionality in the ``epitran`` module is encapsulated
in the very simple ``Epitran`` class:

Epitran(code, preproc=True, postproc=True, ligatures=False,
cedict\_file=None).

Its constructor takes one argument, ``code``, the ISO 639-3 code of the
language to be transliterated plus a hyphen plus a four letter code for
the script (e.g. 'Latn' for Latin script, 'Cyrl' for Cyrillic script,
and 'Arab' for a Perso-Arabic script). It also takes optional keyword
arguments:

-  ``preproc`` and ``postproc`` enable pre- and post-processors. These
   are enabled by default.
-  ``ligatures`` enables non-standard IPA ligatures like "ʤ" and "ʨ".
-  ``cedict_file`` gives the path to the
   `CC-CEDict <https://cc-cedict.org/wiki/>`__ dictionary file (relevant
   only when working with Mandarin Chinese and which, because of
   licensing restrictions cannot be distributed with Epitran).

.. code:: python

    >>> import epitran
    >>> epi = epitran.Epitran('uig-Arab')  # Uyghur in Perso-Arabic script

It is now possible to use the Epitran class for English and Mandarin
Chinese (Simplified and Traditional) G2P as well as the other langugages
that use Epitran's "classic" model. For Chinese, it is necessary to
point the constructor to a copy of the
`CC-CEDict <https://cc-cedict.org/wiki/>`__ dictionary:

.. code:: python

    >>> import epitran
    >>> epi = epitran.Epitran('cmn-Hans', cedict_file='cedict_1_0_ts_utf-8_mdbg.txt')

The most useful public method of the Epitran class is ``transliterate``:

Epitran.\ **transliterate**\ (text, normpunc=False, ligatures=False).
Convert ``text`` (in Unicode-encoded orthography of the language
specified in the constructor) to IPA, which is returned. ``normpunc``
enables punctuation normalization and ``ligatures`` enables non-standard
IPA ligatures like "ʤ" and "ʨ". Usage is illustrated below (Python 2):

.. code:: python

    >>> epi.transliterate(u'Düğün')
    u'dy\u0270yn'
    >>> print(epi.transliterate(u'Düğün'))
    dyɰyn

| Epitran.\ **word\_to\_tuples**\ (word, normpunc=False):
| Takes a ``word`` (a Unicode string) in a supported orthography as
input and returns a list of tuples with each tuple corresponding to an
IPA segment of the word. The tuples have the following structure:

::

    (
        character_category :: String,
        is_upper :: Integer,
        orthographic_form :: Unicode String,
        phonetic_form :: Unicode String,
        segments :: List<Tuples>
    )

Note that **word\_to\_tuples** is not implemented for all
language-script pairs.

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

Here is an example of an interaction with ``word_to_tuples`` (Python 2):

.. code:: python

    >>> import epitran
    >>> epi = epitran.Epitran('tur-Latn')
    >>> epi.word_to_tuples(u'Düğün')
    [(u'L', 1, u'D', u'd', [(u'd', [-1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1])]), (u'L', 0, u'u\u0308', u'y', [(u'y', [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1])]), (u'L', 0, u'g\u0306', u'\u0270', [(u'\u0270', [-1, 1, -1, 1, 0, -1, -1, 0, 1, -1, -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, -1])]), (u'L', 0, u'u\u0308', u'y', [(u'y', [1, 1, -1, 1, -1, -1, -1, 0, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1])]), (u'L', 0, u'n', u'n', [(u'n', [-1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 0, -1])])]

The Backoff class
~~~~~~~~~~~~~~~~~

Sometimes, when parsing text in more than one script, it is useful to
employ a graceful backoff. This is provided by the Backoff class:

Backoff(lang\_script\_codes, cedict\_file=None)

Note that the Backoff class does not currently support parameterized
preprocessor and postprocessor application and does not support
non-standard ligatures. It also does not support punctuation
normalization. ``lang_script_codes`` is a list of codes like
``eng-Latn`` or ``hin-Deva``. For example, if one was transcribing a
Hindi text with many English loanwords and some stray characters of
Simplified Chinese, one might use the following code (Python 3):

.. code:: python

    from epitran.backoff import Backoff
    >>> backoff = Backoff(['hin-Deva', 'eng-Latn', 'cmn-Hans'], cedict_file=‘cedict_1_0_ts_utf-8_mdbg.txt')
    >>> backoff.transliterate('हिन्दी')
    'ɦindiː'
    >>> backoff.transliterate('English')
    'ɪŋɡlɪʃ'
    >>> backoff.transliterate('中文')
    'ʈ͡ʂoŋwən'

Backoff works on a token-by-token basis: tokens that contain mixed
scripts will be returned as the empty string, since they cannot be fully
converted by any of the modes.

The Backoff class has the following public methods:

-  **transliterate**: returns a unicode string of IPA phonemes
-  **trans\_list**: returns a list of IPA unicode strings, each of which
   is a
    phoneme
-  **xsampa\_list**: returns a list of X-SAMPA (ASCII) strings, each of
   which is
    phoneme

Consider the following example (Python 3):

.. code:: python

    >>> backoff.transliterate('हिन्दी')
    'ɦindiː'
    >>> backoff.trans_list('हिन्दी')
    ['ɦ', 'i', 'n', 'd', 'iː']
    >>> backoff.xsampa_list('हिन्दी')
    ['h\\', 'i', 'n', 'd', 'i:']

Preprocessors, postprocessors, and their pitfalls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to build a maintainable orthography to phoneme mapper, it is
sometimes necessary to employ preprocessors that make contextual
substitutions of symbols before text is passed to a orthography-to-IPA
mapping system that preserves relationships between input and output
characters. This is particularly true of languages with a poor
sound-symbols correspondence (like French and English). Languages like
French are particularly good targets for this approach because the
pronunciation of a given string of letters is highly predictable even
though the individual symbols often do not map neatly into sounds.
(Sound-symbol correspondence is so poor in English that effective
English G2P systems rely heavily on pronouncing dictionaries.)

Preprocessing the inputs words to allow for straightforward
grapheme-to-phoneme mappings (as is done in the current version of
``epitran`` for some languages) is advantageous because the restricted
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

For information on writing new pre- and post-processors, see the section
on "`Extending Epitran with map files, preprocessors and
postprocessors <#extending-epitran>`__\ ", below.

Using the ``epitran.vector`` Module
-----------------------------------

The ``epitran.vector`` module is also very simple. It contains one
class, ``VectorsWithIPASpace``, including one method of interest,
``word_to_segs``:

The constructor for ``VectorsWithIPASpace`` takes two arguments:

-  ``code``: the language-script code for the language to be processed.
-  ``spaces``: the codes for the punctuation/symbol/IPA space in which
   the characters/segments from the data are expected to reside. The
   available spaces are listed `below <#language-support>`__.

Its principle method is ``word_to_segs``:

VectorWithIPASpace.\ **word\_to\_segs**\ (word, normpunc=False).
``word`` is a Unicode string. If the keyword argument *normpunc* is set
to True, punctuation discovered in ``word`` is normalized to ASCII
equivalents.

A typical interaction with the ``VectorsWithIPASpace`` object via the
``word_to_segs`` method is illustrated here (Python 2):

.. code:: python

    >>> import epitran.vector
    >>> vwis = epitran.vector.VectorsWithIPASpace('uzb-Latn', ['uzb-Latn'])
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

A few notes are in order regarding this data structure:

-  ``character_category`` is defined as part of the Unicode standard
   (`Chapter
   4 <http://www.unicode.org/versions/Unicode8.0.0/ch04.pdf#G134153>`__).
   It consists of a single, uppercase letter from the set {'L', 'M',
   'N', 'P', 'S', 'Z', 'C'}.. The most frequent of these are 'L'
   (letter), 'N' (number), 'P' (punctuation), and 'Z' (separator
   [including separating white space]).
-  ``is_upper`` consists only of integers from the set {0, 1}, with 0
   indicating lowercase and 1 indicating uppercase.
-  The integer in ``in_ipa_punc_space`` is an index to a list of known
   characters/segments such that, barring degenerate cases, each
   character or segment is assignmed a unique and globally consistant
   number. In cases where a character is encountered which is not in the
   known space, this field has the value -1.
-  The length of the list ``phonological_feature_vector`` should be
   constant for any instantiation of the class (it is based on the
   number of features defined in panphon) but is--in
   principles--variable. The integers in this list are drawn from the
   set {-1, 0, 1}, with -1 corresponding to '-', 0 corresponding to '0',
   and 1 corresponding to '+'. For characters with no IPA equivalent,
   all values in the list are 0.

Language Support
----------------

Transliteration Language/Script Pairs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------+----------------------------+
| Code           | Language (Script)          |
+================+============================+
| aar-Latn       | Afar                       |
+----------------+----------------------------+
| amh-Ethi       | Amharic                    |
+----------------+----------------------------+
| ara-Arab       | Literary Arabic            |
+----------------+----------------------------+
| aze-Cyrl       | Azerbaijani (Cyrillic)     |
+----------------+----------------------------+
| aze-Latn       | Azerbaijani (Latin)        |
+----------------+----------------------------+
| ben-Beng       | Bengali                    |
+----------------+----------------------------+
| ben-Beng-red   | Bengali (reduced)          |
+----------------+----------------------------+
| bxk-Latn       | Bukusu                     |
+----------------+----------------------------+
| cat-Latn       | Catalan                    |
+----------------+----------------------------+
| ceb-Latn       | Cebuano                    |
+----------------+----------------------------+
| cmn-Hans       | Mandarin (Simplified)\*    |
+----------------+----------------------------+
| cmn-Hant       | Mandarin (Traditional)\*   |
+----------------+----------------------------+
| ckb-Arab       | Sorani                     |
+----------------+----------------------------+
| deu-Latn       | German                     |
+----------------+----------------------------+
| deu-Latn-np    | German†                    |
+----------------+----------------------------+
| eng-Latn       | English‡                   |
+----------------+----------------------------+
| fas-Arab       | Farsi (Perso-Arabic)       |
+----------------+----------------------------+
| fra-Latn       | French                     |
+----------------+----------------------------+
| fra-Latn-np    | French†                    |
+----------------+----------------------------+
| hau-Latn       | Hausa                      |
+----------------+----------------------------+
| hin-Deva       | Hindi                      |
+----------------+----------------------------+
| hun-Latn       | Hungarian                  |
+----------------+----------------------------+
| ilo-Latn       | Ilocano                    |
+----------------+----------------------------+
| ind-Latn       | Indonesian                 |
+----------------+----------------------------+
| ita-Latn       | Italian                    |
+----------------+----------------------------+
| jav-Latn       | Javanese                   |
+----------------+----------------------------+
| kaz-Cyrl       | Kazakh (Cyrillic)          |
+----------------+----------------------------+
| kaz-Latn       | Kazakh (Latin)             |
+----------------+----------------------------+
| kin-Latn       | Kinyarwanda                |
+----------------+----------------------------+
| kir-Arab       | Kyrgyz (Perso-Arabic)      |
+----------------+----------------------------+
| kir-Cyrl       | Kyrgyz (Cyrillic)          |
+----------------+----------------------------+
| kir-Latn       | Kyrgyz (Latin)             |
+----------------+----------------------------+
| kmr-Latn       | Kurmanji                   |
+----------------+----------------------------+
| lao-Laoo       | Lao                        |
+----------------+----------------------------+
| lsm-Latn       | Lusaamia                   |
+----------------+----------------------------+
| mar-Deva       | Marathi                    |
+----------------+----------------------------+
| mlt-Latn       | Maltese                    |
+----------------+----------------------------+
| mya-Mymr       | Burmese                    |
+----------------+----------------------------+
| msa-Latn       | Malay                      |
+----------------+----------------------------+
| nld-Latn       | Dutch                      |
+----------------+----------------------------+
| nya-Latn       | Chichewa                   |
+----------------+----------------------------+
| orm-Latn       | Oromo                      |
+----------------+----------------------------+
| pan-Guru       | Punjabi (Eastern)          |
+----------------+----------------------------+
| pol-Latn       | Polish                     |
+----------------+----------------------------+
| por-Latn       | Portuguese                 |
+----------------+----------------------------+
| ron-Latn       | Romanian                   |
+----------------+----------------------------+
| rus-Cyrl       | Russian                    |
+----------------+----------------------------+
| sna-Latn       | Shona                      |
+----------------+----------------------------+
| som-Latn       | Somali                     |
+----------------+----------------------------+
| spa-Latn       | Spanish                    |
+----------------+----------------------------+
| swa-Latn       | Swahili                    |
+----------------+----------------------------+
| swe-Latn       | Swedish                    |
+----------------+----------------------------+
| tam-Taml       | Tamil                      |
+----------------+----------------------------+
| tel-Telu       | Telugu                     |
+----------------+----------------------------+
| tgk-Cyrl       | Tajik                      |
+----------------+----------------------------+
| tgl-Latn       | Tagalog                    |
+----------------+----------------------------+
| tha-Thai       | Thai                       |
+----------------+----------------------------+
| tir-Ethi       | Tigrinya                   |
+----------------+----------------------------+
| tuk-Cyrl       | Turkmen (Cyrillic)         |
+----------------+----------------------------+
| tuk-Latn       | Turkmen (Latin)            |
+----------------+----------------------------+
| tur-Latn       | Turkish (Latin)            |
+----------------+----------------------------+
| ukr-Cyrl       | Ukranian                   |
+----------------+----------------------------+
| uig-Arab       | Uyghur (Perso-Arabic)      |
+----------------+----------------------------+
| uzb-Cyrl       | Uzbek (Cyrillic)           |
+----------------+----------------------------+
| uzb-Latn       | Uzbek (Latin)              |
+----------------+----------------------------+
| vie-Latn       | Vietnamese                 |
+----------------+----------------------------+
| xho-Latn       | Xhosa                      |
+----------------+----------------------------+
| yor-Latn       | Yoruba                     |
+----------------+----------------------------+
| zul-Latn       | Zulu                       |
+----------------+----------------------------+

\*Chinese G2P requires the freely available
`CC-CEDict <https://cc-cedict.org/wiki/>`__ dictionary.

†These language preprocessors and maps naively assume a phonemic
orthography.

‡English G2P requires the installation of the freely available `CMU
Flite <http://tts.speech.cs.cmu.edu/awb/flite-2.0.5-current.tar.bz2>`__
speech synthesis system.

Languages with limited support due to highly ambiguous orthographies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some the languages listed above should be approached with caution. It is
not possible to provide highly accurate support for these
language-script pairs due to the high degree of ambiguity inherent in
the orthographies. Eventually, we plan to support these languages with a
different back end based on WFSTs or neural methods.

+---------------+------------------------+
| Code          | Language (Script)      |
+===============+========================+
| ara-Arab      | Arabic                 |
+---------------+------------------------+
| cat-Latn      | Catalan                |
+---------------+------------------------+
| ckb-Arab      | Sorani                 |
+---------------+------------------------+
| fas-Arab      | Farsi (Perso-Arabic)   |
+---------------+------------------------+
| fra-Latn      | French                 |
+---------------+------------------------+
| fra-Latn-np   | French†                |
+---------------+------------------------+
| mya-Mymr      | Burmese                |
+---------------+------------------------+
| por-Latn      | Portuguese             |
+---------------+------------------------+

Language "Spaces"
~~~~~~~~~~~~~~~~~

+------------------+------------+----------------------------------------+
| Code             | Language   | Note                                   |
+==================+============+========================================+
| amh-Ethi         | Amharic    |                                        |
+------------------+------------+----------------------------------------+
| deu-Latn         | German     |                                        |
+------------------+------------+----------------------------------------+
| eng-Latn         | English    |                                        |
+------------------+------------+----------------------------------------+
| nld-Latn         | Dutch      |                                        |
+------------------+------------+----------------------------------------+
| spa-Latn         | Spanish    |                                        |
+------------------+------------+----------------------------------------+
| tur-Latn         | Turkish    | Based on data with suffixes attached   |
+------------------+------------+----------------------------------------+
| tur-Latn-nosuf   | Turkish    | Based on data with suffixes removed    |
+------------------+------------+----------------------------------------+
| uzb-Latn-suf     | Uzbek      | Based on data with suffixes attached   |
+------------------+------------+----------------------------------------+

Note that major languages, including **French**, are missing from this
table to to a lack of appropriate text data.

Installation of Flite (for English G2P)
---------------------------------------

For use with most languages, Epitran requires no special installation
steps. It can be installed as an ordinarary python package, either with
``pip`` or by running ``python setup.py install`` in the root of the
source directory. However, English G2P in Epitran relies on CMU Flite, a
speech synthesis package by Alan Black and other speech researchers at
Carnegie Mellon University. For the current version of Epitran, you
should follow the installation instructions for ``lex_lookup``, which is
used as the default G2P interface for Epitran.

``t2p``
~~~~~~~

The ``epitran.flite`` module shells out to the ``flite`` speech
synthesis system to do English G2P.
`Flite <http://www.speech.cs.cmu.edu/flite/>`__ must be installed in
order for this module to function. The ``t2p`` binary from ``flite`` is
not installed by default and must be manually copied into the path. An
illustration of how this can be done on a Unix-like system is given
below. Note that GNU ``gmake`` is required and that, if you have another
``make`` installed, you may have to call ``gmake`` explicitly:

.. code:: bash

    $ tar xjf flite-2.0.0-release.tar.bz2
    $ cd flite-2.0.0-release/
    $ ./configure && make
    $ sudo make install
    $ sudo cp bin/t2p /usr/local/bin

You should adapt these instructions to local conditions. Installation on
Windows is easiest when using Cygwin. You will have to use your
discretion in deciding where to put ``t2p.exe`` on Windows, since this
may depend on your python setup. Other platforms are likely workable but
have not been tested.

``lex_lookup``
~~~~~~~~~~~~~~

``t2p`` does not behave as expected on letter sequences that are highly
infrequent in English. In such cases, ``t2p`` gives the pronunciation of
the English letters of the name, rather than an attempt at the
pronunciation of the name. There is a different binary included in the
most recent (pre-release) versions of Flite that behaves better in this
regard, but takes some extra effort to install. To install, you need to
obtain at least version
`2.0.5 <http://tts.speech.cs.cmu.edu/awb/flite-2.0.5-current.tar.bz2>`__
of Flite. Untar and compile the source, following the steps below,
adjusting where appropriate for your system:

.. code:: bash

    $ tar xjf flite-2.0.5-current.tar.bz2
    $ cd flite-2.0.5-current
    $ ./configure && make
    $ sudo make install
    $ cd testsuite
    $ make lex_lookup
    $ sudo cp lex_lookup /usr/local/bin

When installing on MacOS and other systems that use a BSD version of
``cp``, some modification to a Makefile must be made in order to install
flite-2.0.5 (between steps 3 and 4). Edit ``main/Makefile`` and change
both instances of ``cp -pd`` to ``cp -pR``. Then resume the steps above
at step 4.

Usage
~~~~~

To use ``lex_lookup``, simply instantiate Epitran as usual, but with the
``code`` set to 'eng-Latn':

.. code:: python

    >>> import epitran
    >>> epi = epitran.Epitran('eng-Latn')
    >>> print epi.transliterate(u'Berkeley')
    bɹ̩kli

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
contains the phonetic characters/sequences. The two columns are
separated by a comma; each row is terminated by a newline. For many
languages (most languages with unambiguous, phonemically adequate
orthographies) just this easy-to-produce mapping file is adequate to
produce a serviceable G2P system.

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

The preprocessor and postprocessor files have the same format. They
consist of a sequence of lines, each consisting of one of four types:

#. Symbol definitions
#. Context-sensitive rewrite rules
#. Comments
#. Blank lines

Symbol definitions
^^^^^^^^^^^^^^^^^^

Lines like the following

::

    ::vowels:: = a|e|i|o|u

define symbols that can be reused in writing rules. Symbols must consist
of a prefix of two colons, a sequence of one or more lowercase letters
and underscores, and a suffix of two colons. The are separated from
their definitions by the equals sign (optionally set off with white
space). The definition consists of a substring from a regular
expression.

Symbols must be defined before they are referenced.

Rewrite rules
^^^^^^^^^^^^^

Context-sensitive rewrite rules in Epitran are written in a format
familiar to phonologists but transparent to computer scientists. They
can be schematized as

::

    a -> b / X _ Y

which can be rewitten as

::

    XaY → XbY

The arrow ``->`` can be read as "is rewritten as" and the slash ``/``
can be read as "in the context". The underscore indicates the position
of the symbol(s) being rewritten. Another special symbol is the
octothorp ``#``, which indicates the beginning or end of a (word length)
string (a word boundary). Consider the following rule:

::

    e -> ə / _ #

This rule can be read as "/e/ is rewritten as /ə/ in the context at the
end of the word." A final special symbol is zero ``0``, which represents
the empty string. It is used in rules that insert or delete segments.
Consider the following rule that deletes /ə/ between /k/ and /l/:

::

    ə　-> 0 / k _ l

All rules must include the arrow operator, the slash operator, and the
underscore. A rule that applies in a context-free fashion can be written
in the following way:

::

    ch -> x / _

The implementation of context-sensitive rules in Epitran pre- and
post-processors uses regular expression replacement. Specifically, it
employs the ``regex`` package, a drop-in replacement for ``re``. Because
of this, regular expression notation can be used in writing rules:

::

    c -> s / _ [ie]

or

::

    c -> s / _ (i|e)

For a complete guide to ``regex`` regular expressions, see the
documentation for ```re`` <https://docs.python.org/2/library/re.html>`__
and for ```regex`` <https://pypi.python.org/pypi/regex>`__,
specifically.

Fragments of regular expressions can be assigned to symbols and reused
throughout a file. For example, symbol for the disjunction of vowels in
a language can be used in a rule that changes /u/ into /w/ before
vowels:

::

    ::vowels:: = a|e|i|o|u
    ...
    u -> w / _ (::vowels::)

There is a special construct for handling cases of metathesis (where
"AB" is replaced with "BA"). For example, the rule:

::

    (?P<sw1>[เแโไใไ])(?P<sw2>.) -> 0 / _

Will "swap" the positions of any character in "เแโไใไ" and any following
character. Left of the arrow, there should be two groups (surrounded by
parentheses) with the names ``sw1`` and ``sw2`` (a name for a group is
specified by ``?P<name>`` appearing immediately after the open
parenthesis for a group. The substrings matched by the two groups,
``sw1`` and ``sw2`` will be "swapped" or metathesized. The item
immediately right of the arrow is ignored, but the context is not.

The rules apply in order, so earlier rules may "feed" and "bleed" later
rules. Therefore, their sequence is *very important* and can be
leveraged in order to achieve valuable results.

Comments and blank lines
^^^^^^^^^^^^^^^^^^^^^^^^

Comments and blank lines (lines consisting only of white space) are
allowed to make your code more readable. Any line in which the first
non-whitespace character is a percent sign ``%`` is interpreted as
comment. The rest of the line is ignored when the file is interpreted.
Blank lines are also ignored.

A strategy for adding language support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Epitran uses a mapping-and-repairs approach to G2P. It is expected that
there is a mapping between graphemes and phonemes that can do most of
the work of converting orthographic representations to phonological
representations. In phonemically adequate orthogrphies, this mapping can
do *all* of the work. This mapping should be completed first. For many
languages, a basis for this mapping table already exists on
`Wikipedia <http://www.wikipedia.org>`__ and
`Omniglot <http://www.omniglot.com>`__ (though the Omniglot tables are
typically not machine readable).

On the other hand, many writing systems deviate from the phonemically
adequate idea. It is here that pre- and post-processors must be
introduced. For example, in Swedish, the letter receives a different
pronunciation before two consonants (/ɐ/) than elsewhere (/ɑː/). It
makes sense to add a preprocessor rule that rewrites as /ɐ/ before two
consonants (and similar rules for the other vowels, since they are
affected by the same condition). Preprocessor rules should generally be
employed whenever the orthographic representation must be adjusted (by
contextual changes, deletions, etc.) prior to the mapping step.

One common use for postprocessors is to eliminate characters that are
needed by the preprocessors or maps, but which should not appear in the
output. A classic example of this is the virama used in Indic scripts.
In these scripts, in order to write a consonant *not followed* by a
vowel, one uses the form of the consonant symbol with particular
inherent vowel followed by a virama (which has various names in
different Indic languages). An easy way of handling this is to allow the
mapping to translate the consonant into an IPA consonant + an inherent
vowel (which, for a given language, will always be the same), then use
the postprocessor to delete the vowel + virama sequence (wherever it
occurs).

In fact, any situation where a character that is introduced by the map
needs to be subsequently deleted is a good use-case for postprocessors.
Another example from Indian languages includes so-called schwa deletion.
Some vowels implied by a direct mapping between the orthography and the
phonology are not actually pronounced; these vowels can generally be
predicted. In most languages, they occur in the context after a
vowel+consonant sequence and before a consonant+vowel sequence. In other
words, the rule looks like the following:

::

    ə -> 0 / (::vowel::)(::consonant::) _ (::consonant::)(::vowel::)

Perhaps the best way to learn how to structure language support for a
new language is to consult the existing languages in Epitran. The French
preprocessor ``fra-Latn.txt`` and the Thai postprocessor
``tha-Thai.txt`` illustrate many of the use-cases for these rules.

Citing Epitran
==============

If you use Epitran in published work, or in other research, please use
the following citation:

David R. Mortensen, Siddharth Dalmia, and Patrick Littell. 2018.
Epitran: Precision G2P for many languages. In *Proceedings of the
Eleventh International Conference on Language Resources and Evaluation
(LREC 2018)*, Paris, France. European Language Resources Association
(ELRA).

``@InProceedings{Mortensen-et-al:2018,   author = {Mortensen, David R.  and Dalmia, Siddharth and Littell, Patrick},   title = {Epitran: Precision {G2P} for Many Languages},   booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},   year = {2018},   month = {May},   date = {7--12},   location = {Miyazaki, Japan},   editor = {Nicoletta Calzolari (Conference chair) and Khalid Choukri and Christopher Cieri and Thierry Declerck and Sara Goggi and Koiti Hasida and Hitoshi Isahara and Bente Maegaard and Joseph Mariani and H\'el\`ene Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis and Takenobu Tokunaga},   publisher = {European Language Resources Association (ELRA)},   address = {Paris, France},   isbn = {979-10-95546-00-9},   language = {english}   }``
