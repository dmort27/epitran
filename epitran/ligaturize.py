# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import


def ligaturize(text):
    """Convert text to employ non-standard ligatures

    Args:
        text (unicode): IPA text to Convert

    Return:
        unicode: non-standard IPA text with phonetic ligatures for affricates
    """
    mapping = [(u't͡s', u'ʦ'),
               (u't͡ʃ', u'ʧ'),
               (u't͡ɕ', u'ʨ'),
               (u'd͡z', u'ʣ'),
               (u'd͡ʒ', u'ʤ'),
               (u'd͡ʑ', u'ʥ'),]
    for from_, to_ in mapping:
        text = text.replace(from_, to_)
    return text
