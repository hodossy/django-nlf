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
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\5\2\24\n\2\3\2\3\2\5\2\30\n\2\3\3\5\3")
        buf.write("\33\n\3\3\3\3\3\6\3\37\n\3\r\3\16\3 \3\3\3\3\3\4\5\4&")
        buf.write("\n\4\3\4\3\4\5\4*\n\4\3\5\3\5\5\5.\n\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5\64\n\5\3\5\3\5\3\5\3\5\5\5:\n\5\3\6\3\6\5\6>\n\6")
        buf.write("\3\6\3\6\3\6\5\6C\n\6\7\6E\n\6\f\6\16\6H\13\6\3\7\3\7")
        buf.write("\5\7L\n\7\3\7\3\7\3\7\3\7\3\b\3\b\5\bT\n\b\3\b\3\b\3\b")
        buf.write("\5\bY\n\b\7\b[\n\b\f\b\16\b^\13\b\3\t\5\ta\n\t\3\t\3\t")
        buf.write("\3\t\2\2\n\2\4\6\b\n\f\16\20\2\7\3\2\17\20\3\2\3\4\3\2")
        buf.write("\3\16\4\2\26\26\31\31\3\2\26\31\2n\2\23\3\2\2\2\4\32\3")
        buf.write("\2\2\2\6%\3\2\2\2\b9\3\2\2\2\n=\3\2\2\2\fK\3\2\2\2\16")
        buf.write("S\3\2\2\2\20`\3\2\2\2\22\24\7\24\2\2\23\22\3\2\2\2\23")
        buf.write("\24\3\2\2\2\24\25\3\2\2\2\25\27\t\2\2\2\26\30\7\24\2\2")
        buf.write("\27\26\3\2\2\2\27\30\3\2\2\2\30\3\3\2\2\2\31\33\7\24\2")
        buf.write("\2\32\31\3\2\2\2\32\33\3\2\2\2\33\34\3\2\2\2\34\36\t\3")
        buf.write("\2\2\35\37\7\24\2\2\36\35\3\2\2\2\37 \3\2\2\2 \36\3\2")
        buf.write('\2\2 !\3\2\2\2!"\3\2\2\2"#\7\26\2\2#\5\3\2\2\2$&\7\24')
        buf.write("\2\2%$\3\2\2\2%&\3\2\2\2&'\3\2\2\2')\t\4\2\2(*\7\24")
        buf.write("\2\2)(\3\2\2\2)*\3\2\2\2*\7\3\2\2\2+,\7\21\2\2,.\7\24")
        buf.write("\2\2-+\3\2\2\2-.\3\2\2\2./\3\2\2\2/:\7\31\2\2\60:\5\4")
        buf.write("\3\2\61\62\7\21\2\2\62\64\7\24\2\2\63\61\3\2\2\2\63\64")
        buf.write("\3\2\2\2\64\65\3\2\2\2\65\66\t\5\2\2\66\67\5\6\4\2\67")
        buf.write("8\t\6\2\28:\3\2\2\29-\3\2\2\29\60\3\2\2\29\63\3\2\2\2")
        buf.write(":\t\3\2\2\2;>\5\b\5\2<>\5\f\7\2=;\3\2\2\2=<\3\2\2\2>F")
        buf.write("\3\2\2\2?B\5\2\2\2@C\5\b\5\2AC\5\f\7\2B@\3\2\2\2BA\3\2")
        buf.write("\2\2CE\3\2\2\2D?\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2")
        buf.write("G\13\3\2\2\2HF\3\2\2\2IJ\7\21\2\2JL\7\24\2\2KI\3\2\2\2")
        buf.write("KL\3\2\2\2LM\3\2\2\2MN\7\22\2\2NO\5\n\6\2OP\7\23\2\2P")
        buf.write("\r\3\2\2\2QT\5\n\6\2RT\5\f\7\2SQ\3\2\2\2SR\3\2\2\2T\\")
        buf.write("\3\2\2\2UX\5\2\2\2VY\5\n\6\2WY\5\f\7\2XV\3\2\2\2XW\3\2")
        buf.write("\2\2Y[\3\2\2\2ZU\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2")
        buf.write("\2]\17\3\2\2\2^\\\3\2\2\2_a\5\16\b\2`_\3\2\2\2`a\3\2\2")
        buf.write("\2ab\3\2\2\2bc\7\2\2\3c\21\3\2\2\2\23\23\27\32 %)-\63")
        buf.write("9=BFKSX\\`")
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

        def WHITESPACE(self, i: int = None):
            if i is None:
                return self.getTokens(DjangoNLFParser.WHITESPACE)

            return self.getToken(DjangoNLFParser.WHITESPACE, i)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_operator

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOperator"):
                listener.enterOperator(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOperator"):
                listener.exitOperator(self)

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
            if _la not in (DjangoNLFParser.AND, DjangoNLFParser.OR):
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
            if hasattr(listener, "enterBoolean_expr"):
                listener.enterBoolean_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBoolean_expr"):
                listener.exitBoolean_expr(self)

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
            if hasattr(listener, "enterLookup"):
                listener.enterLookup(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLookup"):
                listener.exitLookup(self)

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

        def FUNCTION(self, i: int = None):
            if i is None:
                return self.getTokens(DjangoNLFParser.FUNCTION)

            return self.getToken(DjangoNLFParser.FUNCTION, i)

        def NOT(self):
            return self.getToken(DjangoNLFParser.NOT, 0)

        def WHITESPACE(self):
            return self.getToken(DjangoNLFParser.WHITESPACE, 0)

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
            if hasattr(listener, "enterExpression"):
                listener.enterExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpression"):
                listener.exitExpression(self)

    def expression(self):

        localctx = DjangoNLFParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        self._la = 0  # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 8, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == DjangoNLFParser.NOT:
                    self.state = 41
                    self.match(DjangoNLFParser.NOT)
                    self.state = 42
                    self.match(DjangoNLFParser.WHITESPACE)

                self.state = 45
                localctx.value = self.match(DjangoNLFParser.FUNCTION)

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.boolean_expr()

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == DjangoNLFParser.NOT:
                    self.state = 47
                    self.match(DjangoNLFParser.NOT)
                    self.state = 48
                    self.match(DjangoNLFParser.WHITESPACE)

                self.state = 51
                localctx.field = self._input.LT(1)
                _la = self._input.LA(1)
                if _la not in (DjangoNLFParser.TEXT, DjangoNLFParser.FUNCTION):
                    localctx.field = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52
                self.lookup()
                self.state = 53
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

        def nested_comp_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.Nested_comp_exprContext)

            return self.getTypedRuleContext(DjangoNLFParser.Nested_comp_exprContext, i)

        def operator(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.OperatorContext)

            return self.getTypedRuleContext(DjangoNLFParser.OperatorContext, i)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_composite_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterComposite_expr"):
                listener.enterComposite_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitComposite_expr"):
                listener.exitComposite_expr(self)

    def composite_expr(self):

        localctx = DjangoNLFParser.Composite_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_composite_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 9, self._ctx)
            if la_ == 1:
                self.state = 57
                self.expression()

            elif la_ == 2:
                self.state = 58
                self.nested_comp_expr()

            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 11, self._ctx)
            while _alt not in (2, ATN.INVALID_ALT_NUMBER):
                if _alt == 1:
                    self.state = 61
                    self.operator()
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 10, self._ctx)
                    if la_ == 1:
                        self.state = 62
                        self.expression()

                    elif la_ == 2:
                        self.state = 63
                        self.nested_comp_expr()

                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 11, self._ctx)

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

        def NOT(self):
            return self.getToken(DjangoNLFParser.NOT, 0)

        def WHITESPACE(self):
            return self.getToken(DjangoNLFParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_nested_comp_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNested_comp_expr"):
                listener.enterNested_comp_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNested_comp_expr"):
                listener.exitNested_comp_expr(self)

    def nested_comp_expr(self):

        localctx = DjangoNLFParser.Nested_comp_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_nested_comp_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DjangoNLFParser.NOT:
                self.state = 71
                self.match(DjangoNLFParser.NOT)
                self.state = 72
                self.match(DjangoNLFParser.WHITESPACE)

            self.state = 75
            self.match(DjangoNLFParser.OPEN_PAREN)
            self.state = 76
            self.composite_expr()
            self.state = 77
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
            if hasattr(listener, "enterFilter_expr"):
                listener.enterFilter_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFilter_expr"):
                listener.exitFilter_expr(self)

    def filter_expr(self):

        localctx = DjangoNLFParser.Filter_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_filter_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 13, self._ctx)
            if la_ == 1:
                self.state = 79
                self.composite_expr()

            elif la_ == 2:
                self.state = 80
                self.nested_comp_expr()

            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3F) == 0 and (
                (1 << _la)
                & (
                    (1 << DjangoNLFParser.AND)
                    | (1 << DjangoNLFParser.OR)
                    | (1 << DjangoNLFParser.WHITESPACE)
                )
            ) != 0:
                self.state = 83
                self.operator()
                self.state = 86
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 14, self._ctx)
                if la_ == 1:
                    self.state = 84
                    self.composite_expr()

                elif la_ == 2:
                    self.state = 85
                    self.nested_comp_expr()

                self.state = 92
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
            if hasattr(listener, "enterParse"):
                listener.enterParse(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParse"):
                listener.exitParse(self)

    def parse(self):

        localctx = DjangoNLFParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parse)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3F) == 0 and (
                (1 << _la)
                & (
                    (1 << DjangoNLFParser.EQUALS)
                    | (1 << DjangoNLFParser.NEQUALS)
                    | (1 << DjangoNLFParser.NOT)
                    | (1 << DjangoNLFParser.OPEN_PAREN)
                    | (1 << DjangoNLFParser.WHITESPACE)
                    | (1 << DjangoNLFParser.TEXT)
                    | (1 << DjangoNLFParser.FUNCTION)
                )
            ) != 0:
                self.state = 93
                self.filter_expr()

            self.state = 96
            self.match(DjangoNLFParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
