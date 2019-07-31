import epitran

class DictFirst:
    """If words are in a dictionary, use one model; if words are not, use another fallback.
     
    Args:
        code1 (str): language-script code for dictionary language
        code2 (str): language-script code for fall-back language
        dict_fn (str): file path to text file containing dictionary, one word per line
    """
    def __init__(self, code1, code2, dict_fn):
        self.epi1 = epitran.Epitran(code1)
        self.epi2 = epitran.Epitran(code2)
        self.dictionary = self._read_dictionary(dict_fn)

    def _read_dictionary(self, dict_fn):
        with open(dict_fn, encoding='utf-8') as f:
            return {x.strip(): self.epi1.transliterate(x.strip()) for x in f}

    def transliterate(self, token):
        """Convert token to IPA, falling back on second language

        Args:
            token (str): token to covert to IPA

        Returns:
            str: IPA equivalent of token
        """
        if token in self.dictionary:
            return self.dictionary[token]
        else:
            return self.epi2.transliterate(token)
