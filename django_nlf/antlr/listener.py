# Generated from DjangoNLF.g4 by ANTLR 4.8
from antlr4 import ParseTreeListener

from .generated import DjangoNLFParser
from .lookups import Lookup, Operation


# This class defines a complete listener for a parse tree produced by DjangoNLFParser.
class DjangoNLFListener(ParseTreeListener):
    def __init__(self):
        super().__init__()
        self.output = []
        self.lookup = None
        self.operator = None
        self.exclude = False

    # # Enter a parse tree produced by DjangoNLFParser#operator.
    # def enterOperator(self, ctx: DjangoNLFParser.OperatorContext):
    #     print("enterOperator")
    #     pass

    # Exit a parse tree produced by DjangoNLFParser#operator.
    def exitOperator(self, ctx: DjangoNLFParser.OperatorContext):
        print("exitOperator")
        if ctx.AND() is not None:
            self.operator = Operation.AND
        elif ctx.OR() is not None:
            self.operator = Operation.OR

    # # Enter a parse tree produced by DjangoNLFParser#lookup.
    # def enterLookup(self, ctx: DjangoNLFParser.LookupContext):
    #     print("enterLookup")
    #     pass

    # Exit a parse tree produced by DjangoNLFParser#lookup.
    def exitLookup(self, ctx: DjangoNLFParser.LookupContext):
        print("exitLookup")
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
    #     print("enterExpression")
    #     pass

    # Exit a parse tree produced by DjangoNLFParser#expression.
    def exitExpression(self, ctx: DjangoNLFParser.ExpressionContext):
        print("exitExpression")
        current_expression = {
            "field_name": ctx.TEXT(0).getText(),
            "lookup": self.lookup,
            "value": (ctx.QUOTED_TEXT() or ctx.TEXT(1)).getText(),
            "exclude": self.exclude,
        }
        self.lookup = None
        self.exclude = False

        if self.operator is None:
            self.output.append(current_expression)
        else:
            previous_expression = self.output.pop()
            if (
                isinstance(previous_expression, list)
                and self.operator == Operation.AND
                and previous_expression[0] == Operation.OR
            ):
                pre_previous_expression = previous_expression.pop()
                previous_expression.append(
                    [self.operator, pre_previous_expression, current_expression]
                )
                self.output.append(previous_expression)
            else:
                self.output.append([self.operator, previous_expression, current_expression])
            self.operator = None

    # # Enter a parse tree produced by DjangoNLFParser#filter_exp.
    # def enterFilter_exp(self, ctx: DjangoNLFParser.Filter_expContext):
    #     print("enterFilter_exp")
    #     pass
    #
    # # Exit a parse tree produced by DjangoNLFParser#filter_exp.
    # def exitFilter_exp(self, ctx: DjangoNLFParser.Filter_expContext):
    #     print("exitFilter_exp")
    #
    #     pass


del DjangoNLFParser
