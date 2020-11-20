import unittest

from django_nlf import (
    DjangoNLFLanguage,
    Lookup,
    Operation,
    Expression,
    CompositeExpression,
    CustomFunction,
)


class DjangoNLFListenerMultipleExpressionsTestCase(unittest.TestCase):
    def setUp(self):
        self.nl_filter = DjangoNLFLanguage()

    def test_two_exprs_and(self):
        expr = "field is value and another_field equals another_value"
        expected = CompositeExpression(
            Operation.AND,
            Expression(
                field="field",
                lookup=Lookup.EQUALS,
                value="value",
                exclude=False,
            ),
            Expression(
                field="another_field",
                lookup=Lookup.EQUALS,
                value="another_value",
                exclude=False,
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_two_exprs_or(self):
        expr = "field is value or another_field equals value"
        expected = CompositeExpression(
            Operation.OR,
            Expression(
                field="field",
                lookup=Lookup.EQUALS,
                value="value",
                exclude=False,
            ),
            Expression(
                field="another_field",
                lookup=Lookup.EQUALS,
                value="value",
                exclude=False,
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_three_exprs_all_and(self):
        expr = "field is value and another_field equals another_value and field equals yet_another_value"
        expected = CompositeExpression(
            Operation.AND,
            CompositeExpression(
                Operation.AND,
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    value="value",
                    exclude=False,
                ),
                Expression(
                    field="another_field",
                    lookup=Lookup.EQUALS,
                    value="another_value",
                    exclude=False,
                ),
            ),
            Expression(
                field="field",
                lookup=Lookup.EQUALS,
                value="yet_another_value",
                exclude=False,
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_three_exprs_all_or(self):
        expr = "field is value or another_field equals value or yet_another_field equals value"
        expected = CompositeExpression(
            Operation.OR,
            CompositeExpression(
                Operation.OR,
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    value="value",
                    exclude=False,
                ),
                Expression(
                    field="another_field",
                    lookup=Lookup.EQUALS,
                    value="value",
                    exclude=False,
                ),
            ),
            Expression(
                field="yet_another_field",
                lookup=Lookup.EQUALS,
                value="value",
                exclude=False,
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_three_exprs_and_or(self):
        expr = "field is value and another_field equals another_value or another_field equals value"
        expected = CompositeExpression(
            Operation.OR,
            CompositeExpression(
                Operation.AND,
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    value="value",
                    exclude=False,
                ),
                Expression(
                    field="another_field",
                    lookup=Lookup.EQUALS,
                    value="another_value",
                    exclude=False,
                ),
            ),
            Expression(
                field="another_field",
                lookup=Lookup.EQUALS,
                value="value",
                exclude=False,
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_three_exprs_or_and(self):
        expr = "field is value or field equals another_value and another_field equals value"
        expected = CompositeExpression(
            Operation.OR,
            Expression(
                field="field",
                lookup=Lookup.EQUALS,
                value="value",
                exclude=False,
            ),
            CompositeExpression(
                Operation.AND,
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    exclude=False,
                    value="another_value",
                ),
                Expression(
                    field="another_field",
                    lookup=Lookup.EQUALS,
                    value="value",
                    exclude=False,
                ),
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_four_exprs_and_or_and(self):
        expr = (
            "field is value and another_field equals another_value or "
            "another_field equals value and field is another_value"
        )
        expected = CompositeExpression(
            Operation.OR,
            CompositeExpression(
                Operation.AND,
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    exclude=False,
                    value="value",
                ),
                Expression(
                    field="another_field",
                    lookup=Lookup.EQUALS,
                    value="another_value",
                    exclude=False,
                ),
            ),
            CompositeExpression(
                Operation.AND,
                Expression(
                    field="another_field",
                    lookup=Lookup.EQUALS,
                    exclude=False,
                    value="value",
                ),
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    value="another_value",
                    exclude=False,
                ),
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_four_exprs_or_and_or(self):
        expr = (
            "field is value or field equals another_value and "
            "another_field equals value or another_field equals another_value"
        )
        expected = CompositeExpression(
            Operation.OR,
            CompositeExpression(
                Operation.OR,
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    value="value",
                    exclude=False,
                ),
                CompositeExpression(
                    Operation.AND,
                    Expression(
                        field="field",
                        lookup=Lookup.EQUALS,
                        exclude=False,
                        value="another_value",
                    ),
                    Expression(
                        field="another_field",
                        lookup=Lookup.EQUALS,
                        value="value",
                        exclude=False,
                    ),
                ),
            ),
            Expression(
                field="another_field",
                lookup=Lookup.EQUALS,
                value="another_value",
                exclude=False,
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_four_exprs_with_function_and_boolean_expr(self):
        expr = (
            "field is value or field matches function(multiple, params) and "
            'is not archived or not anotherFunction("quoted param")'
        )
        expected = CompositeExpression(
            Operation.OR,
            CompositeExpression(
                Operation.OR,
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    value="value",
                    exclude=False,
                ),
                CompositeExpression(
                    Operation.AND,
                    Expression(
                        field="field",
                        lookup=Lookup.REGEX,
                        value=CustomFunction("function", ["multiple", "params"]),
                        exclude=False,
                    ),
                    Expression(
                        field="archived",
                        lookup=Lookup.EQUALS,
                        value=False,
                        exclude=False,
                    ),
                ),
            ),
            CustomFunction("anotherFunction", ["quoted param"], {"exclude": True}),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
