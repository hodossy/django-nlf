import unittest

from django_nlf.antlr import DjangoNLFilter, Lookup


class DjangoNLFListenerSingleExpressionTestCase(unittest.TestCase):
    def setUp(self):
        self.nl_filter = DjangoNLFilter()

    def test_equals(self):
        expressions = ["field is value", "field equals value", "field=value"]
        expected = [
            {
                "field_name": "field",
                "lookup": Lookup.EQUALS,
                "value": "value",
                "exclude": False,
            }
        ]
        for expr in expressions:
            res = self.nl_filter.parse(expr)
            self.assertListEqual(res, expected)

    def test_not_equals(self):
        expressions = ["field is not value", "field not equals value", "field!=value"]
        expected = [
            {
                "field_name": "field",
                "lookup": Lookup.EQUALS,
                "value": "value",
                "exclude": True,
            }
        ]
        for expr in expressions:
            res = self.nl_filter.parse(expr)
            self.assertListEqual(res, expected)

    def test_like(self):
        expressions = ["field is like value", "field ~ value"]
        expected = [
            {
                "field_name": "field",
                "lookup": Lookup.LIKE,
                "value": "value",
                "exclude": False,
            }
        ]
        for expr in expressions:
            res = self.nl_filter.parse(expr)
            self.assertListEqual(res, expected)

    def test_nlike(self):
        expressions = ["field is not like value", "field!~value"]
        expected = [
            {
                "field_name": "field",
                "lookup": Lookup.LIKE,
                "value": "value",
                "exclude": True,
            }
        ]
        for expr in expressions:
            res = self.nl_filter.parse(expr)
            self.assertListEqual(res, expected)

    def test_in(self):
        expr = "field in value"
        expected = [
            {
                "field_name": "field",
                "lookup": Lookup.IN,
                "value": "value",
                "exclude": False,
            }
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_nin(self):
        expr = "field not in value"
        expected = [
            {
                "field_name": "field",
                "lookup": Lookup.IN,
                "value": "value",
                "exclude": True,
            }
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_gt(self):
        expr = "field > value"
        expected = [
            {
                "field_name": "field",
                "lookup": Lookup.GT,
                "value": "value",
                "exclude": False,
            }
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_gte(self):
        expr = "field >= value"
        expected = [
            {
                "field_name": "field",
                "lookup": Lookup.GTE,
                "value": "value",
                "exclude": False,
            }
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_lt(self):
        expr = "field < value"
        expected = [
            {
                "field_name": "field",
                "lookup": Lookup.LT,
                "value": "value",
                "exclude": False,
            }
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_lte(self):
        expr = "field <= value"
        expected = [
            {
                "field_name": "field",
                "lookup": Lookup.LTE,
                "value": "value",
                "exclude": False,
            }
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
