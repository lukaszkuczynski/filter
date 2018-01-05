from abc import abstractmethod


class FilterRule:

    def __init__(self, config):
        self.config = config


    @abstractmethod
    def match(self, doc):
        pass


class FilterContainsTextRule(FilterRule):

    def match(self, doc):
        for key in doc.keys():
            if key in self.config['fields']:
                pattern_for_field = self.config['fields'][key]
                return pattern_for_field in doc[key]


class FilterFactory:

    def for_rule(self, rule):
        if rule['type'] == 'contains_text':
            return FilterContainsTextRule(rule)