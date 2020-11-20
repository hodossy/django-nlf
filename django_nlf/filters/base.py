import typing

from django.db import models
from django.db.models.constants import LOOKUP_SEP

from django_nlf.antlr import DjangoNLFLanguage
from django_nlf.functions import FunctionFactory
from django_nlf.types import CompositeExpression, CustomFunction, Expression, Operation


class NLFilterBase:
    language_class = DjangoNLFLanguage
    function_factory = FunctionFactory

    def get_conditions(self, expression):
        filter_tree = self.get_language().parse(expression)
        return self.build_conditions(filter_tree)

    def resolve_expression(self, expression: Expression):
        if isinstance(expression.field, CustomFunction):
            field_name = self.resolve_function(expression.field)
        else:
            field_name = self.normalize_field_name(expression.field)

        if isinstance(expression.value, CustomFunction):
            value = self.resolve_function(expression.value, field_name=field_name)
        else:
            value = self.normalize_value(field_name, expression.value)

        condition = self.get_condition(field_name, expression.lookup, value)

        return condition if not expression.exclude else ~condition

    def build_conditions(self, filter_tree: typing.Union[Expression, CompositeExpression]):
        if isinstance(filter_tree, Expression):
            return self.resolve_expression(filter_tree)

        if isinstance(filter_tree, CustomFunction):
            return self.resolve_function(filter_tree)

        left = self.build_conditions(filter_tree.left)
        right = self.build_conditions(filter_tree.right)

        if filter_tree.op == Operation.OR:
            return left | right
        return left & right

    def resolve_function(self, func: CustomFunction, field_name: str = None):
        context = self.get_function_context()
        fn = self.function_factory.get_function(func.name, **context)

        return fn(*func.args, **context, field_name=field_name)

    def get_language(self):
        return self.language_class()

    def get_function_context(self):
        raise NotImplementedError(".get_function_context() must be overriden")

    def filter(self, queryset, value):
        raise NotImplementedError(".filter() must be overriden")

    def normalize_value(self, field_name, value):
        raise NotImplementedError(".normalize_value() must be overriden")

    def normalize_field_name(self, field_name):
        raise NotImplementedError(".normalize_field_name() must be overriden")

    def get_condition(self, field, lookup, value):
        raise NotImplementedError(".get_condition() must be overriden")
