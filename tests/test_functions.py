from unittest import TestCase

from django_nlf.functions import FunctionRegistry
from django_nlf.types import FunctionRole

from .models import Article, Publication
from .utils import BaseTestCase

# register functions by importing them
from .filter_functions import *


class DjangoNLFilterFunctionsTestCase(BaseTestCase):
    def test_unknown_function(self):
        filter_expr = "unknownFn()"
        with self.assertRaises(AttributeError):
            self.nl_filter.filter(Article.objects.all(), filter_expr)

    def test_function_as_value(self):
        filter_expr = "created_at > startOfWeek()"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertListEqual(list(qs.all()), [self.a4])

    def test_function_as_field(self):
        filter_expr = "totalViews() > 10000"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertListEqual(list(qs.all()), [self.p1])

    def test_function_as_field_on_wrong_model(self):
        filter_expr = "totalViews() > 10000"
        with self.assertRaises(ValueError):
            self.nl_filter.filter(Article.objects.all(), filter_expr)

    def test_function_wrong_role(self):
        filter_expr = "market_share < totalViews()"
        with self.assertRaises(ValueError):
            self.nl_filter.filter(Publication.objects.all(), filter_expr)

    def test_function_as_expression_no_params(self):
        filter_expr = "hasBeenPublished()"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 3)
        self.assertListEqual(list(qs.all()), [self.a1, self.a2, self.a3])

    def test_function_as_expression_no_params_negated(self):
        filter_expr = "not hasBeenPublished()"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertListEqual(list(qs.all()), [self.a4])

    def test_function_as_expression_one_param(self):
        filter_expr = 'hasBeenPublished("The Python Journal")'
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 2)
        self.assertListEqual(list(qs.all()), [self.a1, self.a2])

    def test_function_as_expression_with_param(self):
        filter_expr = 'hasBeenPublished("The Python Journal", "Science News")'
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 3)
        self.assertListEqual(list(qs.all()), [self.a1, self.a2, self.a3])


class FunctionRegistryTestCase(TestCase):
    DATE_FUNCTIONS = [
        ("startOfWeek", ""),
        ("startOfMonth", ""),
        ("startOfYear", ""),
    ]

    def test_get_functions_for_article(self):
        functions = FunctionRegistry.get_functions_for(Article)
        self.assertListEqual(functions[FunctionRole.VALUE], self.DATE_FUNCTIONS)
        self.assertListEqual(functions[FunctionRole.EXPRESSION], [("hasBeenPublished", "")])

    def test_get_functions_for_publication(self):
        functions = FunctionRegistry.get_functions_for(Publication)
        self.assertListEqual(functions[FunctionRole.VALUE], self.DATE_FUNCTIONS)
        self.assertListEqual(functions[FunctionRole.FIELD], [("totalViews", "")])
