grammar MathOp;

program
    : subprog (NEWLINE subprog?)+ ;

subprog
    : types WHITESPACE FUNCNAME args (NEWLINE|WHITESPACE?) block;

args
    : '(' atom? (',' WHITESPACE? atom)* ')'
    ;

if_block
    : IF WHITESPACE? '(' expression ')' WHITESPACE? block
    ;

elif_block
    : ELIF WHITESPACE? '(' expression ')' WHITESPACE? block
    ;

else_block
    : ELSE WHITESPACE? block
    ;

block
    : BLOCK_BEGIN NEWLINE (TAB* command | WHITESPACE* NEWLINE)* NEWLINE TAB* BLOCK_END
    ;

command
    : expression               #printexpression
    | subprog                  #declfunc
    | if_block ((NEWLINE TAB | WHITESPACE) elif_block)* ((NEWLINE TAB | WHITESPACE) else_block)?                #ifelseBlock
    | RETURN WHITESPACE expression #return
    ;

expression
    : '(' WHITESPACE? expression WHITESPACE? ')'                #exprExpression
    | atom                        #atomExpression
    | expression WHITESPACE? op=POW WHITESPACE? expression          #powExpression
    | expression WHITESPACE? op=( MUL | DIV | MOD ) WHITESPACE? expression         #multExpression
    | expression WHITESPACE? op=( PLUS | MINUS ) WHITESPACE? expression               #addExpression
    | expression WHITESPACE? op=( BIGGEREQ | BIGGER | LESSEQ | LESS ) WHITESPACE? expression #compExpression
    | expression WHITESPACE? op=( EQUAL | NOTEQUAL ) WHITESPACE? expression             #eqExpression
    | ID WHITESPACE? op=ASSIGN WHITESPACE? ( types '(' expression ')' | expression)   #assign
    | FUNCNAME '(' atom? (',' WHITESPACE? atom)* ')'     #funcCall
    ;

atom
    :   number    #Num
    |   ID      #Id
    ;

number
    :   FLOAT   #Float
    |   INT     #Int
    ;

types
    :   TYPE_INT
    |   TYPE_FLOAT
    ;

ASSIGN    : '=' ;
EQUAL     : '==' ;
NOTEQUAL  : '!=' ;
LESS      : '<';
LESSEQ    : '<=';
BIGGER    : '>';
BIGGEREQ  : '>=';
PLUS      : '+' ;
MINUS     : '-';
MUL       : '*';
DIV       : '/';
POW       : '^';
MOD       : '%';

BLOCK_BEGIN:'{' ;
BLOCK_END:  '}';
TAB:        '    ';

TYPE_INT:   'int' ;
TYPE_FLOAT: 'float' ;

IF:         'if' ;
ELIF:       'elif' ;
ELSE:       'else' ;
RETURN:     'return' ;
NEWLINE:    '\r'? '\n' ;
ID:         [a-zA-Z]+ ;
FUNCNAME:   ('_' [a-zA-Z] [a-zA-Z0-9]+)+ ;
INT:        ([0]|[1-9][0-9]*) ;
FLOAT:      INT '.' INT ;
WHITESPACE: ' ' ;
