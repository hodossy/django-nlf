# pylint: disable=invalid-name,missing-module-docstring,missing-class-docstring,missing-function-docstring,too-many-ancestors,duplicate-code
# Generated from DjangoNLF.g4 by ANTLR 4.8
# encoding: utf-8
import sys
from io import StringIO
from typing import TextIO

from antlr4 import (
    ATN,
    ATNDeserializer,
    DFA,
    NoViableAltException,
    Parser,
    ParserATNSimulator,
    ParserRuleContext,
    ParseTreeListener,
    PredictionContextCache,
    RecognitionException,
    Token,
    TokenStream,
)


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\5\2\24\n\2\3\2\3\2\5\2\30\n\2\3\3\5\3")
        buf.write("\33\n\3\3\3\3\3\6\3\37\n\3\r\3\16\3 \3\3\3\3\3\4\5\4&")
        buf.write("\n\4\3\4\3\4\5\4*\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\62\n")
        buf.write("\5\3\6\3\6\3\6\3\6\7\68\n\6\f\6\16\6;\13\6\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\5\bC\n\b\3\b\3\b\3\b\5\bH\n\b\7\bJ\n\b\f")
        buf.write("\b\16\bM\13\b\3\t\5\tP\n\t\3\t\3\t\3\t\2\2\n\2\4\6\b\n")
        buf.write("\f\16\20\2\6\3\2\17\21\3\2\3\4\3\2\3\16\3\2\26\31\2X\2")
        buf.write("\23\3\2\2\2\4\32\3\2\2\2\6%\3\2\2\2\b\61\3\2\2\2\n\63")
        buf.write("\3\2\2\2\f<\3\2\2\2\16B\3\2\2\2\20O\3\2\2\2\22\24\7\24")
        buf.write("\2\2\23\22\3\2\2\2\23\24\3\2\2\2\24\25\3\2\2\2\25\27\t")
        buf.write("\2\2\2\26\30\7\24\2\2\27\26\3\2\2\2\27\30\3\2\2\2\30\3")
        buf.write("\3\2\2\2\31\33\7\24\2\2\32\31\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\36\t\3\2\2\35\37\7\24\2\2\36\35\3\2\2\2")
        buf.write('\37 \3\2\2\2 \36\3\2\2\2 !\3\2\2\2!"\3\2\2\2"#\7\26')
        buf.write("\2\2#\5\3\2\2\2$&\7\24\2\2%$\3\2\2\2%&\3\2\2\2&'\3\2")
        buf.write("\2\2')\t\4\2\2(*\7\24\2\2)(\3\2\2\2)*\3\2\2\2*\7\3\2")
        buf.write("\2\2+\62\7\31\2\2,\62\5\4\3\2-.\7\26\2\2./\5\6\4\2/\60")
        buf.write("\t\5\2\2\60\62\3\2\2\2\61+\3\2\2\2\61,\3\2\2\2\61-\3\2")
        buf.write("\2\2\62\t\3\2\2\2\639\5\b\5\2\64\65\5\2\2\2\65\66\5\b")
        buf.write("\5\2\668\3\2\2\2\67\64\3\2\2\28;\3\2\2\29\67\3\2\2\29")
        buf.write(":\3\2\2\2:\13\3\2\2\2;9\3\2\2\2<=\7\22\2\2=>\5\n\6\2>")
        buf.write("?\7\23\2\2?\r\3\2\2\2@C\5\n\6\2AC\5\f\7\2B@\3\2\2\2BA")
        buf.write("\3\2\2\2CK\3\2\2\2DG\5\2\2\2EH\5\n\6\2FH\5\f\7\2GE\3\2")
        buf.write("\2\2GF\3\2\2\2HJ\3\2\2\2ID\3\2\2\2JM\3\2\2\2KI\3\2\2\2")
        buf.write("KL\3\2\2\2L\17\3\2\2\2MK\3\2\2\2NP\5\16\b\2ON\3\2\2\2")
        buf.write("OP\3\2\2\2PQ\3\2\2\2QR\7\2\2\3R\21\3\2\2\2\16\23\27\32")
        buf.write(" %)\619BGKO")
        return buf.getvalue()


