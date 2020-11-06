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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("&\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\5\2\f\n\2\3\2\3")
        buf.write("\2\5\2\20\n\2\3\3\5\3\23\n\3\3\3\3\3\5\3\27\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5!\n\5\f\5\16\5$\13\5\3\5")
        buf.write("\2\2\6\2\4\6\b\2\5\3\2\21\23\3\2\3\20\3\2\26\27\2&\2\13")
        buf.write("\3\2\2\2\4\22\3\2\2\2\6\30\3\2\2\2\b\34\3\2\2\2\n\f\7")
        buf.write("\24\2\2\13\n\3\2\2\2\13\f\3\2\2\2\f\r\3\2\2\2\r\17\t\2")
        buf.write("\2\2\16\20\7\24\2\2\17\16\3\2\2\2\17\20\3\2\2\2\20\3\3")
        buf.write("\2\2\2\21\23\7\24\2\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24")
        buf.write("\3\2\2\2\24\26\t\3\2\2\25\27\7\24\2\2\26\25\3\2\2\2\26")
        buf.write("\27\3\2\2\2\27\5\3\2\2\2\30\31\7\26\2\2\31\32\5\4\3\2")
        buf.write("\32\33\t\4\2\2\33\7\3\2\2\2\34\"\5\6\4\2\35\36\5\2\2\2")
        buf.write("\36\37\5\6\4\2\37!\3\2\2\2 \35\3\2\2\2!$\3\2\2\2\" \3")
        buf.write("\2\2\2\"#\3\2\2\2#\t\3\2\2\2$\"\3\2\2\2\7\13\17\22\26")
        buf.write("\"")
        return buf.getvalue()


class DjangoNLFParser ( Parser ):

    grammarFileName = "DjangoNLF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'>'", "'>='", 
                     "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>", "EQUALS", "NEQUALS", "LIKE", "NLIKE", 
                      "IN", "NIN", "GT", "GTE", "LT", "LTE", "BEFORE", "NBEFORE", 
                      "AFTER", "NAFTER", "AND", "OR", "NOT", "WHITESPACE", 
                      "NEWLINE", "TEXT", "QUOTED_TEXT" ]

    RULE_operator = 0
    RULE_lookup = 1
    RULE_expression = 2
    RULE_filter_exp = 3

    ruleNames =  [ "operator", "lookup", "expression", "filter_exp" ]

    EOF = Token.EOF
    EQUALS=1
    NEQUALS=2
    LIKE=3
    NLIKE=4
    IN=5
    NIN=6
    GT=7
    GTE=8
    LT=9
    LTE=10
    BEFORE=11
    NBEFORE=12
    AFTER=13
    NAFTER=14
    AND=15
    OR=16
    NOT=17
    WHITESPACE=18
    NEWLINE=19
    TEXT=20
    QUOTED_TEXT=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(DjangoNLFParser.AND, 0)

        def OR(self):
            return self.getToken(DjangoNLFParser.OR, 0)

        def NOT(self):
            return self.getToken(DjangoNLFParser.NOT, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DjangoNLFParser.WHITESPACE)
            else:
                return self.getToken(DjangoNLFParser.WHITESPACE, i)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = DjangoNLFParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DjangoNLFParser.WHITESPACE:
                self.state = 8
                self.match(DjangoNLFParser.WHITESPACE)


            self.state = 11
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DjangoNLFParser.AND) | (1 << DjangoNLFParser.OR) | (1 << DjangoNLFParser.NOT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DjangoNLFParser.WHITESPACE:
                self.state = 12
                self.match(DjangoNLFParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LookupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
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

        def BEFORE(self):
            return self.getToken(DjangoNLFParser.BEFORE, 0)

        def NBEFORE(self):
            return self.getToken(DjangoNLFParser.NBEFORE, 0)

        def AFTER(self):
            return self.getToken(DjangoNLFParser.AFTER, 0)

        def NAFTER(self):
            return self.getToken(DjangoNLFParser.NAFTER, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DjangoNLFParser.WHITESPACE)
            else:
                return self.getToken(DjangoNLFParser.WHITESPACE, i)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_lookup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLookup" ):
                listener.enterLookup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLookup" ):
                listener.exitLookup(self)




    def lookup(self):

        localctx = DjangoNLFParser.LookupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_lookup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DjangoNLFParser.WHITESPACE:
                self.state = 15
                self.match(DjangoNLFParser.WHITESPACE)


            self.state = 18
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DjangoNLFParser.EQUALS) | (1 << DjangoNLFParser.NEQUALS) | (1 << DjangoNLFParser.LIKE) | (1 << DjangoNLFParser.NLIKE) | (1 << DjangoNLFParser.IN) | (1 << DjangoNLFParser.NIN) | (1 << DjangoNLFParser.GT) | (1 << DjangoNLFParser.GTE) | (1 << DjangoNLFParser.LT) | (1 << DjangoNLFParser.LTE) | (1 << DjangoNLFParser.BEFORE) | (1 << DjangoNLFParser.NBEFORE) | (1 << DjangoNLFParser.AFTER) | (1 << DjangoNLFParser.NAFTER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DjangoNLFParser.WHITESPACE:
                self.state = 19
                self.match(DjangoNLFParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(DjangoNLFParser.TEXT)
            else:
                return self.getToken(DjangoNLFParser.TEXT, i)

        def lookup(self):
            return self.getTypedRuleContext(DjangoNLFParser.LookupContext,0)


        def QUOTED_TEXT(self):
            return self.getToken(DjangoNLFParser.QUOTED_TEXT, 0)

        def getRuleIndex(self):
            return DjangoNLFParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = DjangoNLFParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(DjangoNLFParser.TEXT)
            self.state = 23
            self.lookup()
            self.state = 24
            _la = self._input.LA(1)
            if not(_la==DjangoNLFParser.TEXT or _la==DjangoNLFParser.QUOTED_TEXT):
                self._errHandler.recoverInline(self)
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


    class Filter_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DjangoNLFParser.ExpressionContext,i)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DjangoNLFParser.OperatorContext)
            else:
                return self.getTypedRuleContext(DjangoNLFParser.OperatorContext,i)


        def getRuleIndex(self):
            return DjangoNLFParser.RULE_filter_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter_exp" ):
                listener.enterFilter_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter_exp" ):
                listener.exitFilter_exp(self)




    def filter_exp(self):

        localctx = DjangoNLFParser.Filter_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filter_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.expression()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DjangoNLFParser.AND) | (1 << DjangoNLFParser.OR) | (1 << DjangoNLFParser.NOT) | (1 << DjangoNLFParser.WHITESPACE))) != 0):
                self.state = 27
                self.operator()
                self.state = 28
                self.expression()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





