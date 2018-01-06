from filter_rule import FilterRule


class FilterProcessor:

    def __init__(self, rules):
        '''
        Create filter processor with rules
        :param rules: Collection of rules as dict (described in README)
        '''
        self.rules = [FilterRule(rule) for rule in rules]

    def process(self, docs):
        left = []
        filtered_out = []
        for doc in docs:
            if any(rule.match(doc) for rule in self.rules):
                filtered_out.append(doc)
                continue
            left.append(doc)
        return left