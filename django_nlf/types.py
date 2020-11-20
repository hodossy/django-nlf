import typing
from dataclasses import dataclass, field
from enum import Enum, auto


class Lookup(Enum):
    """Enumeration of supported lookups"""

    EQUALS = auto()
    CONTAINS = auto()
    REGEX = auto()
    IN = auto()
    GT = auto()
    GTE = auto()
    LT = auto()
    LTE = auto()


class Operation(Enum):
    AND = auto()
    OR = auto()


@dataclass(eq=True)
class Expression:
    lookup: Lookup
    field: str
    value: str
    exclude: bool


@dataclass()
class CompositeExpression:
    op: Operation
    left: typing.Union[Expression, "CompositeExpression"]
    right: typing.Union[Expression, "CompositeExpression"]


@dataclass()
class CustomFunction:
    name: str
    args: typing.Iterable[str]
    kwargs: typing.Mapping = field(default_factory=dict)


class FunctionRole(Enum):
    FIELD = auto()
    VALUE = auto()
    EXPRESSION = auto()


@dataclass()
class FunctionMeta:
    role: FunctionRole = FunctionRole.VALUE
    models: typing.Iterable["django.db.models.Model"] = tuple()
