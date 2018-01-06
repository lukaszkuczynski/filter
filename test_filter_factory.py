from filter_rule import FilterFactory, FilterContainsTextRule
from unittest import TestCase

class FilterFactoryTest(TestCase):

    def test_filter_factory_returns_contains_text_filter(self):
        json_rule = {
            "type": "contains_text"
        }
        filter = FilterFactory().for_rule(json_rule)
        self.assertIsInstance(filter, FilterContainsTextRule)

    def test_filter_factory_given_no_type_returns_meaningful_error(self):
        json_rule = {

        }
        try:
            FilterFactory().for_rule(json_rule)
            self.fail("should not go here")
        except Exception as e:
            self.assertIn("Rule definition should contain 'type' field", e.__str__())

    def test_filter_factory_given_undefined_type_returns_meaningful_error(self):
        json_rule = {
            "type": "UNKNOWN"
        }
        try:
            FilterFactory().for_rule(json_rule)
            self.fail("should not go here")
        except Exception as e:
            self.assertIn("Filter rule of 'UNKNOWN' type is not defined", e.__str__())
