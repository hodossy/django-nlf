# Generated from DjangoNLF.g4 by ANTLR 4.8
from antlr4 import ParseTreeListener

from .generated import DjangoNLFParser
from ..utils import Lookup, Operation


class Operator:
    def __init__(self, value, depth=0):
        self.value = depth * 2 + value

    def is_and(self):
        return self.value % 2 == 0

    def has_precedence(self, other):
        return self.is_and() and self.value == other.value - 1

    def to_operation(self):
        return Operation(self.value % 2)

    def __repr__(self):
        operation = "AND" if self.is_and() else "OR"
        return f"<Operator.{operation}: {self.value}>"


def handle_precedence(operator, left, right):
    if isinstance(left, list) and operator.has_precedence(left[0]):
        previous_expression = left.pop()
        left.append([operator, previous_expression, right])
        return left

    return [operator, left, right]


def handle_operator(el):
    return el.to_operation() if isinstance(el, Operator) else el


def normalize_operators(output):
    return [
        normalize_operators(el) if isinstance(el, list) else handle_operator(el) for el in output
    ]


# This class defines a complete listener for a parse tree produced by DjangoNLFParser.
class DjangoNLFListener(ParseTreeListener):
    def __init__(self):
        super().__init__()
        self.output = []

        self.lookup = None
        self.operator = None
        self.exclude = False

        self.stage = []
        self.depth = 0

    # # Enter a parse tree produced by DjangoNLFParser#operator.
    # def enterOperator(self, ctx: DjangoNLFParser.OperatorContext):
    #     pass

    # Exit a parse tree produced by DjangoNLFParser#operator.
    def exitOperator(self, ctx: DjangoNLFParser.OperatorContext):
        if ctx.AND() is not None:
            self.operator = Operator(0, self.depth)
        elif ctx.OR() is not None:
            self.operator = Operator(1, self.depth)

    # # Enter a parse tree produced by DjangoNLFParser#lookup.
    # def enterLookup(self, ctx: DjangoNLFParser.LookupContext):
    #     pass

    # Exit a parse tree produced by DjangoNLFParser#lookup.
    def exitLookup(self, ctx: DjangoNLFParser.LookupContext):
        if ctx.EQUALS() is not None:
            self.lookup = Lookup.EQUALS
        elif ctx.NEQUALS() is not None:
            self.lookup = Lookup.EQUALS
            self.exclude = True
        elif ctx.LIKE() is not None:
            self.lookup = Lookup.LIKE
        elif ctx.NLIKE() is not None:
            self.lookup = Lookup.LIKE
            self.exclude = True
        elif ctx.IN() is not None:
            self.lookup = Lookup.IN
        elif ctx.NIN() is not None:
            self.lookup = Lookup.IN
            self.exclude = True
        elif ctx.GT() is not None:
            self.lookup = Lookup.GT
        elif ctx.GTE() is not None:
            self.lookup = Lookup.GTE
        elif ctx.LT() is not None:
            self.lookup = Lookup.LT
        elif ctx.LTE() is not None:
            self.lookup = Lookup.LTE

    # # Enter a parse tree produced by DjangoNLFParser#expression.
    # def enterExpression(self, ctx: DjangoNLFParser.ExpressionContext):
    #     pass

    # Exit a parse tree produced by DjangoNLFParser#expression.
    def exitExpression(self, ctx: DjangoNLFParser.ExpressionContext):
        current_expression = {
            "field_name": ctx.field.text,
            "lookup": self.lookup,
            "value": ctx.value.text,
            "exclude": self.exclude,
        }
        self.lookup = None
        self.exclude = False

        if self.operator is None:
            self.output.append(current_expression)
        else:
            previous_expression = self.output.pop()
            step = handle_precedence(self.operator, previous_expression, current_expression)
            self.output.append(step)
            self.operator = None

    # # Enter a parse tree produced by DjangoNLFParser#composite_expr.
    # def enterComposite_expr(self, ctx: DjangoNLFParser.Composite_exprContext):
    #     pass

    # # Exit a parse tree produced by DjangoNLFParser#composite_expr.
    # def exitComposite_expr(self, ctx: DjangoNLFParser.Composite_exprContext):
    #     pass

    # Enter a parse tree produced by DjangoNLFParser#nested_comp_expr.
    def enterNested_comp_expr(self, ctx: DjangoNLFParser.Nested_comp_exprContext):
        self.stage.append((self.operator, self.output))
        self.depth += 1
        # let the listener parse the nested expression as if it were a new one
        self.output = []
        self.operator = None

    # Exit a parse tree produced by DjangoNLFParser#nested_comp_expr.
    def exitNested_comp_expr(self, ctx: DjangoNLFParser.Nested_comp_exprContext):
        operator, left = self.stage.pop()
        right = self.output

        if operator:
            step = handle_precedence(operator, left[0], right[0])

            self.output = [step]

        self.depth -= 1

    # # Enter a parse tree produced by DjangoNLFParser#filter_exp.
    # def enterFilter_expr(self, ctx: DjangoNLFParser.Filter_exprContext):
    #     pass

    # Exit a parse tree produced by DjangoNLFParser#filter_exp.
    def exitFilter_expr(self, ctx: DjangoNLFParser.Filter_exprContext):
        self.output = normalize_operators(self.output)

    # # Enter a parse tree produced by DjangoNLFParser#parse.
    # def enterParse(self, ctx: DjangoNLFParser.ParseContext):
    #     pass
    #
    # # Exit a parse tree produced by DjangoNLFParser#parse.
    # def exitParse(self, ctx: DjangoNLFParser.ParseContext):
    #     pass


del DjangoNLFParser
