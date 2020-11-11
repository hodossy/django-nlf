import typing
from dataclasses import dataclass
from enum import Enum


class Lookup(Enum):
    EQUALS = 0
    LIKE = 1
    IN = 2
    GT = 3
    GTE = 4
    LT = 5
    LTE = 6


class Operation(Enum):
    AND = 0
    OR = 1


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