class DjangoNLFParser(Parser):

    grammarFileName = "DjangoNLF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'>'",
        "'>='",
        "'<'",
        "'<='",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'('",
        "')'",
    ]

    symbolicNames = [
        "<INVALID>",
        "EQUALS",
        "NEQUALS",
        "CONTAINS",
        "NCONTAINS",
        "REGEX",
        "NREGEX",
        "IN",
        "NIN",
        "GT",
        "GTE",
        "LT",
        "LTE",
        "AND",
        "OR",
        "NOT",
        "OPEN_PAREN",
        "CLOSE_PAREN",
        "WHITESPACE",
        "NEWLINE",
        "TEXT",
        "QUOTED_TEXT",
        "LISTING",
        "FUNCTION",
    ]

    RULE_operator = 0
    RULE_boolean_expr = 1
    RULE_lookup = 2
    RULE_expression = 3
    RULE_composite_expr = 4
    RULE_nested_comp_expr = 5
    RULE_filter_expr = 6
    RULE_parse = 7

    ruleNames = [
        "operator",
        "boolean_expr",
        "lookup",
        "expression",
        "composite_expr",
        "nested_comp_expr",
        "filter_expr",
        "parse",
    ]

    EOF = Token.EOF
    EQUALS = 1
    NEQUALS = 2
    CONTAINS = 3
    NCONTAINS = 4
    REGEX = 5
    NREGEX = 6
    IN = 7
    NIN = 8
    GT = 9
    GTE = 10
    LT = 11
    LTE = 12
    AND = 13
    OR = 14
    NOT = 15
    OPEN_PAREN = 16
    CLOSE_PAREN = 17
    WHITESPACE = 18
    NEWLINE = 19
    TEXT = 20
    QUOTED_TEXT = 21
    LISTING = 22
    FUNCTION = 23

    def __init__(self, input_: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input_, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._la = None
        self._predicates = None

    class OperatorContext(ParserRuleContext):
        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(DjangoNLFParser.AND, 0)

        def OR(self):
            return self.getToken(DjangoNLFParser.OR, 0)

        def NOT(self):
            return self.getToken(DjangoNLFParser.NOT, 0)

        def WHITESPACE(self, i: int = None):
            if i is None:
                return self.getTokens(DjangoNLFParser.WHITESPACE)

            return self.getToken(DjangoNLFParser.WHITESPACE, i)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_operator

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enter_operator"):
                listener.enter_operator(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exit_operator"):
                listener.exit_operator(self)

    def operator(self):

        localctx = DjangoNLFParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_operator)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DjangoNLFParser.WHITESPACE:
                self.state = 16
                self.match(DjangoNLFParser.WHITESPACE)

            self.state = 19
            _la = self._input.LA(1)
            if not (
                (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << DjangoNLFParser.AND)
                            | (1 << DjangoNLFParser.OR)
                            | (1 << DjangoNLFParser.NOT)
                        )
                    )
                    != 0
                )
            ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
            if la_ == 1:
                self.state = 20
                self.match(DjangoNLFParser.WHITESPACE)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_exprContext(ParserRuleContext):
        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.field = None  # Token

        def EQUALS(self):
            return self.getToken(DjangoNLFParser.EQUALS, 0)

        def NEQUALS(self):
            return self.getToken(DjangoNLFParser.NEQUALS, 0)

        def TEXT(self):
            return self.getToken(DjangoNLFParser.TEXT, 0)

        def WHITESPACE(self, i: int = None):
            if i is None:
                return self.getTokens(DjangoNLFParser.WHITESPACE)

            return self.getToken(DjangoNLFParser.WHITESPACE, i)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_boolean_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enter_boolean_expr"):
                listener.enter_boolean_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exit_boolean_expr"):
                listener.exit_boolean_expr(self)

    def boolean_expr(self):

        localctx = DjangoNLFParser.Boolean_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_boolean_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DjangoNLFParser.WHITESPACE:
                self.state = 23
                self.match(DjangoNLFParser.WHITESPACE)

            self.state = 26
            _la = self._input.LA(1)
            if _la not in (DjangoNLFParser.EQUALS, DjangoNLFParser.NEQUALS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.match(DjangoNLFParser.WHITESPACE)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la != DjangoNLFParser.WHITESPACE:
                    break

            self.state = 32
            localctx.field = self.match(DjangoNLFParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LookupContext(ParserRuleContext):
        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(DjangoNLFParser.EQUALS, 0)

        def NEQUALS(self):
            return self.getToken(DjangoNLFParser.NEQUALS, 0)

        def CONTAINS(self):
            return self.getToken(DjangoNLFParser.CONTAINS, 0)

        def NCONTAINS(self):
            return self.getToken(DjangoNLFParser.NCONTAINS, 0)

        def REGEX(self):
            return self.getToken(DjangoNLFParser.REGEX, 0)

        def NREGEX(self):
            return self.getToken(DjangoNLFParser.NREGEX, 0)

        def IN(self):
            return self.getToken(DjangoNLFParser.IN, 0)

        def NIN(self):
            return self.getToken(DjangoNLFParser.NIN, 0)

        def GT(self):
            return self.getToken(DjangoNLFParser.GT, 0)

        def GTE(self):
            return self.getToken(DjangoNLFParser.GTE, 0)

        def LT(self):
            return self.getToken(DjangoNLFParser.LT, 0)

        def LTE(self):
            return self.getToken(DjangoNLFParser.LTE, 0)

        def WHITESPACE(self, i: int = None):
            if i is None:
                return self.getTokens(DjangoNLFParser.WHITESPACE)

            return self.getToken(DjangoNLFParser.WHITESPACE, i)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_lookup

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enter_lookup"):
                listener.enter_lookup(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exit_lookup"):
                listener.exit_lookup(self)

    def lookup(self):

        localctx = DjangoNLFParser.LookupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lookup)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DjangoNLFParser.WHITESPACE:
                self.state = 34
                self.match(DjangoNLFParser.WHITESPACE)

            self.state = 37
            _la = self._input.LA(1)
            if not (
                (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << DjangoNLFParser.EQUALS)
                            | (1 << DjangoNLFParser.NEQUALS)
                            | (1 << DjangoNLFParser.CONTAINS)
                            | (1 << DjangoNLFParser.NCONTAINS)
                            | (1 << DjangoNLFParser.REGEX)
                            | (1 << DjangoNLFParser.NREGEX)
                            | (1 << DjangoNLFParser.IN)
                            | (1 << DjangoNLFParser.NIN)
                            | (1 << DjangoNLFParser.GT)
                            | (1 << DjangoNLFParser.GTE)
                            | (1 << DjangoNLFParser.LT)
                            | (1 << DjangoNLFParser.LTE)
                        )
                    )
                    != 0
                )
            ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DjangoNLFParser.WHITESPACE:
                self.state = 38
                self.match(DjangoNLFParser.WHITESPACE)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):
        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None  # Token
            self.field = None  # Token

        def FUNCTION(self):
            return self.getToken(DjangoNLFParser.FUNCTION, 0)

        def boolean_expr(self):
            return self.getTypedRuleContext(DjangoNLFParser.Boolean_exprContext, 0)

        def lookup(self):
            return self.getTypedRuleContext(DjangoNLFParser.LookupContext, 0)

        def TEXT(self, i: int = None):
            if i is None:
                return self.getTokens(DjangoNLFParser.TEXT)

            return self.getToken(DjangoNLFParser.TEXT, i)

        def QUOTED_TEXT(self):
            return self.getToken(DjangoNLFParser.QUOTED_TEXT, 0)

        def LISTING(self):
            return self.getToken(DjangoNLFParser.LISTING, 0)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_expression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enter_expression"):
                listener.enter_expression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exit_expression"):
                listener.exit_expression(self)

    def expression(self):

        localctx = DjangoNLFParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        self._la = 0  # Token type
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DjangoNLFParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                localctx.value = self.match(DjangoNLFParser.FUNCTION)
            elif token in [
                DjangoNLFParser.EQUALS,
                DjangoNLFParser.NEQUALS,
                DjangoNLFParser.WHITESPACE,
            ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.boolean_expr()
            elif token in [DjangoNLFParser.TEXT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                localctx.field = self.match(DjangoNLFParser.TEXT)
                self.state = 44
                self.lookup()
                self.state = 45
                localctx.value = self._input.LT(1)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << DjangoNLFParser.TEXT)
                                | (1 << DjangoNLFParser.QUOTED_TEXT)
                                | (1 << DjangoNLFParser.LISTING)
                                | (1 << DjangoNLFParser.FUNCTION)
                            )
                        )
                        != 0
                    )
                ):
                    localctx.value = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Composite_exprContext(ParserRuleContext):
        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.ExpressionContext)

            return self.getTypedRuleContext(DjangoNLFParser.ExpressionContext, i)

        def operator(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.OperatorContext)

            return self.getTypedRuleContext(DjangoNLFParser.OperatorContext, i)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_composite_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enter_composite_expr"):
                listener.enter_composite_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exit_composite_expr"):
                listener.exit_composite_expr(self)

    def composite_expr(self):

        localctx = DjangoNLFParser.Composite_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_composite_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.expression()
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 7, self._ctx)
            while _alt not in (2, ATN.INVALID_ALT_NUMBER):
                if _alt == 1:
                    self.state = 50
                    self.operator()
                    self.state = 51
                    self.expression()
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 7, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Nested_comp_exprContext(ParserRuleContext):
        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(DjangoNLFParser.OPEN_PAREN, 0)

        def composite_expr(self):
            return self.getTypedRuleContext(DjangoNLFParser.Composite_exprContext, 0)

        def CLOSE_PAREN(self):
            return self.getToken(DjangoNLFParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_nested_comp_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enter_nested_comp_expr"):
                listener.enter_nested_comp_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exit_nested_comp_expr"):
                listener.exit_nested_comp_expr(self)

    def nested_comp_expr(self):

        localctx = DjangoNLFParser.Nested_comp_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_nested_comp_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(DjangoNLFParser.OPEN_PAREN)
            self.state = 59
            self.composite_expr()
            self.state = 60
            self.match(DjangoNLFParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filter_exprContext(ParserRuleContext):
        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def composite_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.Composite_exprContext)

            return self.getTypedRuleContext(DjangoNLFParser.Composite_exprContext, i)

        def nested_comp_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.Nested_comp_exprContext)

            return self.getTypedRuleContext(DjangoNLFParser.Nested_comp_exprContext, i)

        def operator(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.OperatorContext)

            return self.getTypedRuleContext(DjangoNLFParser.OperatorContext, i)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_filter_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enter_filter_expr"):
                listener.enter_filter_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exit_filter_expr"):
                listener.exit_filter_expr(self)

    def filter_expr(self):

        localctx = DjangoNLFParser.Filter_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_filter_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                DjangoNLFParser.EQUALS,
                DjangoNLFParser.NEQUALS,
                DjangoNLFParser.WHITESPACE,
                DjangoNLFParser.TEXT,
                DjangoNLFParser.FUNCTION,
            ]:
                self.state = 62
                self.composite_expr()
            elif token in [DjangoNLFParser.OPEN_PAREN]:
                self.state = 63
                self.nested_comp_expr()
            else:
                raise NoViableAltException(self)

            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3F) == 0 and (
                (1 << _la)
                & (
                    (1 << DjangoNLFParser.AND)
                    | (1 << DjangoNLFParser.OR)
                    | (1 << DjangoNLFParser.NOT)
                    | (1 << DjangoNLFParser.WHITESPACE)
                )
            ) != 0:
                self.state = 66
                self.operator()
                self.state = 69
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [
                    DjangoNLFParser.EQUALS,
                    DjangoNLFParser.NEQUALS,
                    DjangoNLFParser.WHITESPACE,
                    DjangoNLFParser.TEXT,
                    DjangoNLFParser.FUNCTION,
                ]:
                    self.state = 67
                    self.composite_expr()
                elif token in [DjangoNLFParser.OPEN_PAREN]:
                    self.state = 68
                    self.nested_comp_expr()
                else:
                    raise NoViableAltException(self)

                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParseContext(ParserRuleContext):
        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DjangoNLFParser.EOF, 0)

        def filter_expr(self):
            return self.getTypedRuleContext(DjangoNLFParser.Filter_exprContext, 0)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_parse

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enter_parse"):
                listener.enter_parse(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exit_parse"):
                listener.exit_parse(self)

    def parse(self):

        localctx = DjangoNLFParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parse)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3F) == 0 and (
                (1 << _la)
                & (
                    (1 << DjangoNLFParser.EQUALS)
                    | (1 << DjangoNLFParser.NEQUALS)
                    | (1 << DjangoNLFParser.OPEN_PAREN)
                    | (1 << DjangoNLFParser.WHITESPACE)
                    | (1 << DjangoNLFParser.TEXT)
                    | (1 << DjangoNLFParser.FUNCTION)
                )
            ) != 0:
                self.state = 76
                self.filter_expr()

            self.state = 79
            self.match(DjangoNLFParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
