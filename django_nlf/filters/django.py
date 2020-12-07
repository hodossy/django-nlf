from django.db import models
from django.db.models.constants import LOOKUP_SEP

from django_nlf.conf import nlf_settings
from django_nlf.types import Lookup
from django_nlf.utils import coerce_bool, coerce_datetime

from .base import NLFilterBase


class DjangoNLFilter(NLFilterBase):
    lookups = {
        Lookup.EQUALS: "iexact",
        Lookup.CONTAINS: "icontains",
        Lookup.REGEX: "iregex",
        Lookup.IN: "in",
        Lookup.GT: "gt",
        Lookup.GTE: "gte",
        Lookup.LT: "lt",
        Lookup.LTE: "lte",
    }
    path_sep = nlf_settings.PATH_SEPARATOR
    empty_val = nlf_settings.EMPTY_VALUE
    # field_shortcuts = {}

    def __init__(self, request=None, view=None):
        super().__init__()
        self.request = request
        self.view = view

        self.distinct = False
        self.model = None
        self.opts = None

        self.annotations = {}

    def follow_field_path(self, opts, path):
        field = opts.get_field(path[0])

        if hasattr(field, "get_path_info"):
            # This field is a relation, update opts to follow the relation
            path_info = field.get_path_info()

            if any(path.m2m for path in path_info):
                self.distinct = True

            opts = path_info[-1].to_opts
            return self.follow_field_path(opts, path[1:])

        return field

    def normalize_field_function(self, value):
        annotation, *other = value.items()
        if other:
            raise ValueError("Multiple annotations returned!")
        self.annotations.update(**value)
        field_name, _ = annotation
        return field_name

    def normalize_value_function(self, value):
        return value

    def normalize_expression_function(self, value):
        annotations, condition = value
        self.annotations.update(**annotations)

        return condition

    def normalize_field_name(self, field_name: str) -> str:
        # field_name = self.field_shortcuts.get(field_name, field_name)
        return field_name.replace(self.path_sep, LOOKUP_SEP)

    def normalize_value(self, field_name, value):
        if (
            field_name in self.annotations
            or value == self.empty_val
            or isinstance(value, (models.F, models.Aggregate, models.Subquery, models.Window))
        ):
            return value

        parts = field_name.split(LOOKUP_SEP)
        field = self.follow_field_path(self.opts, parts)

        if field.choices:
            for val, display in field.choices:
                if value.lower() == display.lower():
                    return val

            choices = ", ".join([display for _, display in field.choices])
            raise ValueError(f"Invalid {field_name}! Must be one of {choices}")

        if isinstance(field, (models.DateField, models.DateTimeField)):
            return self.coerce_datetime(value)

        if isinstance(field, (models.BooleanField, models.NullBooleanField)):
            return self.coerce_bool(value)

        return value

    def get_condition(self, field, lookup, value):
        if isinstance(value, bool):
            lookup_str = None
        elif value == self.empty_val:
            lookup_str = "isnull"
            value = True
        else:
            lookup_str = self.lookups.get(lookup)

        orm_lookup = LOOKUP_SEP.join([field, lookup_str]) if lookup_str else field

        return models.Q(**{orm_lookup: value})

    def get_function_context(self):
        return {
            "model": self.model,
            "request": self.request,
            "view": self.view,
        }

    def filter(self, queryset: models.QuerySet, value):
        self.model = queryset.model
        self.opts = queryset.model._meta  # pylint: disable=protected-access

        conditions = self.get_conditions(value)
        if self.annotations:
            queryset = queryset.annotate(**self.annotations)
        queryset = queryset.filter(conditions)

        if self.distinct:
            queryset = queryset.distinct()

        return queryset

    def coerce_bool(self, value):
        return coerce_bool(value)

    def coerce_datetime(self, value):
        return coerce_datetime(value)
