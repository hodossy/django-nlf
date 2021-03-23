"""
Django NLF types
"""
import typing
from dataclasses import dataclass, field
from enum import Enum, auto


class Lookup(Enum):
    """Enumeration of supported lookups."""

    EQUALS = auto()
    CONTAINS = auto()
    REGEX = auto()
    IN = auto()
    GT = auto()
    GTE = auto()
    LT = auto()
    LTE = auto()


class Operation(Enum):
    """Enumeration of operations."""

    AND = auto()
    OR = auto()


@dataclass(eq=True)
class Expression:
    """The most basic building block of the language."""

    lookup: Lookup
    field: str
    value: str
    exclude: bool


@dataclass()
class CustomFunction:
    """The interface for registering and calling custom functions."""

    name: str
    args: typing.Iterable[str] = field(default_factory=list)
    kwargs: typing.Mapping = field(default_factory=dict)


@dataclass()
class CompositeExpression:
    """Combines expressions (as operands) with an operator.
    Operands can be other composite expressions as well.
    """

    operation: Operation
    left: typing.Union[Expression, "CompositeExpression", CustomFunction]
    right: typing.Union[Expression, "CompositeExpression", CustomFunction]


ParsedExpression = typing.Union[Expression, CompositeExpression, CustomFunction]


class FunctionRole(Enum):
    """Enumeration of custom function roles"""

    FIELD = auto()
    VALUE = auto()
    EXPRESSION = auto()


@dataclass()
class FunctionMeta:
    """The metadata for custom functions that help verify their usage in the language."""

    params: typing.Mapping = field(default_factory=dict)
    rtype: str = ""
    role: FunctionRole = FunctionRole.VALUE
    models: typing.Iterable["django.db.models.Model"] = tuple()
    help: str = ""

    def to_repr(self):
        return {
            "params": self.params,
            "rtype": self.rtype,
            "role": self.role.name.lower(),
            "help": self.help,
        }


@dataclass()
class FieldFilterSchema:
    """The schema definiton of a model field. Used for autocomplete"""

    # pylint: disable=too-many-instance-attributes

    type: str
    help: str
    nullable: bool
    choices: typing.Iterable[str] = None
    related: str = None
    search_url: str = None
    search_param: str = None
    target_field: str = None


@dataclass()
class ModelFilterSchema:
    """The schema definition for a model. Used for autocomplete."""

    fields: typing.Iterable[FieldFilterSchema]
    functions: typing.Iterable[FunctionMeta]
    shortcuts: typing.Iterable[str]
    empty_val: str
