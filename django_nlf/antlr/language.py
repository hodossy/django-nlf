from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from .error_listener import DjangoNLFErrorListener
from .generated import DjangoNLFLexer, DjangoNLFParser
from .listener import DjangoNLFListener


class DjangoNLFLanguage:
    lexer_class = DjangoNLFLexer
    parser_class = DjangoNLFParser
    listener_class = DjangoNLFListener
    error_listener_class = DjangoNLFErrorListener

    def parse(self, filter_expr: str):
        if not filter_expr:
            return []

        _input = InputStream(filter_expr)
        lexer = self.get_lexer(_input)
        stream = CommonTokenStream(lexer)
        parser = self.get_parser(stream)

        error_listener = self.get_error_listener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        tree = parser.filter_exp()

        listener = self.get_listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        return listener.output

    def get_error_listener(self) -> DjangoNLFErrorListener:
        return self.error_listener_class()

    def get_listener(self) -> DjangoNLFListener:
        return self.listener_class()

    def get_lexer(self, _input) -> DjangoNLFLexer:
        return self.lexer_class(_input)

    def get_parser(self, token_stream) -> DjangoNLFParser:
        return self.parser_class(token_stream)
