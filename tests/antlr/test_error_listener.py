import unittest

from django_nlf.antlr import DjangoNLFLanguage, LanguageSyntaxError


class DjangoNLFListenerSingleExpressionTestCase(unittest.TestCase):
    def setUp(self):
        self.nl_filter = DjangoNLFLanguage()

    def test_invalid_lookups(self):
        expressions = ["space in filed name equals value", "field in"]
        for expr in expressions:
            with self.assertRaises(LanguageSyntaxError):
                self.nl_filter.parse(expr)
