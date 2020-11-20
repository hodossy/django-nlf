import unittest

from django_nlf import DjangoNLFLanguage, Lookup, Expression, CustomFunction


class DjangoNLFListenerSingleExpressionTestCase(unittest.TestCase):
    def setUp(self):
        self.nl_filter = DjangoNLFLanguage()

    def test_empty_expr(self):
        expr = ""
        expected = []
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_new_line_ignores(self):
        expressions = [
            "\nfield\tis\r\nvalue",
            "field        equals\r\n\r\n\r\nvalue",
            "field=value\n\n\t",
        ]
        expected = Expression(
            field="field",
            lookup=Lookup.EQUALS,
            value="value",
            exclude=False,
        )
        for expr in expressions:
            res = self.nl_filter.parse(expr)
            self.assertEqual(res, expected)

    def test_equals(self):
        expressions = [
            "field is value",
            "field equals value",
            "field=value",
            "field = value",
            "not field is not value",
        ]
        expected = Expression(
            field="field",
            lookup=Lookup.EQUALS,
            value="value",
            exclude=False,
        )
        for expr in expressions:
            res = self.nl_filter.parse(expr)
            self.assertEqual(res, expected)

    def test_not_equals(self):
        expressions = [
            "field is not value",
            "field does not equal value",
            "field!=value",
            "field != value",
            "not field is value",
        ]
        expected = Expression(
            field="field",
            lookup=Lookup.EQUALS,
            value="value",
            exclude=True,
        )
        for expr in expressions:
            res = self.nl_filter.parse(expr)
            self.assertEqual(res, expected)

    def test_contains(self):
        expr = "field contains value"
        expected = Expression(
            field="field",
            lookup=Lookup.CONTAINS,
            value="value",
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_ncontains(self):
        expressions = ["field does not contain value", "field do not contain value"]
        expected = Expression(
            field="field",
            lookup=Lookup.CONTAINS,
            value="value",
            exclude=True,
        )
        for expr in expressions:
            res = self.nl_filter.parse(expr)
            self.assertEqual(res, expected)

    def test_regex(self):
        # TODO: Make this work
        # regex = r"/^(?:[^\d\S].*|([cfdrp][^a].*)|[\w]a[^n].*|.{4,}|.{0,2})$/"
        regex = "value"
        expressions = [f"field matches {regex}", f"field~{regex}", f"field ~ {regex}"]
        expected = Expression(
            field="field",
            lookup=Lookup.REGEX,
            value=f"{regex}",
            exclude=False,
        )
        for expr in expressions:
            res = self.nl_filter.parse(expr)
            self.assertEqual(res, expected)

    def test_nregex(self):
        expressions = ["field does not match value", "field!~value", "field !~ value"]
        expected = Expression(
            field="field",
            lookup=Lookup.REGEX,
            value="value",
            exclude=True,
        )
        for expr in expressions:
            res = self.nl_filter.parse(expr)
            self.assertEqual(res, expected)

    def test_in(self):
        expr = "field in value"
        expected = Expression(
            field="field",
            lookup=Lookup.IN,
            value="value",
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_in_multiple_values(self):
        expr = 'field in (value, another_value, "quoted value")'
        expected = Expression(
            field="field",
            lookup=Lookup.IN,
            value=["value", "another_value", "quoted value"],
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_nin(self):
        expr = "field not in value"
        expected = Expression(
            field="field",
            lookup=Lookup.IN,
            value="value",
            exclude=True,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_gt(self):
        expr = "field > value"
        expected = Expression(
            field="field",
            lookup=Lookup.GT,
            value="value",
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_gte(self):
        expr = "field >= value"
        expected = Expression(
            field="field",
            lookup=Lookup.GTE,
            value="value",
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_lt(self):
        expr = "field < value"
        expected = Expression(
            field="field",
            lookup=Lookup.LT,
            value="value",
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_lte(self):
        expr = "field <= value"
        expected = Expression(
            field="field",
            lookup=Lookup.LTE,
            value="value",
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_custom_function_as_value(self):
        expr = "field in myFunction(param)"
        expected = Expression(
            field="field",
            lookup=Lookup.IN,
            value=CustomFunction("myFunction", ["param"]),
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_custom_function_as_expression(self):
        expr = "myFunction(param)"
        expected = CustomFunction("myFunction", ["param"], {"exclude": False})
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_custom_function_multiple_args_as_value(self):
        expr = 'field in myFunction(param, "another param", param2)'
        expected = Expression(
            field="field",
            lookup=Lookup.IN,
            value=CustomFunction("myFunction", ["param", "another param", "param2"]),
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_custom_function_multiple_args_as_expression(self):
        expr = 'myFunction(param, "another param", param2)'
        expected = CustomFunction(
            "myFunction", ["param", "another param", "param2"], {"exclude": False}
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_simplified_boolean(self):
        expr = "is archived"
        expected = Expression(
            field="archived",
            lookup=Lookup.EQUALS,
            value=True,
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_simplified_boolean_not(self):
        expr = "is not archived"
        expected = Expression(
            field="archived",
            lookup=Lookup.EQUALS,
            value=False,
            exclude=False,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)

    def test_negated_equals(self):
        expr = "not field is value"
        expected = Expression(
            field="field",
            lookup=Lookup.EQUALS,
            value="value",
            exclude=True,
        )
        res = self.nl_filter.parse(expr)
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
