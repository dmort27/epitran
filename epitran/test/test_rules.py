import tempfile
import unittest
from pathlib import Path

from epitran.rules import Rules


class TestRules(unittest.TestCase):
    def _rules(self, text):
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        rule_file = Path(temporary_directory.name) / 'rules.txt'
        rule_file.write_text(text, encoding='utf-8')
        return Rules([rule_file])

    def test_replacement_applies_more_than_32_times(self):
        rules = self._rules('a -> b / _\n')
        self.assertEqual(rules.apply('a' * 40), 'b' * 40)

    def test_metathesis_applies_more_than_32_times(self):
        rules = self._rules('(?P<sw1>a)(?P<sw2>b) -> 0 / _\n')
        self.assertEqual(rules.apply('ab' * 40), 'ba' * 40)
