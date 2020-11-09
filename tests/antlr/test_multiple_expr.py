import unittest

from django_nlf.antlr import DjangoNLFilter, Lookup, Operation


class DjangoNLFListenerMultipleExpressionsTestCase(unittest.TestCase):
    def setUp(self):
        self.nl_filter = DjangoNLFilter()

    def test_two_exprs_and(self):
        expr = "field is value and another_field equals another_value"
        expected = [
            [
                Operation.AND,
                {
                    "field_name": "field",
                    "lookup": Lookup.EQUALS,
                    "value": "value",
                    "exclude": False,
                },
                {
                    "field_name": "another_field",
                    "lookup": Lookup.EQUALS,
                    "value": "another_value",
                    "exclude": False,
                },
            ]
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_two_exprs_or(self):
        expr = "field is value or another_field equals value"
        expected = [
            [
                Operation.OR,
                {
                    "field_name": "field",
                    "lookup": Lookup.EQUALS,
                    "value": "value",
                    "exclude": False,
                },
                {
                    "field_name": "another_field",
                    "lookup": Lookup.EQUALS,
                    "value": "value",
                    "exclude": False,
                },
            ]
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_three_exprs_all_and(self):
        expr = "field is value and another_field equals another_value and field equals yet_another_value"
        expected = [
            [
                Operation.AND,
                [
                    Operation.AND,
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "value": "value",
                        "exclude": False,
                    },
                    {
                        "field_name": "another_field",
                        "lookup": Lookup.EQUALS,
                        "value": "another_value",
                        "exclude": False,
                    },
                ],
                {
                    "field_name": "field",
                    "lookup": Lookup.EQUALS,
                    "value": "yet_another_value",
                    "exclude": False,
                },
            ]
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_three_exprs_all_or(self):
        expr = "field is value or another_field equals value or yet_another_field equals value"
        expected = [
            [
                Operation.OR,
                [
                    Operation.OR,
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "value": "value",
                        "exclude": False,
                    },
                    {
                        "field_name": "another_field",
                        "lookup": Lookup.EQUALS,
                        "value": "value",
                        "exclude": False,
                    },
                ],
                {
                    "field_name": "yet_another_field",
                    "lookup": Lookup.EQUALS,
                    "value": "value",
                    "exclude": False,
                },
            ]
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_three_exprs_and_or(self):
        expr = "field is value and another_field equals another_value or another_field equals value"
        expected = [
            [
                Operation.OR,
                [
                    Operation.AND,
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "value": "value",
                        "exclude": False,
                    },
                    {
                        "field_name": "another_field",
                        "lookup": Lookup.EQUALS,
                        "value": "another_value",
                        "exclude": False,
                    },
                ],
                {
                    "field_name": "another_field",
                    "lookup": Lookup.EQUALS,
                    "value": "value",
                    "exclude": False,
                },
            ]
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_three_exprs_or_and(self):
        expr = "field is value or field equals another_value and another_field equals value"
        expected = [
            [
                Operation.OR,
                {
                    "field_name": "field",
                    "lookup": Lookup.EQUALS,
                    "value": "value",
                    "exclude": False,
                },
                [
                    Operation.AND,
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "exclude": False,
                        "value": "another_value",
                    },
                    {
                        "field_name": "another_field",
                        "lookup": Lookup.EQUALS,
                        "value": "value",
                        "exclude": False,
                    },
                ],
            ]
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_four_exprs_and_or_and(self):
        expr = (
            "field is value and another_field equals another_value or "
            "another_field equals value and field is another_value"
        )
        expected = [
            [
                Operation.OR,
                [
                    Operation.AND,
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "exclude": False,
                        "value": "value",
                    },
                    {
                        "field_name": "another_field",
                        "lookup": Lookup.EQUALS,
                        "value": "another_value",
                        "exclude": False,
                    },
                ],
                [
                    Operation.AND,
                    {
                        "field_name": "another_field",
                        "lookup": Lookup.EQUALS,
                        "exclude": False,
                        "value": "value",
                    },
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "value": "another_value",
                        "exclude": False,
                    },
                ],
            ]
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_four_exprs_or_and_or(self):
        expr = (
            "field is value or field equals another_value and "
            "another_field equals value or another_field equals another_value"
        )
        expected = [
            [
                Operation.OR,
                [
                    Operation.OR,
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "value": "value",
                        "exclude": False,
                    },
                    [
                        Operation.AND,
                        {
                            "field_name": "field",
                            "lookup": Lookup.EQUALS,
                            "exclude": False,
                            "value": "another_value",
                        },
                        {
                            "field_name": "another_field",
                            "lookup": Lookup.EQUALS,
                            "value": "value",
                            "exclude": False,
                        },
                    ],
                ],
                {
                    "field_name": "another_field",
                    "lookup": Lookup.EQUALS,
                    "value": "another_value",
                    "exclude": False,
                },
            ]
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
