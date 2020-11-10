import unittest

from django_nlf.antlr import DjangoNLFLanguage, Lookup, Operation


class DjangoNLFListenerNestedExpressionsTestCase(unittest.TestCase):
    def setUp(self):
        self.nl_filter = DjangoNLFLanguage()

    def test_nested_at_start_no_other(self):
        expr = "(field is value and another_field equals another_value)"
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

    def test_nested_at_start_with_other(self):
        expr = "(field is value or field equals another_value) and another_field is another_value"
        expected = [
            [
                Operation.AND,
                [
                    Operation.OR,
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "value": "value",
                        "exclude": False,
                    },
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "value": "another_value",
                        "exclude": False,
                    },
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

    def test_nested_at_end(self):
        expr = (
            "field is value and (another_field equals another_value or another_field equals value)"
        )
        expected = [
            [
                Operation.AND,
                {
                    "field_name": "field",
                    "lookup": Lookup.EQUALS,
                    "value": "value",
                    "exclude": False,
                },
                [
                    Operation.OR,
                    {
                        "field_name": "another_field",
                        "lookup": Lookup.EQUALS,
                        "value": "another_value",
                        "exclude": False,
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

    def test_nested_at_end_with_precedence(self):
        expr = (
            "field is value or field is another_value and "
            "(another_field equals another_value or another_field equals value)"
        )
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
                        "value": "another_value",
                        "exclude": False,
                    },
                    [
                        Operation.OR,
                        {
                            "field_name": "another_field",
                            "lookup": Lookup.EQUALS,
                            "value": "another_value",
                            "exclude": False,
                        },
                        {
                            "field_name": "another_field",
                            "lookup": Lookup.EQUALS,
                            "value": "value",
                            "exclude": False,
                        },
                    ],
                ],
            ]
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)

    def test_two_nested_and_or_and(self):
        expr = (
            "(field is value and another_field equals another_value) or "
            "(field is another_value and another_field is value)"
        )
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
                [
                    Operation.AND,
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "value": "another_value",
                        "exclude": False,
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

    def test_two_nested_or_and_or(self):
        expr = (
            "(field is value or another_field equals another_value) and "
            "(field is another_value or another_field is value)"
        )
        expected = [
            [
                Operation.AND,
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
                        "value": "another_value",
                        "exclude": False,
                    },
                ],
                [
                    Operation.OR,
                    {
                        "field_name": "field",
                        "lookup": Lookup.EQUALS,
                        "value": "another_value",
                        "exclude": False,
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

    def test_three_nested_with_precedence(self):
        expr = (
            "(field is value and another_field equals another_value) or "
            "(field is another_value and another_field is value) and "
            "(yet_another_field is value and some_other_field is empty)"
        )
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
                [
                    Operation.AND,
                    [
                        Operation.AND,
                        {
                            "field_name": "field",
                            "lookup": Lookup.EQUALS,
                            "value": "another_value",
                            "exclude": False,
                        },
                        {
                            "field_name": "another_field",
                            "lookup": Lookup.EQUALS,
                            "value": "value",
                            "exclude": False,
                        },
                    ],
                    [
                        Operation.AND,
                        {
                            "field_name": "yet_another_field",
                            "lookup": Lookup.EQUALS,
                            "value": "value",
                            "exclude": False,
                        },
                        {
                            "field_name": "some_other_field",
                            "lookup": Lookup.EQUALS,
                            "value": "empty",
                            "exclude": False,
                        },
                    ],
                ],
            ]
        ]
        res = self.nl_filter.parse(expr)
        self.assertListEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
