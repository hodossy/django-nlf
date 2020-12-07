from django.contrib.auth import get_user_model
from django.test import TestCase

from django_nlf.filters.django import DjangoNLFilter
from .models import Article, Publication


User = get_user_model()


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
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

    def setUp(self):
        self.nl_filter = DjangoNLFilter()

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        Article.objects.all().delete()
        Publication.objects.all().delete()
