
# Mapping from decomposed affricate sequences to precomposed ligature characters.
# Each tuple maps an IPA affricate (e.g., t͡s) to its precomposed form (e.g., ʦ).
AFFRICATE_LIGATURES = (
    (u't͡s', u'ʦ'),
    (u't͡ʃ', u'ʧ'),
    (u't͡ɕ', u'ʨ'),
    (u'd͡z', u'ʣ'),
    (u'd͡ʒ', u'ʤ'),
    (u'd͡ʑ', u'ʥ'),
)


def convert_affricates_to_ligatures(text: str) -> str:
    """Convert IPA affricate sequences to their precomposed ligature forms.

    Replaces decomposed affricate representations (e.g., "t͡s") with their
    precomposed Unicode ligatures (e.g., "ʦ"). This is useful for conventions
    that prefer compact affricate symbols over the decomposed form.

    Args:
        text (str): IPA text potentially containing decomposed affricates

    Return:
        str: IPA text with affricates converted to precomposed ligatures
    """
    for from_, to_ in AFFRICATE_LIGATURES:
        text = text.replace(from_, to_)
    return text


# Backward-compatible alias
ligaturize = convert_affricates_to_ligatures
