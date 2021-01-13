from django.db import models
from django.urls import reverse, NoReverseMatch

from django_nlf.conf import nlf_settings
from django_nlf.functions import FunctionRegistry
from django_nlf.types import FieldFilterSchema, ModelFilterSchema


class NLFModelSchemaBuilder:
    __cache = {}
    field_shortcuts = nlf_settings.FIELD_SHORTCUTS
    path_sep = nlf_settings.PATH_SEPARATOR
    empty_val = nlf_settings.EMPTY_VALUE
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

    def _build_schema_for(self, model: "django.db.models.Model") -> ModelFilterSchema:
        fields = self._get_fields(model._meta)  # pylint: disable=protected-access
        functions = FunctionRegistry.get_functions_for(model)
        return ModelFilterSchema(
            fields=[self._build_field_schema_for(field, path) for path, field in fields],
            functions={key.name: value for key, value in functions.items()},
            empty_val=self.empty_val,
        )

    def _get_fields(
        self, opts: "django.db.models.options.Options", explored_rels=None, path: str = ""
    ):
        fields = [
            (f"{path}{self.path_sep}{field.name}" if path else field.name, field)
            for field in opts.get_fields()
        ]

        related_fields = []
        explored_rels = explored_rels or tuple()
        for new_path, field in fields:
            if not field.is_relation:
                continue

            related_opts = field.related_model._meta  # pylint: disable=protected-access
            if (
                field.target_field not in explored_rels
                and related_opts.label not in self.ignored_model_labels
            ):
                explored_rels = explored_rels + (field.target_field,)
                # if we would explore field directions, we would immediately run into an infinite
                # circle when we encounter a relationship with a reverse reletaionship, which is the
                # default behaviour. Therefore we skip those paths that we already examined
                related_fields.extend(self._get_fields(related_opts, explored_rels, new_path))

        return fields + related_fields

    def _build_field_schema_for(self, field, path: str) -> FieldFilterSchema:
        schema = FieldFilterSchema(
            path=path,
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
            return self._get_field_schema_type(field.target_field)

        if isinstance(field, models.BooleanField):
            return "boolean"
        if isinstance(field, models.IntegerField):
            return "integer"
        if isinstance(field, (models.DecimalField, models.FloatField)):
            return "number"

        return "string"
