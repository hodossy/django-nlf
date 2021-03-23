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

    def test__model_schema(self):
        expected = {
            "tests.article": {
                "fields": [
                    "id",
                    "headline",
                    "body",
                    "author",
                    "created_at",
                    "views",
                    "archived",
                    "publications",
                ],
                "functions": ["hasBeenPublished"],
            },
            "auth.user": {
                "fields": [
                    "publication",
                    "article",
                    "id",
                    "password",
                    "last_login",
                    "is_superuser",
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "is_staff",
                    "is_active",
                    "date_joined",
                    "groups",
                    "user_permissions",
                ],
                "functions": [],
            },
            "tests.publication": {
                "fields": [
                    "articles",
                    "id",
                    "title",
                    "category",
                    "subscription_fee",
                    "market_share",
                    "editor",
                ],
                "functions": ["totalViews"],
            },
            "auth.group": {
                "fields": ["user", "id", "name", "permissions"],
                "functions": [],
            },
        }
        schemas = self.builder._get_model_schema(Article)
        for _, schema in schemas.items():
            schema["fields"] = list(schema["fields"].keys())
            schema["functions"] = list(schema["functions"].keys())
        self.assertDictEqual(schemas, expected)

    def test__build_field_schema_for__auto_field(self):
        field_schema = self.builder._build_field_schema_for(Article._meta.get_field("id"))
        expected = FieldFilterSchema(
            type="integer",
            help="",
            nullable=False,
        )
        self.assertEqual(field_schema, expected)

    def test__build_field_schema_for__foreign_key(self):
        field_schema = self.builder._build_field_schema_for(Article._meta.get_field("author"))
        expected = FieldFilterSchema(
            type="relation",
            help="",
            nullable=False,
            related="auth.user",
        )
        self.assertEqual(field_schema, expected)

    def test__build_field_schema_for__foreign_key_with_to_field(self):
        field_schema = self.builder._build_field_schema_for(Publication._meta.get_field("editor"))
        expected = FieldFilterSchema(
            type="relation",
            help="",
            nullable=True,
            related="auth.user",
        )
        self.assertEqual(field_schema, expected)

    def test__build_field_schema_for__many_to_many(self):
        field_schema = self.builder._build_field_schema_for(Article._meta.get_field("publications"))
        expected = FieldFilterSchema(
            type="relation",
            help="",
            nullable=False,
            related="tests.publication",
            search_url="/publications/",
            search_param="search",
            target_field="id",
        )
        self.assertEqual(field_schema, expected)

    def test__build_field_schema_for__many_to_many_reverse(self):
        field_schema = self.builder._build_field_schema_for(Publication._meta.get_field("articles"))
        expected = FieldFilterSchema(
            type="relation",
            help="",
            nullable=True,
            related="tests.article",
            search_url="/articles/",
            search_param="search",
            target_field="id",
        )
        self.assertEqual(field_schema, expected)

    def test_get_schema_cahce_for_publication(self):
        # requesting twice to test cache usage
        initial_schema = self.builder.get_schema_for(Publication)
        schema = self.builder.get_schema_for(Publication)
        self.assertTrue(initial_schema is schema)

    def test_get_schema_for_publication(self):
        schema = self.builder.get_schema_for(Publication)
        self.assertTrue("tests.publication" in schema)
        self.assertTrue("common_functions" in schema)
        self.assertTrue("empty_val" in schema)


class SchemaViewTestCase(DjangoTestCase):
    def test_schema_view_for_article(self):
        response = self.client.get("/schemas/tests/article")
        self.assertEqual(response.status_code, 200)

    def test_schema_view_for_unknown(self):
        response = self.client.get("/schemas/tests/author")
        self.assertEqual(response.status_code, 404)
