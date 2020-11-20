import unittest

from django_nlf import (
    DjangoNLFLanguage,
    Lookup,
    Operation,
    Expression,
    CompositeExpression,
    CustomFunction,
)


class DjangoNLFListenerNestedExpressionsTestCase(unittest.TestCase):
    def setUp(self):
        self.nl_filter = DjangoNLFLanguage()

    def test_nested_at_start_no_other(self):
        expr = "(field is value and another_field equals another_value)"
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

    def test_nested_at_start_with_other(self):
        expr = "(field is value or field equals another_value) and another_field is another_value"
        expected = CompositeExpression(
            Operation.AND,
            CompositeExpression(
                Operation.OR,
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    value="value",
                    exclude=False,
                ),
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    value="another_value",
                    exclude=False,
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

    def test_nested_at_end(self):
        expr = (
            "field is value and (another_field equals another_value or another_field equals value)"
        )
        expected = CompositeExpression(
            Operation.AND,
            Expression(
                field="field",
                lookup=Lookup.EQUALS,
                value="value",
                exclude=False,
            ),
            CompositeExpression(
                Operation.OR,
                Expression(
                    field="another_field",
                    lookup=Lookup.EQUALS,
                    value="another_value",
                    exclude=False,
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

    def test_nested_at_end_with_precedence(self):
        expr = (
            "field is value or field is another_value and "
            "(another_field equals another_value or another_field equals value)"
        )
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
                    value="another_value",
                    exclude=False,
                ),
                CompositeExpression(
                    Operation.OR,
                    Expression(
                        field="another_field",
                        lookup=Lookup.EQUALS,
                        value="another_value",
                        exclude=False,
                    ),
                    Expression(
                        field="another_field",
                        lookup=Lookup.EQUALS,
                        value="value",
                        exclude=False,
                    ),
                ),
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_two_nested_and_or_and(self):
        expr = (
            "(field is value and another_field equals another_value) or "
            "(field is another_value and another_field is value)"
        )
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
            CompositeExpression(
                Operation.AND,
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    value="another_value",
                    exclude=False,
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

    def test_two_nested_or_and_or(self):
        expr = (
            "(field is value or another_field equals another_value) and "
            "(field is another_value or another_field is value)"
        )
        expected = CompositeExpression(
            Operation.AND,
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
                    value="another_value",
                    exclude=False,
                ),
            ),
            CompositeExpression(
                Operation.OR,
                Expression(
                    field="field",
                    lookup=Lookup.EQUALS,
                    value="another_value",
                    exclude=False,
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

    def test_three_nested_with_precedence(self):
        expr = (
            "(field is value and another_field equals another_value) or "
            "(field is another_value and another_field is value) and "
            "(yet_another_field is value and some_other_field is empty)"
        )
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
            CompositeExpression(
                Operation.AND,
                CompositeExpression(
                    Operation.AND,
                    Expression(
                        field="field",
                        lookup=Lookup.EQUALS,
                        value="another_value",
                        exclude=False,
                    ),
                    Expression(
                        field="another_field",
                        lookup=Lookup.EQUALS,
                        value="value",
                        exclude=False,
                    ),
                ),
                CompositeExpression(
                    Operation.AND,
                    Expression(
                        field="yet_another_field",
                        lookup=Lookup.EQUALS,
                        value="value",
                        exclude=False,
                    ),
                    Expression(
                        field="some_other_field",
                        lookup=Lookup.EQUALS,
                        value="empty",
                        exclude=False,
                    ),
                ),
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_three_nested_deeply_with_precedence(self):
        expr = (
            "(field is value and another_field equals another_value) and "
            "((field is another_value and another_field is value) or "
            "(yet_another_field is value and some_other_field is empty))"
        )
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
            CompositeExpression(
                Operation.OR,
                CompositeExpression(
                    Operation.AND,
                    Expression(
                        field="field",
                        lookup=Lookup.EQUALS,
                        value="another_value",
                        exclude=False,
                    ),
                    Expression(
                        field="another_field",
                        lookup=Lookup.EQUALS,
                        value="value",
                        exclude=False,
                    ),
                ),
                CompositeExpression(
                    Operation.AND,
                    Expression(
                        field="yet_another_field",
                        lookup=Lookup.EQUALS,
                        value="value",
                        exclude=False,
                    ),
                    Expression(
                        field="some_other_field",
                        lookup=Lookup.EQUALS,
                        value="empty",
                        exclude=False,
                    ),
                ),
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_three_nested_deeply_negated(self):
        expr = (
            "(field is value and another_field equals another_value) and not "
            "((field is another_value and another_field is value) or "
            "(yet_another_field is not value and some_other_field is empty))"
        )
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
            CompositeExpression(
                Operation.AND,
                CompositeExpression(
                    Operation.OR,
                    Expression(
                        field="field",
                        lookup=Lookup.EQUALS,
                        value="another_value",
                        exclude=True,
                    ),
                    Expression(
                        field="another_field",
                        lookup=Lookup.EQUALS,
                        value="value",
                        exclude=True,
                    ),
                ),
                CompositeExpression(
                    Operation.OR,
                    Expression(
                        field="yet_another_field",
                        lookup=Lookup.EQUALS,
                        value="value",
                        exclude=False,
                    ),
                    Expression(
                        field="some_other_field",
                        lookup=Lookup.EQUALS,
                        value="empty",
                        exclude=True,
                    ),
                ),
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_three_nested_with_function_and_boolean_expr(self):
        expr = (
            "(field is value and is not archived) or "
            "(field is another_value and another_field >= startOfWeek()) and "
            "(yet_another_field is value and hasChildren())"
        )
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
                    field="archived",
                    lookup=Lookup.EQUALS,
                    value=False,
                    exclude=False,
                ),
            ),
            CompositeExpression(
                Operation.AND,
                CompositeExpression(
                    Operation.AND,
                    Expression(
                        field="field",
                        lookup=Lookup.EQUALS,
                        value="another_value",
                        exclude=False,
                    ),
                    Expression(
                        field="another_field",
                        lookup=Lookup.GTE,
                        value=CustomFunction("startOfWeek", []),
                        exclude=False,
                    ),
                ),
                CompositeExpression(
                    Operation.AND,
                    Expression(
                        field="yet_another_field",
                        lookup=Lookup.EQUALS,
                        value="value",
                        exclude=False,
                    ),
                    CustomFunction("hasChildren", [], {"exclude": False}),
                ),
            ),
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
