from antlr4.error.ErrorListener import ErrorListener


class DjangoNLFErrorListener(ErrorListener):
    def __init__(self):
        self._symbol = ""
        self._column = None
        self._msg = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self._symbol = offendingSymbol.text
        self._column = column
        self._msg = msg

    @property
    def error(self):
        if self._msg is not None:
            return f"SyntaxError at {self._symbol} on column {self._column}: {self._msg}"
        return None
