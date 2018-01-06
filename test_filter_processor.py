from unittest import TestCase
from filter_processor import FilterProcessor


class FilterProcessorTest(TestCase):

    programming_languages = [
        {"language": "Java", "static_typed": "true"},
        {"language": "Python", "static_typed": "false"},
        {"language": "Delphi", "static_typed": "true"}
    ]

    def test_filter_processor_given_no_rules_removes_nothing(self):
        processor = FilterProcessor([])
        filtered = processor.process(self.programming_languages)
        self.assertListEqual(self.programming_languages, filtered)

    def test_filter_processor_removes_docs_according_to_rules(self):
        rules = [
            {
                "name": "only_static",
                "type": "contains_text",
                "fields": {
                    "static_typed": "true"
                }
            }
        ]
        processor = FilterProcessor(rules)
        left, removed = processor.process(self.programming_languages)
        self.assertEquals(len(left), 1)
        self.assertEquals(left[0]['language'], "Python")
