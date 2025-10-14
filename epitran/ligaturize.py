# -*- coding: utf-8 -*-



def ligaturize(text: str) -> str:
    """Convert text to employ non-standard ligatures

    Args:
        text (str): IPA text to Convert

    Return:
        str: non-standard IPA text with phonetic ligatures for affricates
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
