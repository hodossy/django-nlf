.PHONY: language
language:
	@echo Generating language lexer and parser...
	@antlr4 -Dlanguage=Python3 -o generated DjangoNLF.g4
	@echo Done.

.DEFAULT: language
