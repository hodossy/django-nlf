import dataclasses
from unittest import TestCase

from django.test import TestCase as DjangoTestCase

from django_nlf.schema import NLFModelSchemaBuilder
from django_nlf.types import FieldFilterSchema

from .models import Article, Publication


class NLFModelSchemaBuilderTestCase(TestCase):
    # pylint: disable=protected-access
    def setUp(self):
        self.builder = NLFModelSchemaBuilder()

    def test__get_fields(self):
        expected = [
            "id",
            "headline",
            "body",
            "author",
            "created_at",
            "views",
            "archived",
            "publications",
            "author.publication",
            "author.article",
            "author.id",
            "author.password",
            "author.last_login",
            "author.is_superuser",
            "author.username",
            "author.first_name",
            "author.last_name",
            "author.email",
            "author.is_staff",
            "author.is_active",
            "author.date_joined",
            "author.groups",
            "author.user_permissions",
            "author.publication.articles",
            "author.publication.id",
            "author.publication.title",
            "author.publication.category",
            "author.publication.subscription_fee",
            "author.publication.market_share",
            "author.publication.editor",
            "author.publication.articles.id",
            "author.publication.articles.headline",
            "author.publication.articles.body",
            "author.publication.articles.author",
            "author.publication.articles.created_at",
            "author.publication.articles.views",
            "author.publication.articles.archived",
            "author.publication.articles.publications",
            "author.publication.editor.publication",
            "author.publication.editor.article",
            "author.publication.editor.id",
            "author.publication.editor.password",
            "author.publication.editor.last_login",
            "author.publication.editor.is_superuser",
            "author.publication.editor.username",
            "author.publication.editor.first_name",
            "author.publication.editor.last_name",
            "author.publication.editor.email",
            "author.publication.editor.is_staff",
            "author.publication.editor.is_active",
            "author.publication.editor.date_joined",
            "author.publication.editor.groups",
            "author.publication.editor.user_permissions",
            "author.publication.editor.groups.user",
            "author.publication.editor.groups.id",
            "author.publication.editor.groups.name",
            "author.publication.editor.groups.permissions",
            "author.article.id",
            "author.article.headline",
            "author.article.body",
            "author.article.author",
            "author.article.created_at",
            "author.article.views",
            "author.article.archived",
            "author.article.publications",
            "author.groups.user",
            "author.groups.id",
            "author.groups.name",
            "author.groups.permissions",
            "publications.articles",
            "publications.id",
            "publications.title",
            "publications.category",
            "publications.subscription_fee",
            "publications.market_share",
            "publications.editor",
            "publications.articles.id",
            "publications.articles.headline",
            "publications.articles.body",
            "publications.articles.author",
            "publications.articles.created_at",
            "publications.articles.views",
            "publications.articles.archived",
            "publications.articles.publications",
            "publications.editor.publication",
            "publications.editor.article",
            "publications.editor.id",
            "publications.editor.password",
            "publications.editor.last_login",
            "publications.editor.is_superuser",
            "publications.editor.username",
            "publications.editor.first_name",
            "publications.editor.last_name",
            "publications.editor.email",
            "publications.editor.is_staff",
            "publications.editor.is_active",
            "publications.editor.date_joined",
            "publications.editor.groups",
            "publications.editor.user_permissions",
            "publications.editor.groups.user",
            "publications.editor.groups.id",
            "publications.editor.groups.name",
            "publications.editor.groups.permissions",
        ]
        fields = [path for path, _ in self.builder._get_fields(Article._meta)]
        self.assertEqual(fields, expected)

    def test__build_field_schema_for__auto_field(self):
        field_schema = self.builder._build_field_schema_for(Article._meta.get_field("id"), "id")
        expected = FieldFilterSchema(
            path="id",
            type="integer",
            help="",
            nullable=False,
            choices=None,
            search_url=None,
            search_param=None,
            target_field=None,
        )
        self.assertEqual(field_schema, expected)

    def test__build_field_schema_for__foreign_key(self):
        field_schema = self.builder._build_field_schema_for(
            Article._meta.get_field("author"), "author"
        )
        expected = FieldFilterSchema(
            path="author",
            type="integer",
            help="",
            nullable=False,
            choices=None,
            search_url=None,
            search_param=None,
            target_field=None,
        )
        self.assertEqual(field_schema, expected)

    def test__build_field_schema_for__foreign_key_with_to_field(self):
        field_schema = self.builder._build_field_schema_for(
            Publication._meta.get_field("editor"), "editor"
        )
        expected = FieldFilterSchema(
            path="editor",
            type="string",
            help="",
            nullable=True,
            choices=None,
            search_url=None,
            search_param=None,
            target_field=None,
        )
        self.assertEqual(field_schema, expected)

    def test__build_field_schema_for__many_to_many(self):
        field_schema = self.builder._build_field_schema_for(
            Article._meta.get_field("publications"), "publications"
        )
        expected = FieldFilterSchema(
            path="publications",
            type="integer",
            help="",
            nullable=False,
            choices=None,
            search_url="/publications/",
            search_param="search",
            target_field="id",
        )
        self.assertEqual(field_schema, expected)

    def test__build_field_schema_for__many_to_many_reverse(self):
        field_schema = self.builder._build_field_schema_for(
            Publication._meta.get_field("articles"), "articles"
        )
        expected = FieldFilterSchema(
            path="articles",
            type="integer",
            help="",
            nullable=True,
            choices=None,
            search_url="/articles/",
            search_param="search",
            target_field="id",
        )
        self.assertEqual(field_schema, expected)

    def test_get_schema_for_publication(self):
        # requesting twice to test cache usage
        initial_schema = self.builder.get_schema_for(Publication)
        schema = self.builder.get_schema_for(Publication)
        self.assertTrue(initial_schema is schema)

    def test_get_schema_for_publication(self):
        # requesting twice to test cache usage
        schema = self.builder.get_schema_for(Publication)
        schema = dataclasses.asdict(schema)
        self.assertTrue("fields" in schema)
        self.assertTrue("functions" in schema)
        self.assertTrue("empty_val" in schema)


class SchemaViewTestCase(DjangoTestCase):
    def test_schema_view_for_article(self):
        response = self.client.get("/schemas/tests/article")
        self.assertEqual(response.status_code, 200)

    def test_schema_view_for_unknown(self):
        response = self.client.get("/schemas/tests/author")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 404)
