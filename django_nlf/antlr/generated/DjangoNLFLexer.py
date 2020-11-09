# Generated from DjangoNLF.g4 by ANTLR 4.8
import sys
from io import StringIO
from typing import TextIO

from antlr4 import (
    ATNDeserializer,
    DFA,
    Lexer,
    LexerATNSimulator,
    PredictionContextCache,
)


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u013f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write('\t\36\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\4%\t%')
        buf.write("\4&\t&\4'\t'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\5\2w\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u008d\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0098\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5\u00a8\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\5\22\u00d0\n\22\3\22\3\22\6\22\u00d4")
        buf.write("\n\22\r\22\16\22\u00d5\3\23\3\23\3\23\3\23\6\23\u00dc")
        buf.write("\n\23\r\23\16\23\u00dd\3\24\3\24\3\24\3\24\3\24\3\24\6")
        buf.write("\24\u00e6\n\24\r\24\16\24\u00e7\3\24\3\24\3\25\3\25\5")
        buf.write("\25\u00ee\n\25\3\25\3\25\3\25\5\25\u00f3\n\25\3\25\3\25")
        buf.write("\6\25\u00f7\n\25\r\25\16\25\u00f8\3\25\5\25\u00fc\n\25")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3'\3'\3")
        buf.write("(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\2\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24'\25)\26+\2")
        buf.write("-\2/\2\61\2\63\2\65\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\2")
        buf.write("K\2M\2O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a\2c\2e\2g\2i\2\3\2!")
        buf.write('\4\2\13\13""\3\2c|\3\2C\\\3\2\62;\4\2\60\60aa\4\2CC')
        buf.write("cc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2")
        buf.write("JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4")
        buf.write("\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWw")
        buf.write("w\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u0134\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2'\3\2\2\2\2)\3\2\2\2\3v\3\2\2\2\5\u008c\3\2")
        buf.write("\2\2\7\u0097\3\2\2\2\t\u00a7\3\2\2\2\13\u00a9\3\2\2\2")
        buf.write("\r\u00ac\3\2\2\2\17\u00b3\3\2\2\2\21\u00b5\3\2\2\2\23")
        buf.write("\u00b8\3\2\2\2\25\u00ba\3\2\2\2\27\u00bd\3\2\2\2\31\u00c1")
        buf.write("\3\2\2\2\33\u00c4\3\2\2\2\35\u00c8\3\2\2\2\37\u00ca\3")
        buf.write("\2\2\2!\u00cc\3\2\2\2#\u00d3\3\2\2\2%\u00db\3\2\2\2'")
        buf.write("\u00df\3\2\2\2)\u00eb\3\2\2\2+\u00ff\3\2\2\2-\u0101\3")
        buf.write("\2\2\2/\u0103\3\2\2\2\61\u0105\3\2\2\2\63\u0107\3\2\2")
        buf.write("\2\65\u0109\3\2\2\2\67\u010b\3\2\2\29\u010d\3\2\2\2;\u010f")
        buf.write("\3\2\2\2=\u0111\3\2\2\2?\u0113\3\2\2\2A\u0115\3\2\2\2")
        buf.write("C\u0117\3\2\2\2E\u0119\3\2\2\2G\u011b\3\2\2\2I\u011d\3")
        buf.write("\2\2\2K\u011f\3\2\2\2M\u0121\3\2\2\2O\u0123\3\2\2\2Q\u0125")
        buf.write("\3\2\2\2S\u0127\3\2\2\2U\u0129\3\2\2\2W\u012b\3\2\2\2")
        buf.write("Y\u012d\3\2\2\2[\u012f\3\2\2\2]\u0131\3\2\2\2_\u0133\3")
        buf.write("\2\2\2a\u0135\3\2\2\2c\u0137\3\2\2\2e\u0139\3\2\2\2g\u013b")
        buf.write("\3\2\2\2i\u013d\3\2\2\2kl\5G$\2lm\5[.\2mw\3\2\2\2no\5")
        buf.write("? \2op\5W,\2pq\5_\60\2qr\5\67\34\2rs\5M'\2st\5[.\2tw")
        buf.write("\3\2\2\2uw\7?\2\2vk\3\2\2\2vn\3\2\2\2vu\3\2\2\2w\4\3\2")
        buf.write('\2\2xy\5G$\2yz\5[.\2z{\7"\2\2{|\5Q)\2|}\5S*\2}~\5]/\2')
        buf.write("~\u008d\3\2\2\2\177\u0080\5Q)\2\u0080\u0081\5S*\2\u0081")
        buf.write('\u0082\5]/\2\u0082\u0083\7"\2\2\u0083\u0084\5? \2\u0084')
        buf.write("\u0085\5W,\2\u0085\u0086\5_\60\2\u0086\u0087\5\67\34\2")
        buf.write("\u0087\u0088\5M'\2\u0088\u0089\5[.\2\u0089\u008d\3\2")
        buf.write("\2\2\u008a\u008b\7#\2\2\u008b\u008d\7?\2\2\u008cx\3\2")
        buf.write("\2\2\u008c\177\3\2\2\2\u008c\u008a\3\2\2\2\u008d\6\3\2")
        buf.write("\2\2\u008e\u008f\5G$\2\u008f\u0090\5[.\2\u0090\u0091\7")
        buf.write("\"\2\2\u0091\u0092\5M'\2\u0092\u0093\5G$\2\u0093\u0094")
        buf.write("\5K&\2\u0094\u0095\5? \2\u0095\u0098\3\2\2\2\u0096\u0098")
        buf.write("\7\u0080\2\2\u0097\u008e\3\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\b\3\2\2\2\u0099\u009a\5G$\2\u009a\u009b\5[.\2\u009b\u009c")
        buf.write('\7"\2\2\u009c\u009d\5Q)\2\u009d\u009e\5S*\2\u009e\u009f')
        buf.write("\5]/\2\u009f\u00a0\7\"\2\2\u00a0\u00a1\5M'\2\u00a1\u00a2")
        buf.write("\5G$\2\u00a2\u00a3\5K&\2\u00a3\u00a4\5? \2\u00a4\u00a8")
        buf.write("\3\2\2\2\u00a5\u00a6\7#\2\2\u00a6\u00a8\7\u0080\2\2\u00a7")
        buf.write("\u0099\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\n\3\2\2\2\u00a9")
        buf.write("\u00aa\5G$\2\u00aa\u00ab\5Q)\2\u00ab\f\3\2\2\2\u00ac\u00ad")
        buf.write("\5Q)\2\u00ad\u00ae\5S*\2\u00ae\u00af\5]/\2\u00af\u00b0")
        buf.write('\7"\2\2\u00b0\u00b1\5G$\2\u00b1\u00b2\5Q)\2\u00b2\16')
        buf.write("\3\2\2\2\u00b3\u00b4\7@\2\2\u00b4\20\3\2\2\2\u00b5\u00b6")
        buf.write("\7@\2\2\u00b6\u00b7\7?\2\2\u00b7\22\3\2\2\2\u00b8\u00b9")
        buf.write("\7>\2\2\u00b9\24\3\2\2\2\u00ba\u00bb\7>\2\2\u00bb\u00bc")
        buf.write("\7?\2\2\u00bc\26\3\2\2\2\u00bd\u00be\5\67\34\2\u00be\u00bf")
        buf.write("\5Q)\2\u00bf\u00c0\5=\37\2\u00c0\30\3\2\2\2\u00c1\u00c2")
        buf.write("\5S*\2\u00c2\u00c3\5Y-\2\u00c3\32\3\2\2\2\u00c4\u00c5")
        buf.write("\5Q)\2\u00c5\u00c6\5S*\2\u00c6\u00c7\5]/\2\u00c7\34\3")
        buf.write("\2\2\2\u00c8\u00c9\7*\2\2\u00c9\36\3\2\2\2\u00ca\u00cb")
        buf.write('\7+\2\2\u00cb \3\2\2\2\u00cc\u00cd\t\2\2\2\u00cd"\3\2')
        buf.write("\2\2\u00ce\u00d0\7\17\2\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d4\7\f\2\2\u00d2")
        buf.write("\u00d4\7\17\2\2\u00d3\u00cf\3\2\2\2\u00d3\u00d2\3\2\2")
        buf.write("\2\u00d4\u00d5\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6")
        buf.write("\3\2\2\2\u00d6$\3\2\2\2\u00d7\u00dc\5/\30\2\u00d8\u00dc")
        buf.write("\5\61\31\2\u00d9\u00dc\5\63\32\2\u00da\u00dc\5\65\33\2")
        buf.write("\u00db\u00d7\3\2\2\2\u00db\u00d8\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00db\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00db")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de&\3\2\2\2\u00df\u00e5")
        buf.write("\5-\27\2\u00e0\u00e6\5/\30\2\u00e1\u00e6\5\61\31\2\u00e2")
        buf.write("\u00e6\5\63\32\2\u00e3\u00e6\5\65\33\2\u00e4\u00e6\5!")
        buf.write("\21\2\u00e5\u00e0\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e5\u00e2")
        buf.write("\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\u00ea\5-\27\2\u00ea(\3\2\2")
        buf.write("\2\u00eb\u00ed\5\35\17\2\u00ec\u00ee\5!\21\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\u00f6\5%\23\2\u00f0\u00f2\5+\26\2\u00f1\u00f3\5!\21\2")
        buf.write("\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\3")
        buf.write("\2\2\2\u00f4\u00f5\5%\23\2\u00f5\u00f7\3\2\2\2\u00f6\u00f0")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00fc\5!\21\2")
        buf.write("\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3")
        buf.write("\2\2\2\u00fd\u00fe\5\37\20\2\u00fe*\3\2\2\2\u00ff\u0100")
        buf.write("\7.\2\2\u0100,\3\2\2\2\u0101\u0102\7$\2\2\u0102.\3\2\2")
        buf.write("\2\u0103\u0104\t\3\2\2\u0104\60\3\2\2\2\u0105\u0106\t")
        buf.write("\4\2\2\u0106\62\3\2\2\2\u0107\u0108\t\5\2\2\u0108\64\3")
        buf.write("\2\2\2\u0109\u010a\t\6\2\2\u010a\66\3\2\2\2\u010b\u010c")
        buf.write("\t\7\2\2\u010c8\3\2\2\2\u010d\u010e\t\b\2\2\u010e:\3\2")
        buf.write("\2\2\u010f\u0110\t\t\2\2\u0110<\3\2\2\2\u0111\u0112\t")
        buf.write("\n\2\2\u0112>\3\2\2\2\u0113\u0114\t\13\2\2\u0114@\3\2")
        buf.write("\2\2\u0115\u0116\t\f\2\2\u0116B\3\2\2\2\u0117\u0118\t")
        buf.write("\r\2\2\u0118D\3\2\2\2\u0119\u011a\t\16\2\2\u011aF\3\2")
        buf.write("\2\2\u011b\u011c\t\17\2\2\u011cH\3\2\2\2\u011d\u011e\t")
        buf.write("\20\2\2\u011eJ\3\2\2\2\u011f\u0120\t\21\2\2\u0120L\3\2")
        buf.write("\2\2\u0121\u0122\t\22\2\2\u0122N\3\2\2\2\u0123\u0124\t")
        buf.write("\23\2\2\u0124P\3\2\2\2\u0125\u0126\t\24\2\2\u0126R\3\2")
        buf.write("\2\2\u0127\u0128\t\25\2\2\u0128T\3\2\2\2\u0129\u012a\t")
        buf.write("\26\2\2\u012aV\3\2\2\2\u012b\u012c\t\27\2\2\u012cX\3\2")
        buf.write("\2\2\u012d\u012e\t\30\2\2\u012eZ\3\2\2\2\u012f\u0130\t")
        buf.write("\31\2\2\u0130\\\3\2\2\2\u0131\u0132\t\32\2\2\u0132^\3")
        buf.write("\2\2\2\u0133\u0134\t\33\2\2\u0134`\3\2\2\2\u0135\u0136")
        buf.write("\t\34\2\2\u0136b\3\2\2\2\u0137\u0138\t\35\2\2\u0138d\3")
        buf.write("\2\2\2\u0139\u013a\t\36\2\2\u013af\3\2\2\2\u013b\u013c")
        buf.write("\t\37\2\2\u013ch\3\2\2\2\u013d\u013e\t \2\2\u013ej\3\2")
        buf.write("\2\2\22\2v\u008c\u0097\u00a7\u00cf\u00d3\u00d5\u00db\u00dd")
        buf.write("\u00e5\u00e7\u00ed\u00f2\u00f8\u00fb\2")
        return buf.getvalue()


class DjangoNLFLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

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

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>", "'>'", "'>='", "'<'", "'<='", "'('", "')'"]

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

    ruleNames = [
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
        "COMA",
        "QUOTE",
        "LOWERCASE",
        "UPPERCASE",
        "NUMBER",
        "SYMBOL",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    grammarFileName = "DjangoNLF.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache()
        )
        self._actions = None
        self._predicates = None
