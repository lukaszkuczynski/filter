from unittest import TestCase
from filter_rule import FilterContainsTextRule

class TestFilterContainsText(TestCase):

    def test_contains_should_match(self):
        rule = {
            "name": "find_Luke",
            "type": "contains_text",
            "fields": {
              "name": "Luk"
            }
        }
        filter = FilterContainsTextRule(rule)
        self.assertTrue(filter.match({
            "name": "Luke Skywalker"
        }));
        self.assertFalse(filter.match({
            "name": "Darth Vader"
        }));