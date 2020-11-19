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

    def __init__(self):
        super().__init__()
        self.distinct = False
        self.model = None
        self.opts = None

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

    def normalize_field_name(self, field_name: str) -> str:
        return field_name.replace(self.path_sep, LOOKUP_SEP)

    def normalize_value(self, field_name, value):
        if value == self.empty_val:
            return value

        parts = field_name.split(LOOKUP_SEP)
        field = self.follow_field_path(self.opts, parts)

        if field.choices:
            for val, display in field.choices:
                if value.lower() == display.lower():
                    return val
            raise ValueError("Invalid choice")

        if isinstance(field, (models.DateField, models.DateTimeField)):
            return self.coerce_datetime(value)

        if isinstance(field, (models.BooleanField, models.NullBooleanField)):
            return self.coerce_bool(value)

        if value.startswith('"') and value.endswith('"'):
            # remove quotes
            return value[1:-1]
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
            "model": self.model
        }

    def filter(self, queryset: models.QuerySet, value):
        self.model = queryset.model
        self.opts = queryset.model._meta  # pylint: disable=protected-access

        conditions = self.get_conditions(value)
        queryset = queryset.filter(conditions)

        if self.distinct:
            queryset = queryset.distinct()

        return  queryset

    def coerce_bool(self, value):
        return coerce_bool(value)

    def coerce_datetime(self, value):
        return coerce_datetime(value)
