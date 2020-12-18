from django.test import override_settings

from .models import Article, Publication
from .utils import BaseTestCase


class DjangoNLFilterSimpleTestCase(BaseTestCase):
    def test_simple_quoted_text_filter(self):
        filter_expr = 'title is "Science News"'
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.first(), self.p2)

    def test_simple_text_filter(self):
        filter_expr = "title contains science"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 2)
        self.assertListEqual(list(qs.all()), [self.p2, self.p3])

    def test_composite_text_filter_or(self):
        filter_expr = "title contains news or title contains journal"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 2)
        self.assertListEqual(list(qs.all()), [self.p2, self.p1])

    def test_negated_composite_text_filter_and(self):
        filter_expr = "title contains science and title does not contain news"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.p3)

    def test_valid_choices_filter(self):
        filter_expr = "category is printed"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.p3)

    def test_invalid_choices_filter(self):
        filter_expr = "category is online"
        with self.assertRaises(ValueError):
            self.nl_filter.filter(Publication.objects.all(), filter_expr)

    def test_simple_decimal_filter(self):
        filter_expr = "subscription_fee >= 2.12"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.p3)

    def test_composite_decimal_filter(self):
        filter_expr = "subscription_fee >= 1.12 and subscription_fee < 10"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.p1)

    def test_negated_composite_filter(self):
        filter_expr = "not subscription_fee >= 1.12 and subscription_fee < 10"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.p2)

    def test_negated_nested_filter(self):
        filter_expr = "not (subscription_fee >= 1.12 and subscription_fee < 10)"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 2)
        self.assertListEqual(list(qs.all()), [self.p2, self.p3])

    def test_float_filter(self):
        filter_expr = "market_share >= 0.2"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.p1)

    def test_text_field_filter(self):
        filter_expr = "body contains NASA"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.a2)

    def test_empty_text_filter_01(self):
        filter_expr = 'body is ""'
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.a4)

    def test_empty_text_filter_02(self):
        filter_expr = "body is EMPTY"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.a3)

    def test_date_filter(self):
        filter_expr = "created_at > 2016-05-01"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.a4)

    def test_integer_filter(self):
        filter_expr = "views > 10000"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.a1)

    def test_boolean_filter_true(self):
        filter_expr = "archived is true"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.a3)

    def test_boolean_filter_false(self):
        filter_expr = "archived is false"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 3)

    def test_boolean_filter_true_alt(self):
        filter_expr = "is archived"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.a3)

    def test_boolean_filter_false_alt(self):
        filter_expr = "is not archived"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 3)

    def test_foreignkey_filter_01(self):
        filter_expr = "author.is_active is false"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 0)

    def test_foreignkey_filter_02(self):
        filter_expr = "author.username is jfields"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)

    def test_forward_many_to_many_filter(self):
        filter_expr = "publications.title contains science"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 2)
        self.assertListEqual(list(qs.all()), [self.a2, self.a3])

    def test_backward_many_to_many_filter(self):
        filter_expr = "articles.views > 10000 or articles.views < 5000"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 2)
        self.assertListEqual(list(qs.all()), [self.p2, self.p1])


class DjangoNLFilterShortcutsTestCase(BaseTestCase):
    def test_model_shortcuts(self):
        self.nl_filter.field_shortcuts = {"tests.Publication": {"views": "articles.views"}}
        filter_expr = "views > 10000 or views < 5000"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 2)
        self.assertListEqual(list(qs.all()), [self.p2, self.p1])

    def test_generic_shortcuts(self):
        self.nl_filter.field_shortcuts = {"__all__": {"views": "articles.views"}}
        filter_expr = "views > 10000 or views < 5000"
        qs = self.nl_filter.filter(Publication.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 2)
        self.assertListEqual(list(qs.all()), [self.p2, self.p1])


class DjangoNLFilterConverterTestCase(BaseTestCase):
    @override_settings(NLF_FIELD_NAME_CONVERTER="django_nlf.utils.camel_to_snake_case")
    def test_camel_case_fields(self):
        filter_expr = "createdAt > 2016-05-01"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first(), self.a4)
