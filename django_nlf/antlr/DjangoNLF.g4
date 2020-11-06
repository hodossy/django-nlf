grammar DjangoNLF;

/*
 * Parser rules
 */
operator            : WHITESPACE? (AND | OR | NOT) WHITESPACE? ;
lookup              : WHITESPACE? (EQUALS | NEQUALS | LIKE | NLIKE | IN | NIN | GT | GTE | LT | LTE) WHITESPACE? ;
expression          : TEXT lookup (TEXT | QUOTED_TEXT) ;
filter_expr         : expression (operator expression)* ;
nested_filter_expr  : \( filter_expr \) ;

/*
 * Lexer rules
 */

// Field lookups
EQUALS              : I S | E Q U A L S | '=' ;
NEQUALS             : I S ' ' N O T | N O T ' ' E Q U A L S | '!=' ;
LIKE                : I S ' ' L I K E | '~' ;
NLIKE               : I S ' ' N O T ' ' L I K E | '!~' ;
IN                  : I N ;
NIN                 : N O T ' ' I N ;
GT                  : '>' ;
GTE                 : '>=' ;
LT                  : '<' ;
LTE                 : '<=' ;

// Operators
AND                 : A N D ;
OR                  : O R ;
NOT                 : N O T ;

WHITESPACE          : (' ' | '\t') ;
NEWLINE             : ('\r'? '\n' | '\r')+ ;
TEXT                : (LOWERCASE | UPPERCASE | NUMBER | SYMBOL)+ ;
QUOTED_TEXT         : QUOTE (LOWERCASE | UPPERCASE | NUMBER | SYMBOL | WHITESPACE)+ QUOTE;

fragment QUOTE      : '"' ;
fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;
fragment NUMBER     : [0-9] ;
fragment SYMBOL     : '.' | '_' ;
fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];
