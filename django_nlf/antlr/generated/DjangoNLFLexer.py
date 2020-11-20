# pylint: disable=invalid-name,missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code
# Generated from DjangoNLF.g4 by ANTLR 4.8
import sys
from io import StringIO
from typing import TextIO

from antlr4 import ATNDeserializer, DFA, Lexer, LexerATNSimulator, PredictionContextCache


def serializedATN():  # pylint: disable=too-many-statements
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u018f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write('\t\36\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\4%\t%')
        buf.write("\4&\t&\4'\t'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\177\n\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u008d")
        buf.write("\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\u009c\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u00ac\n\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u00c4\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u00cb")
        buf.write("\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\5\7\u00da\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\5\24\u0102\n\24\3\24\3\24\6")
        buf.write("\24\u0106\n\24\r\24\16\24\u0107\3\25\3\25\3\25\3\25\6")
        buf.write("\25\u010e\n\25\r\25\16\25\u010f\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\7\26\u0118\n\26\f\26\16\26\u011b\13\26\3\26\3")
        buf.write("\26\3\27\5\27\u0120\n\27\3\27\5\27\u0123\n\27\3\27\3\27")
        buf.write("\5\27\u0127\n\27\3\27\3\27\5\27\u012b\n\27\3\27\3\27\5")
        buf.write("\27\u012f\n\27\6\27\u0131\n\27\r\27\16\27\u0132\3\27\5")
        buf.write("\27\u0136\n\27\3\27\5\27\u0139\n\27\3\30\3\30\3\30\3\30")
        buf.write("\6\30\u013f\n\30\r\30\16\30\u0140\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0147\n\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3")
        buf.write("\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\5\37")
        buf.write('\u015a\n\37\3 \3 \3!\3!\3"\3"\3#\3#\3$\3$\3%\3%\3&\3')
        buf.write("&\3'\3'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\2\2:\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24'\25)\26+\27-\30/\31\61\2")
        buf.write("\63\2\65\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\2K\2M\2O\2Q\2")
        buf.write("S\2U\2W\2Y\2[\2]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2\3\2!")
        buf.write('\4\2\13\13""\3\2c|\3\2C\\\3\2\62;\5\2//\61\61<<\4\2')
        buf.write("CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4")
        buf.write("\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPp")
        buf.write("p\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2")
        buf.write("WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u0193")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\3~\3\2\2\2\5\u009b\3\2\2\2\7\u009d\3\2\2\2")
        buf.write("\t\u00a6\3\2\2\2\13\u00c3\3\2\2\2\r\u00d9\3\2\2\2\17\u00db")
        buf.write("\3\2\2\2\21\u00de\3\2\2\2\23\u00e5\3\2\2\2\25\u00e7\3")
        buf.write("\2\2\2\27\u00ea\3\2\2\2\31\u00ec\3\2\2\2\33\u00ef\3\2")
        buf.write("\2\2\35\u00f3\3\2\2\2\37\u00f6\3\2\2\2!\u00fa\3\2\2\2")
        buf.write("#\u00fc\3\2\2\2%\u00fe\3\2\2\2'\u0105\3\2\2\2)\u010d")
        buf.write("\3\2\2\2+\u0111\3\2\2\2-\u011f\3\2\2\2/\u013e\3\2\2\2")
        buf.write("\61\u014a\3\2\2\2\63\u014c\3\2\2\2\65\u014e\3\2\2\2\67")
        buf.write("\u0150\3\2\2\29\u0152\3\2\2\2;\u0154\3\2\2\2=\u0159\3")
        buf.write("\2\2\2?\u015b\3\2\2\2A\u015d\3\2\2\2C\u015f\3\2\2\2E\u0161")
        buf.write("\3\2\2\2G\u0163\3\2\2\2I\u0165\3\2\2\2K\u0167\3\2\2\2")
        buf.write("M\u0169\3\2\2\2O\u016b\3\2\2\2Q\u016d\3\2\2\2S\u016f\3")
        buf.write("\2\2\2U\u0171\3\2\2\2W\u0173\3\2\2\2Y\u0175\3\2\2\2[\u0177")
        buf.write("\3\2\2\2]\u0179\3\2\2\2_\u017b\3\2\2\2a\u017d\3\2\2\2")
        buf.write("c\u017f\3\2\2\2e\u0181\3\2\2\2g\u0183\3\2\2\2i\u0185\3")
        buf.write("\2\2\2k\u0187\3\2\2\2m\u0189\3\2\2\2o\u018b\3\2\2\2q\u018d")
        buf.write("\3\2\2\2st\5O(\2tu\5c\62\2u\177\3\2\2\2vw\5G$\2wx\5_\60")
        buf.write("\2xy\5g\64\2yz\5? \2z{\5U+\2{|\5c\62\2|\177\3\2\2\2}\177")
        buf.write("\7?\2\2~s\3\2\2\2~v\3\2\2\2~}\3\2\2\2\177\4\3\2\2\2\u0080")
        buf.write('\u0081\5O(\2\u0081\u0082\5c\62\2\u0082\u0083\7"\2\2\u0083')
        buf.write("\u0084\5Y-\2\u0084\u0085\5[.\2\u0085\u0086\5e\63\2\u0086")
        buf.write("\u009c\3\2\2\2\u0087\u0088\5E#\2\u0088\u008c\5[.\2\u0089")
        buf.write("\u008a\5G$\2\u008a\u008b\5c\62\2\u008b\u008d\3\2\2\2\u008c")
        buf.write("\u0089\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write('\u008e\u008f\7"\2\2\u008f\u0090\5Y-\2\u0090\u0091\5[')
        buf.write('.\2\u0091\u0092\5e\63\2\u0092\u0093\7"\2\2\u0093\u0094')
        buf.write("\5G$\2\u0094\u0095\5_\60\2\u0095\u0096\5g\64\2\u0096\u0097")
        buf.write("\5? \2\u0097\u0098\5U+\2\u0098\u009c\3\2\2\2\u0099\u009a")
        buf.write("\7#\2\2\u009a\u009c\7?\2\2\u009b\u0080\3\2\2\2\u009b\u0087")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009c\6\3\2\2\2\u009d\u009e")
        buf.write('\5C"\2\u009e\u009f\5[.\2\u009f\u00a0\5Y-\2\u00a0\u00a1')
        buf.write("\5e\63\2\u00a1\u00a2\5? \2\u00a2\u00a3\5O(\2\u00a3\u00a4")
        buf.write("\5Y-\2\u00a4\u00a5\5c\62\2\u00a5\b\3\2\2\2\u00a6\u00a7")
        buf.write("\5E#\2\u00a7\u00ab\5[.\2\u00a8\u00a9\5G$\2\u00a9\u00aa")
        buf.write("\5c\62\2\u00aa\u00ac\3\2\2\2\u00ab\u00a8\3\2\2\2\u00ab")
        buf.write('\u00ac\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\7"\2\2')
        buf.write("\u00ae\u00af\5Y-\2\u00af\u00b0\5[.\2\u00b0\u00b1\5e\63")
        buf.write('\2\u00b1\u00b2\7"\2\2\u00b2\u00b3\5C"\2\u00b3\u00b4')
        buf.write("\5[.\2\u00b4\u00b5\5Y-\2\u00b5\u00b6\5e\63\2\u00b6\u00b7")
        buf.write("\5? \2\u00b7\u00b8\5O(\2\u00b8\u00b9\5Y-\2\u00b9\n\3\2")
        buf.write("\2\2\u00ba\u00bb\5W,\2\u00bb\u00bc\5? \2\u00bc\u00bd\5")
        buf.write("e\63\2\u00bd\u00be\5C\"\2\u00be\u00bf\5M'\2\u00bf\u00c0")
        buf.write("\5G$\2\u00c0\u00c1\5c\62\2\u00c1\u00c4\3\2\2\2\u00c2\u00c4")
        buf.write("\7\u0080\2\2\u00c3\u00ba\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4")
        buf.write("\f\3\2\2\2\u00c5\u00c6\5E#\2\u00c6\u00ca\5[.\2\u00c7\u00c8")
        buf.write("\5G$\2\u00c8\u00c9\5c\62\2\u00c9\u00cb\3\2\2\2\u00ca\u00c7")
        buf.write("\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc")
        buf.write('\u00cd\7"\2\2\u00cd\u00ce\5Y-\2\u00ce\u00cf\5[.\2\u00cf')
        buf.write('\u00d0\5e\63\2\u00d0\u00d1\7"\2\2\u00d1\u00d2\5W,\2\u00d2')
        buf.write('\u00d3\5? \2\u00d3\u00d4\5e\63\2\u00d4\u00d5\5C"\2\u00d5')
        buf.write("\u00d6\5M'\2\u00d6\u00da\3\2\2\2\u00d7\u00d8\7#\2\2\u00d8")
        buf.write("\u00da\7\u0080\2\2\u00d9\u00c5\3\2\2\2\u00d9\u00d7\3\2")
        buf.write("\2\2\u00da\16\3\2\2\2\u00db\u00dc\5O(\2\u00dc\u00dd\5")
        buf.write("Y-\2\u00dd\20\3\2\2\2\u00de\u00df\5Y-\2\u00df\u00e0\5")
        buf.write('[.\2\u00e0\u00e1\5e\63\2\u00e1\u00e2\7"\2\2\u00e2\u00e3')
        buf.write("\5O(\2\u00e3\u00e4\5Y-\2\u00e4\22\3\2\2\2\u00e5\u00e6")
        buf.write("\7@\2\2\u00e6\24\3\2\2\2\u00e7\u00e8\7@\2\2\u00e8\u00e9")
        buf.write("\7?\2\2\u00e9\26\3\2\2\2\u00ea\u00eb\7>\2\2\u00eb\30\3")
        buf.write("\2\2\2\u00ec\u00ed\7>\2\2\u00ed\u00ee\7?\2\2\u00ee\32")
        buf.write("\3\2\2\2\u00ef\u00f0\5? \2\u00f0\u00f1\5Y-\2\u00f1\u00f2")
        buf.write("\5E#\2\u00f2\34\3\2\2\2\u00f3\u00f4\5[.\2\u00f4\u00f5")
        buf.write("\5a\61\2\u00f5\36\3\2\2\2\u00f6\u00f7\5Y-\2\u00f7\u00f8")
        buf.write("\5[.\2\u00f8\u00f9\5e\63\2\u00f9 \3\2\2\2\u00fa\u00fb")
        buf.write('\7*\2\2\u00fb"\3\2\2\2\u00fc\u00fd\7+\2\2\u00fd$\3\2')
        buf.write("\2\2\u00fe\u00ff\t\2\2\2\u00ff&\3\2\2\2\u0100\u0102\7")
        buf.write("\17\2\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\u0103\3\2\2\2\u0103\u0106\7\f\2\2\u0104\u0106\7\17\2")
        buf.write("\2\u0105\u0101\3\2\2\2\u0105\u0104\3\2\2\2\u0106\u0107")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("(\3\2\2\2\u0109\u010e\5\65\33\2\u010a\u010e\5\67\34\2")
        buf.write("\u010b\u010e\59\35\2\u010c\u010e\5=\37\2\u010d\u0109\3")
        buf.write("\2\2\2\u010d\u010a\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010c")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u010d\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110*\3\2\2\2\u0111\u0119\5\63\32\2\u0112")
        buf.write("\u0118\5\65\33\2\u0113\u0118\5\67\34\2\u0114\u0118\59")
        buf.write("\35\2\u0115\u0118\5=\37\2\u0116\u0118\5%\23\2\u0117\u0112")
        buf.write("\3\2\2\2\u0117\u0113\3\2\2\2\u0117\u0114\3\2\2\2\u0117")
        buf.write("\u0115\3\2\2\2\u0117\u0116\3\2\2\2\u0118\u011b\3\2\2\2")
        buf.write("\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011c\3")
        buf.write("\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d\5\63\32\2\u011d")
        buf.write(",\3\2\2\2\u011e\u0120\5!\21\2\u011f\u011e\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u0123\5%\23\2")
        buf.write("\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0126\3")
        buf.write("\2\2\2\u0124\u0127\5)\25\2\u0125\u0127\5+\26\2\u0126\u0124")
        buf.write("\3\2\2\2\u0126\u0125\3\2\2\2\u0127\u0130\3\2\2\2\u0128")
        buf.write("\u012a\5\61\31\2\u0129\u012b\5%\23\2\u012a\u0129\3\2\2")
        buf.write("\2\u012a\u012b\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012f")
        buf.write("\5)\25\2\u012d\u012f\5+\26\2\u012e\u012c\3\2\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012f\u0131\3\2\2\2\u0130\u0128\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3")
        buf.write("\2\2\2\u0133\u0135\3\2\2\2\u0134\u0136\5%\23\2\u0135\u0134")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0138\3\2\2\2\u0137")
        buf.write("\u0139\5#\22\2\u0138\u0137\3\2\2\2\u0138\u0139\3\2\2\2")
        buf.write("\u0139.\3\2\2\2\u013a\u013f\5\65\33\2\u013b\u013f\5\67")
        buf.write("\34\2\u013c\u013f\59\35\2\u013d\u013f\5;\36\2\u013e\u013a")
        buf.write("\3\2\2\2\u013e\u013b\3\2\2\2\u013e\u013c\3\2\2\2\u013e")
        buf.write("\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u013e\3\2\2\2")
        buf.write("\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0146\5")
        buf.write("!\21\2\u0143\u0147\5)\25\2\u0144\u0147\5+\26\2\u0145\u0147")
        buf.write("\5-\27\2\u0146\u0143\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u0149\5#\22\2\u0149\60\3\2\2\2\u014a\u014b\7.\2")
        buf.write("\2\u014b\62\3\2\2\2\u014c\u014d\7$\2\2\u014d\64\3\2\2")
        buf.write("\2\u014e\u014f\t\3\2\2\u014f\66\3\2\2\2\u0150\u0151\t")
        buf.write("\4\2\2\u01518\3\2\2\2\u0152\u0153\t\5\2\2\u0153:\3\2\2")
        buf.write("\2\u0154\u0155\7a\2\2\u0155<\3\2\2\2\u0156\u015a\7\60")
        buf.write("\2\2\u0157\u015a\5;\36\2\u0158\u015a\t\6\2\2\u0159\u0156")
        buf.write("\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015a")
        buf.write(">\3\2\2\2\u015b\u015c\t\7\2\2\u015c@\3\2\2\2\u015d\u015e")
        buf.write("\t\b\2\2\u015eB\3\2\2\2\u015f\u0160\t\t\2\2\u0160D\3\2")
        buf.write("\2\2\u0161\u0162\t\n\2\2\u0162F\3\2\2\2\u0163\u0164\t")
        buf.write("\13\2\2\u0164H\3\2\2\2\u0165\u0166\t\f\2\2\u0166J\3\2")
        buf.write("\2\2\u0167\u0168\t\r\2\2\u0168L\3\2\2\2\u0169\u016a\t")
        buf.write("\16\2\2\u016aN\3\2\2\2\u016b\u016c\t\17\2\2\u016cP\3\2")
        buf.write("\2\2\u016d\u016e\t\20\2\2\u016eR\3\2\2\2\u016f\u0170\t")
        buf.write("\21\2\2\u0170T\3\2\2\2\u0171\u0172\t\22\2\2\u0172V\3\2")
        buf.write("\2\2\u0173\u0174\t\23\2\2\u0174X\3\2\2\2\u0175\u0176\t")
        buf.write("\24\2\2\u0176Z\3\2\2\2\u0177\u0178\t\25\2\2\u0178\\\3")
        buf.write("\2\2\2\u0179\u017a\t\26\2\2\u017a^\3\2\2\2\u017b\u017c")
        buf.write("\t\27\2\2\u017c`\3\2\2\2\u017d\u017e\t\30\2\2\u017eb\3")
        buf.write("\2\2\2\u017f\u0180\t\31\2\2\u0180d\3\2\2\2\u0181\u0182")
        buf.write("\t\32\2\2\u0182f\3\2\2\2\u0183\u0184\t\33\2\2\u0184h\3")
        buf.write("\2\2\2\u0185\u0186\t\34\2\2\u0186j\3\2\2\2\u0187\u0188")
        buf.write("\t\35\2\2\u0188l\3\2\2\2\u0189\u018a\t\36\2\2\u018an\3")
        buf.write("\2\2\2\u018b\u018c\t\37\2\2\u018cp\3\2\2\2\u018d\u018e")
        buf.write("\t \2\2\u018er\3\2\2\2\35\2~\u008c\u009b\u00ab\u00c3\u00ca")
        buf.write("\u00d9\u0101\u0105\u0107\u010d\u010f\u0117\u0119\u011f")
        buf.write("\u0122\u0126\u012a\u012e\u0132\u0135\u0138\u013e\u0140")
        buf.write("\u0146\u0159\2")
        return buf.getvalue()


class DjangoNLFLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

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

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>", "'>'", "'>='", "'<'", "'<='", "'('", "')'"]

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

    ruleNames = [
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
        "COMA",
        "QUOTE",
        "LOWERCASE",
        "UPPERCASE",
        "NUMBER",
        "UNDERSCORE",
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

    def __init__(self, input_=None, output: TextIO = sys.stdout):
        super().__init__(input_, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache()
        )
        self._actions = None
        self._predicates = None
