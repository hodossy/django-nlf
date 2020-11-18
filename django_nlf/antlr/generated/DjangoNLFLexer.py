# pylint: disable=invalid-name,missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code
# Generated from DjangoNLF.g4 by ANTLR 4.8
import sys
from io import StringIO
from typing import TextIO

from antlr4 import ATNDeserializer, DFA, Lexer, LexerATNSimulator, PredictionContextCache


def serializedATN():  # pylint: disable=too-many-statements
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u018a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write('\t\36\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\4%\t%')
        buf.write("\4&\t&\4'\t'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\177\n\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3\u0095\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u00a3\n\5\3\5\5\5\u00a6")
        buf.write("\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00be\n\6\3")
        buf.write("\7\3\7\3\7\5\7\u00c3\n\7\3\7\5\7\u00c6\n\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00d5\n\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\5\24\u00fd\n\24\3\24\3\24\6\24\u0101\n\24\r")
        buf.write("\24\16\24\u0102\3\25\3\25\3\25\3\25\6\25\u0109\n\25\r")
        buf.write("\25\16\25\u010a\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0113")
        buf.write("\n\26\f\26\16\26\u0116\13\26\3\26\3\26\3\27\5\27\u011b")
        buf.write("\n\27\3\27\5\27\u011e\n\27\3\27\3\27\5\27\u0122\n\27\3")
        buf.write("\27\3\27\5\27\u0126\n\27\3\27\3\27\5\27\u012a\n\27\6\27")
        buf.write("\u012c\n\27\r\27\16\27\u012d\3\27\5\27\u0131\n\27\3\27")
        buf.write("\5\27\u0134\n\27\3\30\3\30\3\30\3\30\6\30\u013a\n\30\r")
        buf.write("\30\16\30\u013b\3\30\3\30\3\30\3\30\5\30\u0142\n\30\3")
        buf.write("\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\5\37\u0155\n\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3'\3'\3(\3(\3)")
        buf.write("\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\2\2:\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24'\25)\26+\27-\30/\31\61\2\63\2\65\2\67\29\2;\2=\2")
        buf.write("?\2A\2C\2E\2G\2I\2K\2M\2O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a\2")
        buf.write('c\2e\2g\2i\2k\2m\2o\2q\2\3\2!\4\2\13\13""\3\2c|\3\2')
        buf.write("C\\\3\2\62;\5\2//\61\61<<\4\2CCcc\4\2DDdd\4\2EEee\4\2")
        buf.write("FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4")
        buf.write("\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSs")
        buf.write("s\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2")
        buf.write("ZZzz\4\2[[{{\4\2\\\\||\2\u018f\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\3~\3\2\2\2\5\u0094")
        buf.write("\3\2\2\2\7\u0096\3\2\2\2\t\u009f\3\2\2\2\13\u00bd\3\2")
        buf.write("\2\2\r\u00d4\3\2\2\2\17\u00d6\3\2\2\2\21\u00d9\3\2\2\2")
        buf.write("\23\u00e0\3\2\2\2\25\u00e2\3\2\2\2\27\u00e5\3\2\2\2\31")
        buf.write("\u00e7\3\2\2\2\33\u00ea\3\2\2\2\35\u00ee\3\2\2\2\37\u00f1")
        buf.write("\3\2\2\2!\u00f5\3\2\2\2#\u00f7\3\2\2\2%\u00f9\3\2\2\2")
        buf.write("'\u0100\3\2\2\2)\u0108\3\2\2\2+\u010c\3\2\2\2-\u011a")
        buf.write("\3\2\2\2/\u0139\3\2\2\2\61\u0145\3\2\2\2\63\u0147\3\2")
        buf.write("\2\2\65\u0149\3\2\2\2\67\u014b\3\2\2\29\u014d\3\2\2\2")
        buf.write(";\u014f\3\2\2\2=\u0154\3\2\2\2?\u0156\3\2\2\2A\u0158\3")
        buf.write("\2\2\2C\u015a\3\2\2\2E\u015c\3\2\2\2G\u015e\3\2\2\2I\u0160")
        buf.write("\3\2\2\2K\u0162\3\2\2\2M\u0164\3\2\2\2O\u0166\3\2\2\2")
        buf.write("Q\u0168\3\2\2\2S\u016a\3\2\2\2U\u016c\3\2\2\2W\u016e\3")
        buf.write("\2\2\2Y\u0170\3\2\2\2[\u0172\3\2\2\2]\u0174\3\2\2\2_\u0176")
        buf.write("\3\2\2\2a\u0178\3\2\2\2c\u017a\3\2\2\2e\u017c\3\2\2\2")
        buf.write("g\u017e\3\2\2\2i\u0180\3\2\2\2k\u0182\3\2\2\2m\u0184\3")
        buf.write("\2\2\2o\u0186\3\2\2\2q\u0188\3\2\2\2st\5O(\2tu\5c\62\2")
        buf.write("u\177\3\2\2\2vw\5G$\2wx\5_\60\2xy\5g\64\2yz\5? \2z{\5")
        buf.write("U+\2{|\5c\62\2|\177\3\2\2\2}\177\7?\2\2~s\3\2\2\2~v\3")
        buf.write("\2\2\2~}\3\2\2\2\177\4\3\2\2\2\u0080\u0081\5O(\2\u0081")
        buf.write('\u0082\5c\62\2\u0082\u0083\7"\2\2\u0083\u0084\5Y-\2\u0084')
        buf.write("\u0085\5[.\2\u0085\u0086\5e\63\2\u0086\u0095\3\2\2\2\u0087")
        buf.write("\u0088\5Y-\2\u0088\u0089\5[.\2\u0089\u008a\5e\63\2\u008a")
        buf.write('\u008b\7"\2\2\u008b\u008c\5G$\2\u008c\u008d\5_\60\2\u008d')
        buf.write("\u008e\5g\64\2\u008e\u008f\5? \2\u008f\u0090\5U+\2\u0090")
        buf.write("\u0091\5c\62\2\u0091\u0095\3\2\2\2\u0092\u0093\7#\2\2")
        buf.write("\u0093\u0095\7?\2\2\u0094\u0080\3\2\2\2\u0094\u0087\3")
        buf.write("\2\2\2\u0094\u0092\3\2\2\2\u0095\6\3\2\2\2\u0096\u0097")
        buf.write('\5C"\2\u0097\u0098\5[.\2\u0098\u0099\5Y-\2\u0099\u009a')
        buf.write("\5e\63\2\u009a\u009b\5? \2\u009b\u009c\5O(\2\u009c\u009d")
        buf.write("\5Y-\2\u009d\u009e\5c\62\2\u009e\b\3\2\2\2\u009f\u00a0")
        buf.write("\5E#\2\u00a0\u00a2\5[.\2\u00a1\u00a3\5G$\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4")
        buf.write("\u00a6\5c\62\2\u00a5\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write('\u00a6\u00a7\3\2\2\2\u00a7\u00a8\7"\2\2\u00a8\u00a9\5')
        buf.write("Y-\2\u00a9\u00aa\5[.\2\u00aa\u00ab\5e\63\2\u00ab\u00ac")
        buf.write('\7"\2\2\u00ac\u00ad\5C"\2\u00ad\u00ae\5[.\2\u00ae\u00af')
        buf.write("\5Y-\2\u00af\u00b0\5e\63\2\u00b0\u00b1\5? \2\u00b1\u00b2")
        buf.write("\5O(\2\u00b2\u00b3\5Y-\2\u00b3\n\3\2\2\2\u00b4\u00b5\5")
        buf.write("W,\2\u00b5\u00b6\5? \2\u00b6\u00b7\5e\63\2\u00b7\u00b8")
        buf.write("\5C\"\2\u00b8\u00b9\5M'\2\u00b9\u00ba\5G$\2\u00ba\u00bb")
        buf.write("\5c\62\2\u00bb\u00be\3\2\2\2\u00bc\u00be\7\u0080\2\2\u00bd")
        buf.write("\u00b4\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\f\3\2\2\2\u00bf")
        buf.write("\u00c0\5E#\2\u00c0\u00c2\5[.\2\u00c1\u00c3\5G$\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3\2\2\2")
        buf.write("\u00c4\u00c6\5c\62\2\u00c5\u00c4\3\2\2\2\u00c5\u00c6\3")
        buf.write('\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\7"\2\2\u00c8\u00c9')
        buf.write("\5Y-\2\u00c9\u00ca\5[.\2\u00ca\u00cb\5e\63\2\u00cb\u00cc")
        buf.write('\7"\2\2\u00cc\u00cd\5W,\2\u00cd\u00ce\5? \2\u00ce\u00cf')
        buf.write("\5e\63\2\u00cf\u00d0\5C\"\2\u00d0\u00d1\5M'\2\u00d1\u00d5")
        buf.write("\3\2\2\2\u00d2\u00d3\7#\2\2\u00d3\u00d5\7\u0080\2\2\u00d4")
        buf.write("\u00bf\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\16\3\2\2\2\u00d6")
        buf.write("\u00d7\5O(\2\u00d7\u00d8\5Y-\2\u00d8\20\3\2\2\2\u00d9")
        buf.write("\u00da\5Y-\2\u00da\u00db\5[.\2\u00db\u00dc\5e\63\2\u00dc")
        buf.write('\u00dd\7"\2\2\u00dd\u00de\5O(\2\u00de\u00df\5Y-\2\u00df')
        buf.write("\22\3\2\2\2\u00e0\u00e1\7@\2\2\u00e1\24\3\2\2\2\u00e2")
        buf.write("\u00e3\7@\2\2\u00e3\u00e4\7?\2\2\u00e4\26\3\2\2\2\u00e5")
        buf.write("\u00e6\7>\2\2\u00e6\30\3\2\2\2\u00e7\u00e8\7>\2\2\u00e8")
        buf.write("\u00e9\7?\2\2\u00e9\32\3\2\2\2\u00ea\u00eb\5? \2\u00eb")
        buf.write("\u00ec\5Y-\2\u00ec\u00ed\5E#\2\u00ed\34\3\2\2\2\u00ee")
        buf.write("\u00ef\5[.\2\u00ef\u00f0\5a\61\2\u00f0\36\3\2\2\2\u00f1")
        buf.write("\u00f2\5Y-\2\u00f2\u00f3\5[.\2\u00f3\u00f4\5e\63\2\u00f4")
        buf.write(' \3\2\2\2\u00f5\u00f6\7*\2\2\u00f6"\3\2\2\2\u00f7\u00f8')
        buf.write("\7+\2\2\u00f8$\3\2\2\2\u00f9\u00fa\t\2\2\2\u00fa&\3\2")
        buf.write("\2\2\u00fb\u00fd\7\17\2\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0101\7\f\2\2\u00ff")
        buf.write("\u0101\7\17\2\2\u0100\u00fc\3\2\2\2\u0100\u00ff\3\2\2")
        buf.write("\2\u0101\u0102\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103")
        buf.write("\3\2\2\2\u0103(\3\2\2\2\u0104\u0109\5\65\33\2\u0105\u0109")
        buf.write("\5\67\34\2\u0106\u0109\59\35\2\u0107\u0109\5=\37\2\u0108")
        buf.write("\u0104\3\2\2\2\u0108\u0105\3\2\2\2\u0108\u0106\3\2\2\2")
        buf.write("\u0108\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0108\3")
        buf.write("\2\2\2\u010a\u010b\3\2\2\2\u010b*\3\2\2\2\u010c\u0114")
        buf.write("\5\63\32\2\u010d\u0113\5\65\33\2\u010e\u0113\5\67\34\2")
        buf.write("\u010f\u0113\59\35\2\u0110\u0113\5=\37\2\u0111\u0113\5")
        buf.write("%\23\2\u0112\u010d\3\2\2\2\u0112\u010e\3\2\2\2\u0112\u010f")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0111\3\2\2\2\u0113")
        buf.write("\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2")
        buf.write("\u0115\u0117\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118\5")
        buf.write("\63\32\2\u0118,\3\2\2\2\u0119\u011b\5!\21\2\u011a\u0119")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d\3\2\2\2\u011c")
        buf.write("\u011e\5%\23\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u0121\3\2\2\2\u011f\u0122\5)\25\2\u0120\u0122\5")
        buf.write("+\26\2\u0121\u011f\3\2\2\2\u0121\u0120\3\2\2\2\u0122\u012b")
        buf.write("\3\2\2\2\u0123\u0125\5\61\31\2\u0124\u0126\5%\23\2\u0125")
        buf.write("\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0129\3\2\2\2")
        buf.write("\u0127\u012a\5)\25\2\u0128\u012a\5+\26\2\u0129\u0127\3")
        buf.write("\2\2\2\u0129\u0128\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u0123")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u0131\5%\23\2")
        buf.write("\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0133\3")
        buf.write("\2\2\2\u0132\u0134\5#\22\2\u0133\u0132\3\2\2\2\u0133\u0134")
        buf.write("\3\2\2\2\u0134.\3\2\2\2\u0135\u013a\5\65\33\2\u0136\u013a")
        buf.write("\5\67\34\2\u0137\u013a\59\35\2\u0138\u013a\5;\36\2\u0139")
        buf.write("\u0135\3\2\2\2\u0139\u0136\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u0139\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0139\3")
        buf.write("\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u0141")
        buf.write("\5!\21\2\u013e\u0142\5)\25\2\u013f\u0142\5+\26\2\u0140")
        buf.write("\u0142\5-\27\2\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0140\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\3")
        buf.write("\2\2\2\u0143\u0144\5#\22\2\u0144\60\3\2\2\2\u0145\u0146")
        buf.write("\7.\2\2\u0146\62\3\2\2\2\u0147\u0148\7$\2\2\u0148\64\3")
        buf.write("\2\2\2\u0149\u014a\t\3\2\2\u014a\66\3\2\2\2\u014b\u014c")
        buf.write("\t\4\2\2\u014c8\3\2\2\2\u014d\u014e\t\5\2\2\u014e:\3\2")
        buf.write("\2\2\u014f\u0150\7a\2\2\u0150<\3\2\2\2\u0151\u0155\7\60")
        buf.write("\2\2\u0152\u0155\5;\36\2\u0153\u0155\t\6\2\2\u0154\u0151")
        buf.write("\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0153\3\2\2\2\u0155")
        buf.write(">\3\2\2\2\u0156\u0157\t\7\2\2\u0157@\3\2\2\2\u0158\u0159")
        buf.write("\t\b\2\2\u0159B\3\2\2\2\u015a\u015b\t\t\2\2\u015bD\3\2")
        buf.write("\2\2\u015c\u015d\t\n\2\2\u015dF\3\2\2\2\u015e\u015f\t")
        buf.write("\13\2\2\u015fH\3\2\2\2\u0160\u0161\t\f\2\2\u0161J\3\2")
        buf.write("\2\2\u0162\u0163\t\r\2\2\u0163L\3\2\2\2\u0164\u0165\t")
        buf.write("\16\2\2\u0165N\3\2\2\2\u0166\u0167\t\17\2\2\u0167P\3\2")
        buf.write("\2\2\u0168\u0169\t\20\2\2\u0169R\3\2\2\2\u016a\u016b\t")
        buf.write("\21\2\2\u016bT\3\2\2\2\u016c\u016d\t\22\2\2\u016dV\3\2")
        buf.write("\2\2\u016e\u016f\t\23\2\2\u016fX\3\2\2\2\u0170\u0171\t")
        buf.write("\24\2\2\u0171Z\3\2\2\2\u0172\u0173\t\25\2\2\u0173\\\3")
        buf.write("\2\2\2\u0174\u0175\t\26\2\2\u0175^\3\2\2\2\u0176\u0177")
        buf.write("\t\27\2\2\u0177`\3\2\2\2\u0178\u0179\t\30\2\2\u0179b\3")
        buf.write("\2\2\2\u017a\u017b\t\31\2\2\u017bd\3\2\2\2\u017c\u017d")
        buf.write("\t\32\2\2\u017df\3\2\2\2\u017e\u017f\t\33\2\2\u017fh\3")
        buf.write("\2\2\2\u0180\u0181\t\34\2\2\u0181j\3\2\2\2\u0182\u0183")
        buf.write("\t\35\2\2\u0183l\3\2\2\2\u0184\u0185\t\36\2\2\u0185n\3")
        buf.write("\2\2\2\u0186\u0187\t\37\2\2\u0187p\3\2\2\2\u0188\u0189")
        buf.write("\t \2\2\u0189r\3\2\2\2\36\2~\u0094\u00a2\u00a5\u00bd\u00c2")
        buf.write("\u00c5\u00d4\u00fc\u0100\u0102\u0108\u010a\u0112\u0114")
        buf.write("\u011a\u011d\u0121\u0125\u0129\u012d\u0130\u0133\u0139")
        buf.write("\u013b\u0141\u0154\2")
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
