
import os.path
from importlib import resources
from pathlib import Path

from . import rules


class Tir2PP:
    def __init__(self) -> None:
        fn = os.path.join('data', 'post', 'tir-Ethi-pp.txt')
        resource_path = resources.files(__package__).joinpath(fn)
        self.rules = rules.Rules([Path(str(resource_path))])

    def apply(self, word: str) -> str:
        word = word.replace('ɨ', '')
        return self.rules.apply(word)
