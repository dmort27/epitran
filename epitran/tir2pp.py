# -*- coding: utf-8 -*-

import os.path

import pkg_resources
from . import rules


class Tir2PP(object):
    def __init__(self) -> None:
        fn = os.path.join('data', 'post', 'tir-Ethi-pp.txt')
        fn = pkg_resources.resource_filename(__name__, fn)
        self.rules = rules.Rules([fn])

    def apply(self, word: str) -> str:
        word = word.replace('ɨ', '')
        return self.rules.apply(word)
