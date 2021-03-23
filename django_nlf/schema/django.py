from typing import Mapping

from django.db import models
from django.urls import reverse, NoReverseMatch

from django_nlf.conf import nlf_settings
from django_nlf.functions import FunctionRegistry
from django_nlf.types import FieldFilterSchema, ModelFilterSchema


class NLFModelSchemaBuilder:
    __cache = {}
    field_shortcuts = nlf_settings.FIELD_SHORTCUTS
    empty_val = nlf_settings.EMPTY_VALUE
    path_separator = nlf_settings.PATH_SEPARATOR
    autocomplete_views = nlf_settings.SEARCH_URL_MAP
    autocomplete_param = nlf_settings.SEARCH_PARAM
    ignored_model_labels = (
        "auth.Permission",
        "contenttypes.ContentType",
    )

    def get_schema_for(self, model: "django.db.models.Model"):
        """Returns a schema for the given model.

        :param "django.db.models.Model" model: .
        :return: .
        :rtype: ModelFilterSchema
        """
        label = model._meta.label  # pylint: disable=protected-access
        if label not in self.__cache:
            NLFModelSchemaBuilder.__cache[label] = self._build_schema_for(model)

        return self.__cache[label]

    def _build_schema_for(self, model: "django.db.models.Model") -> Mapping[str, ModelFilterSchema]:
        schema = self._get_model_schema(model)
        schema["common_functions"] = FunctionRegistry.get_functions_for(None)
        schema["empty_val"] = self.empty_val
        schema["path_separator"] = self.path_separator

        return schema

    def _get_model_schema(self, model: "django.db.models.Model", explored_models=tuple()):
        opts = model._meta  # pylint: disable=protected-access
        app = opts.label.lower()
        schema = {
            app: {
                "fields": {},
                "functions": FunctionRegistry.get_functions_for(model),
            },
        }

        for field in opts.get_fields():
            schema[app]["fields"][field.name] = self._build_field_schema_for(field)
            if not field.is_relation:
                continue

            related_opts = field.related_model._meta  # pylint: disable=protected-access
            if (
                related_opts.label not in explored_models
                and related_opts.label not in self.ignored_model_labels
            ):
                explored_models = explored_models + (related_opts.label,)
                related_schema = self._get_model_schema(field.related_model, explored_models)
                schema.update(related_schema)

        return schema

    def _build_field_schema_for(self, field) -> FieldFilterSchema:
        schema = FieldFilterSchema(
            type=self._get_field_schema_type(field),
            help=str(getattr(field, "help_text", "")),  # convert to str to evaluate lazy text
            nullable=field.null,
        )

        if field.is_relation:
            related_model_label = (
                field.related_model._meta.label  # pylint: disable=protected-access
            )
            url_name = self.autocomplete_views.get(
                related_model_label, f"{field.related_model.__name__.lower()}-list"
            )
            schema.related = related_model_label.lower()
            try:
                schema.search_url = reverse(url_name)
                schema.search_param = self.autocomplete_param
                schema.target_field = field.target_field.name
            except NoReverseMatch:
                pass

        elif field.flatchoices:  # flatchoices does not exist on relations
            schema.choices = [display for _, display in field.flatchoices]

        return schema

    def _get_field_schema_type(self, field) -> str:
        if field.is_relation:
            return "relation"
        if isinstance(field, models.BooleanField):
            return "boolean"
        # AutoField on Django 2.2 is not an IntegerField
        # TODO: remove AutoField check when dropping support for Django 2
        if isinstance(field, (models.IntegerField, models.AutoField)):
            return "integer"
        if isinstance(field, (models.DecimalField, models.FloatField)):
            return "number"

        return "string"
