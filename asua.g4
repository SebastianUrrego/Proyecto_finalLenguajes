grammar asua;

// Reglas principales
program      : importStatement* statement* EOF;
importStatement : 'import' ID ';';

statement    : assignment
             | logStatement
             | conditional
             | loop
             | graph
             | primeGraph
             | array
             | fileOperation
             | kMeansOperation  // Nueva regla para K-Means
             | regressionOperation
             | mlpOperation
             | functionDef  // Añadido aquí
             | functionCall // Añadido aquí
             | returnStatement
             ;

// Logs y asignaciones
logStatement : 'log' '(' expr ')' ';';
assignment: ID '=' (expr | matrixOperation);

// Expresiones
expr
    : '-' expr                                        // Negación unitaria
    | '+' expr
    | expr ('+' | '-' | '*' | '/' | '%') expr         // Operaciones aritméticas
    | expr ('>' | '<' | '>=' | '<=' | '==' | '!=') expr // Comparaciones
    | '(' expr ')'                                    // Paréntesis
    | ID '(' arguments? ')' 
    | 'sqrt' '(' expr ')'                             // Raíz cuadrada
    | 'pow' '(' expr ',' expr ')'                     // Potencia
    | 'sin' '(' expr ')'                              // Función seno
    | 'cos' '(' expr ')'                              // Función coseno
    | 'tan' '(' expr ')'                              // Función tangente
    | 'abs' '(' expr ')'                              // Valor absoluto
    | 'pi'                                            // Constante pi
    | 'e'                                             // Constante e
    | NUMBER                                          // Número
    | ID                                              // Identificador
    | STRING                                          // Cadena de texto
    | matrix                                          // Matrices
    | 'True'
    | 'False'
    ;
 
list : '[' (expr (',' expr)*)? ']' ';';

array : 'array' ID '[' NUMBER ']' '=' '[' (expr (',' expr)*)? ']' ';';

accessArray : ID '[' expr ']';
 
// Operaciones con matrices
matrix       : '[' row (',' row)* ']' ';';
row          : '[' expr (',' expr)* ']';

// Operaciones para matrices
matrixOperation: 'transpose' '(' ID ')'   // Transponer una matriz
               | 'inverse' '(' ID ')'     // Inversa de una matriz
               ;

// Estructuras de control
conditional : 'if' '(' expr ')' '{' statement* '}' ('else' '{' statement* '}')? ;
loop
    : 'for' '(' assignment ';' expr ';' assignment ')' '{' statement* '}'
    | 'while' '(' expr ')' '{' statement* '}'
    ;

// Parámetros y argumentos
parameters  : ID (',' ID)* ;
arguments   : expr (',' expr)* ;

// Funciones
functionDef : 'def' ID '(' parameters? ')' '{' statement* returnStatement? '}' ;
functionCall: ID '(' arguments? ')' ';';
returnStatement: 'return' expr ';';

graph : 'plot' '(' expr ',' expr ',' rangeStart ',' rangeEnd ',' step ')' ';';

primeGraph : 'plotPrimes' '(' rangeStart ',' rangeEnd ',' step ')' ';';

rangeStart : expr;  // Inicio del rango de x
rangeEnd   : expr;  // Fin del rango de x
step       : expr;  // Incremento entre puntos

// Operaciones de archivos
fileOperation: 'readFile' '(' STRING ')' ';' 
             | 'writeFile' '(' STRING ',' expr ')' ';';

// Gramática para kMeansOperation
kMeansOperation : 'kMeansOperation' '(' NUMBER ',' matrix ')' ';';

regressionOperation
    : 'linearRegression' ID '=' 'regress' '(' ID ',' ID ')' ';';
        
mlpOperation : 'mlp' '(' NUMBER ',' NUMBER ',' NUMBER ',' NUMBER ',' matrix ',' matrix ')' ';';
       
// Tokens básicos
NUMBER       : [0-9]+('.'[0-9]+)?;
ID           : [a-zA-Z_][a-zA-Z_0-9]*;
STRING       : '"' .*? '"';
WS           : [ \t\r\n]+ -> skip;
COMMENT      : '//' ~[\r\n]* -> skip;
