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
