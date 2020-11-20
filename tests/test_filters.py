from django.contrib.auth.models import User
from django.test import TestCase

from django_nlf.filters.django import DjangoNLFilter
from .models import Article, Publication


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nl_filter = DjangoNLFilter()

        cls.p1 = Publication(title="The Python Journal", subscription_fee=1.99, market_share=0.254)
        cls.p1.save()
        cls.p2 = Publication(title="Science News", subscription_fee=0.99, market_share=0.04)
        cls.p2.save()
        cls.p3 = Publication(
            title="Science Weekly",
            category=Publication.PRINTED,
            subscription_fee=12.49,
            market_share=0.17,
        )
        cls.p3.save()

        cls.author1 = User.objects.create(
            username="jfields",
            first_name="Janie",
            last_name="Fields",
            email="janie.fields@django.org",
        )
        cls.author2 = User.objects.create(
            username="cbanks", first_name="Chase", last_name="Banks", email="Chase.Banks@nasa.org"
        )

        cls.a1 = Article(
            headline="Django lets you build Web apps easily",
            body="Django lets you build Web apps easily",
            created_at="2009-03-25T12:43:24.193",
            author=cls.author1,
            views=23198,
        )
        cls.a1.save()
        cls.a2 = Article(
            headline="NASA uses Python",
            body="NASA uses Python",
            created_at="2012-06-11T20:24:17.218",
            author=cls.author2,
            views=8312,
        )
        cls.a2.save()
        cls.a3 = Article(
            headline="Oxygen-free diet works wonders",
            body=None,
            created_at="2016-04-26T05:45:27.651",
            author=cls.author2,
            archived=True,
            views=1309,
        )
        cls.a3.save()
        cls.a4 = Article(
            headline="NASA finds intelligent life on Earth",
            body="",
            created_at="2117-02-24T10:44:10.234",
            author=cls.author2,
        )
        cls.a4.save()

        cls.a1.publications.add(cls.p1)
        cls.a2.publications.add(cls.p1, cls.p3)
        cls.a3.publications.add(cls.p2)

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        Article.objects.all().delete()
        Publication.objects.all().delete()


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


class DjangoNLFilterFunctionsTestCase(BaseTestCase):
    def test_a_date_function(self):
        filter_expr = "created_at > startOfWeek()"
        qs = self.nl_filter.filter(Article.objects.all(), filter_expr)
        self.assertEqual(qs.count(), 1)
        self.assertListEqual(list(qs.all()), [self.a4])
