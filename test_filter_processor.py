from unittest import TestCase
from filter_processor import FilterProcessor


class FilterProcessorTest(TestCase):

    programming_languages = [
        {"langugage": "Java", "static_typed": "true"},
        {"langugage": "Python", "static_typed": "false"},
        {"langugage": "Delphi", "static_typed": "true"}
    ]

    def test_filter_processor_given_no_rules_removes_nothing(self):
        processor = FilterProcessor([])
        filtered = processor.process(self.programming_languages)
        self.assertListEqual(self.programming_languages, filtered)

