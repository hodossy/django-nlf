import typing
from dataclasses import dataclass
from enum import Enum, auto


class Lookup(Enum):
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


class CompositeExpression(typing.NamedTuple):
    op: Operation
    left: typing.Union[Expression, "CompositeExpression"]
    right: typing.Union[Expression, "CompositeExpression"]


class CustomFunction(typing.NamedTuple):
    name: str
    args: typing.Iterable[str]
