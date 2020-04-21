grammar MathOp;

program
    : subprog (NEWLINE subprog?)+ ;

subprog
    : type WHITESPACE FUNCNAME args (NEWLINE|WHITESPACE?) block;

args
    : '(' atom? (',' WHITESPACE? atom)* ')'
    ;

block
    : BLOCK_BEGIN NEWLINE (TAB* command | WHITESPACE* NEWLINE)* NEWLINE TAB* BLOCK_END
    ;

command
    : expression               #printexpression
    | if ((NEWLINE TAB | WHITESPACE) elif)* ((NEWLINE TAB | WHITESPACE) else)?                #ifelseBlock
    | 'return' WHITESPACE expression #return
    ;

if
    : 'if' WHITESPACE expression WHITESPACE? block
    ;

elif
    : 'else' WHITESPACE if
    ;

else
    : 'else' WHITESPACE? block
    ;

expression
    : '(' expression ')'                #exprExpression
    | atom                        #atomExpression
    | expression WHITESPACE? op=( '^' | '$' ) WHITESPACE? expression         #exponentExpression
    | expression WHITESPACE? op=( '*' | '/' | '%' ) WHITESPACE? expression         #multExpression
    | expression WHITESPACE? op=( '+' | '-' ) WHITESPACE? expression               #addExpression
    | expression WHITESPACE? op=( '>=' | '<=' | '>' | '<' ) WHITESPACE? expression #compExpression
    | expression WHITESPACE? op=( '==' | '!=' ) WHITESPACE? expression             #eqExpression
    | ID WHITESPACE? '=' WHITESPACE? ('(' type ')')? expression   #assign
    | FUNCNAME args     #funcCall
    ;

atom
    :   number    #Num
    |   ID      #Id
    ;

number
    :   FLOAT   #Float
    |   INT     #Int
    ;

type
    :   TYPE_INT
    |   TYPE_FLOAT
    ;

BLOCK_BEGIN:'{' ;
BLOCK_END:  '}';
TAB:        '    ';
TYPE_INT:   'int' ;
TYPE_FLOAT: 'float' ;
NEWLINE:    '\r'? '\n' ;
ID:         [a-zA-Z]+ ;
FUNCNAME:   ('_' [a-zA-Z] [a-zA-Z0-9]+)+ ;
INT:        ([0]|[1-9][0-9]*) ;
FLOAT:      INT ',' INT ;
WHITESPACE: ' ' ;

