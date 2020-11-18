import typing

from django.db import models
from django.db.models.constants import LOOKUP_SEP

from .antlr import DjangoNLFLanguage
from .conf import nlf_settings
from .types import Expression, CompositeExpression, Operation, Lookup
from .utils import coerce_bool, coerce_datetime


class NLFilterBase:
    language_class = DjangoNLFLanguage

    def get_conditions(self, expression):
        filter_tree = self.get_language().parse(expression)
        return self.build_conditions(filter_tree)

    def build_condition(self, expression: Expression):
        field_name = self.normalize_field_name(expression.field)
        value = self.normalize_value(field_name, expression.value)
        condition = self.get_condition(field_name, expression.lookup, value)
        return condition if not expression.exclude else ~condition

    def build_conditions(self, filter_tree: typing.Union[Expression, CompositeExpression]):
        if isinstance(filter_tree, Expression):
            return self.build_condition(filter_tree)

        left = self.build_conditions(filter_tree.left)
        right = self.build_conditions(filter_tree.right)

        if filter_tree.op == Operation.OR:
            return left | right
        return left & right

    def get_language(self):
        return self.language_class()

    def filter(self, queryset, value):
        raise NotImplementedError(".filter() must be overriden")

    def normalize_value(self, field_name, value):
        raise NotImplementedError(".normalize_value() must be overriden")

    def normalize_field_name(self, field_name):
        raise NotImplementedError(".normalize_field_name() must be overriden")

    def get_condition(self, field, lookup, value):
        raise NotImplementedError(".get_condition() must be overriden")


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
        self.opts = None

    def follow_field_path(self, opts, path):
        field = opts.get_field(path[0])

        if hasattr(field, "get_path_info"):
            # This field is a relation, update opts to follow the relation
            path_info = field.get_path_info()
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

    def filter(self, queryset, value):
        self.opts = queryset.model._meta  # pylint: disable=protected-access
        conditions = self.get_conditions(value)
        return queryset.filter(conditions)

    def coerce_bool(self, value):
        return coerce_bool(value)

    def coerce_datetime(self, value):
        return coerce_datetime(value)
