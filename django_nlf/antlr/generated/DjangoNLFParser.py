# Generated from DjangoNLF.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\5\2\22\n\2\3\2\3\2\5\2\26\n\2\3\3\5\3\31\n\3")
        buf.write("\3\3\3\3\5\3\35\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7")
        buf.write("\5'\n\5\f\5\16\5*\13\5\3\6\3\6\3\6\3\6\3\7\3\7\5\7\62")
        buf.write("\n\7\3\7\3\7\3\7\5\7\67\n\7\7\79\n\7\f\7\16\7<\13\7\3")
        buf.write("\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\5\3\2\r\17\3\2\3")
        buf.write("\f\3\2\24\26\2A\2\21\3\2\2\2\4\30\3\2\2\2\6\36\3\2\2\2")
        buf.write('\b"\3\2\2\2\n+\3\2\2\2\f\61\3\2\2\2\16=\3\2\2\2\20\22')
        buf.write("\7\22\2\2\21\20\3\2\2\2\21\22\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\25\t\2\2\2\24\26\7\22\2\2\25\24\3\2\2\2\25\26\3\2\2\2")
        buf.write("\26\3\3\2\2\2\27\31\7\22\2\2\30\27\3\2\2\2\30\31\3\2\2")
        buf.write("\2\31\32\3\2\2\2\32\34\t\3\2\2\33\35\7\22\2\2\34\33\3")
        buf.write("\2\2\2\34\35\3\2\2\2\35\5\3\2\2\2\36\37\7\24\2\2\37 \5")
        buf.write('\4\3\2 !\t\4\2\2!\7\3\2\2\2"(\5\6\4\2#$\5\2\2\2$%\5\6')
        buf.write("\4\2%'\3\2\2\2&#\3\2\2\2'*\3\2\2\2(&\3\2\2\2()\3\2\2")
        buf.write("\2)\t\3\2\2\2*(\3\2\2\2+,\7\20\2\2,-\5\b\5\2-.\7\21\2")
        buf.write("\2.\13\3\2\2\2/\62\5\b\5\2\60\62\5\n\6\2\61/\3\2\2\2\61")
        buf.write("\60\3\2\2\2\62:\3\2\2\2\63\66\5\2\2\2\64\67\5\b\5\2\65")
        buf.write("\67\5\n\6\2\66\64\3\2\2\2\66\65\3\2\2\2\679\3\2\2\28\63")
        buf.write("\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\r\3\2\2\2<:\3")
        buf.write("\2\2\2=>\5\f\7\2>?\7\2\2\3?\17\3\2\2\2\n\21\25\30\34(")
        buf.write("\61\66:")
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
        "LIKE",
        "NLIKE",
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
    ]

    RULE_operator = 0
    RULE_lookup = 1
    RULE_expression = 2
    RULE_composite_expr = 3
    RULE_nested_comp_expr = 4
    RULE_filter_expr = 5
    RULE_parse = 6

    ruleNames = [
        "operator",
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
    LIKE = 3
    NLIKE = 4
    IN = 5
    NIN = 6
    GT = 7
    GTE = 8
    LT = 9
    LTE = 10
    AND = 11
    OR = 12
    NOT = 13
    OPEN_PAREN = 14
    CLOSE_PAREN = 15
    WHITESPACE = 16
    NEWLINE = 17
    TEXT = 18
    QUOTED_TEXT = 19
    LISTING = 20

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
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
            else:
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
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DjangoNLFParser.WHITESPACE:
                self.state = 14
                self.match(DjangoNLFParser.WHITESPACE)

            self.state = 17
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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DjangoNLFParser.WHITESPACE:
                self.state = 18
                self.match(DjangoNLFParser.WHITESPACE)

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

        def LIKE(self):
            return self.getToken(DjangoNLFParser.LIKE, 0)

        def NLIKE(self):
            return self.getToken(DjangoNLFParser.NLIKE, 0)

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
            else:
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
        self.enterRule(localctx, 2, self.RULE_lookup)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DjangoNLFParser.WHITESPACE:
                self.state = 21
                self.match(DjangoNLFParser.WHITESPACE)

            self.state = 24
            _la = self._input.LA(1)
            if not (
                (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << DjangoNLFParser.EQUALS)
                            | (1 << DjangoNLFParser.NEQUALS)
                            | (1 << DjangoNLFParser.LIKE)
                            | (1 << DjangoNLFParser.NLIKE)
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
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DjangoNLFParser.WHITESPACE:
                self.state = 25
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
            self.field = None  # Token
            self.value = None  # Token

        def lookup(self):
            return self.getTypedRuleContext(DjangoNLFParser.LookupContext, 0)

        def TEXT(self, i: int = None):
            if i is None:
                return self.getTokens(DjangoNLFParser.TEXT)
            else:
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
        self.enterRule(localctx, 4, self.RULE_expression)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            localctx.field = self.match(DjangoNLFParser.TEXT)
            self.state = 29
            self.lookup()
            self.state = 30
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
            else:
                return self.getTypedRuleContext(DjangoNLFParser.ExpressionContext, i)

        def operator(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.OperatorContext)
            else:
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
        self.enterRule(localctx, 6, self.RULE_composite_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.expression()
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 33
                    self.operator()
                    self.state = 34
                    self.expression()
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)

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
            if hasattr(listener, "enterNested_comp_expr"):
                listener.enterNested_comp_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNested_comp_expr"):
                listener.exitNested_comp_expr(self)

    def nested_comp_expr(self):

        localctx = DjangoNLFParser.Nested_comp_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_nested_comp_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(DjangoNLFParser.OPEN_PAREN)
            self.state = 42
            self.composite_expr()
            self.state = 43
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
            else:
                return self.getTypedRuleContext(DjangoNLFParser.Composite_exprContext, i)

        def nested_comp_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.Nested_comp_exprContext)
            else:
                return self.getTypedRuleContext(DjangoNLFParser.Nested_comp_exprContext, i)

        def operator(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.OperatorContext)
            else:
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
        self.enterRule(localctx, 10, self.RULE_filter_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DjangoNLFParser.TEXT]:
                self.state = 45
                self.composite_expr()
                pass
            elif token in [DjangoNLFParser.OPEN_PAREN]:
                self.state = 46
                self.nested_comp_expr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 56
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
                self.state = 49
                self.operator()
                self.state = 52
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [DjangoNLFParser.TEXT]:
                    self.state = 50
                    self.composite_expr()
                    pass
                elif token in [DjangoNLFParser.OPEN_PAREN]:
                    self.state = 51
                    self.nested_comp_expr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 58
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

        def filter_expr(self):
            return self.getTypedRuleContext(DjangoNLFParser.Filter_exprContext, 0)

        def EOF(self):
            return self.getToken(DjangoNLFParser.EOF, 0)

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
        self.enterRule(localctx, 12, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.filter_expr()
            self.state = 60
            self.match(DjangoNLFParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
