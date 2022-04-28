//1912966
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//KEY WORDS
BREAK: 'B' R E A K;
FOREACH: 'F' O R E A C H;
INT: 'I' N T;
NULLS: 'N' U L L;
CONSTRUCTOR: 'C' O N S T R U C T O R;
CONTINUE: 'C' O N T I N U E;
TRUES: 'T' R U E;
FLOAT: 'F' L O A T;
CLASS: 'C' L A S S;
DESTRUCTOR: 'D' E S T R U C T O R;
IF: 'I' F;
FALSES: 'F' A L S E;
BOOLEAN: 'B' O O L E A N;
VAL: 'V' A L;
NEW: 'N' E W;
ELSEIF: 'E' L S E I F;
ARRAY: 'A' R R A Y;
STRING: 'S' T R I N G;
VAR: 'V' A R;
BY: 'B' Y;
ELSE: 'E' L S E;
IN: 'I' N;
RETURN: 'R' E T U R N;
SELF: 'S' E L F;


program: list_class EOF;

list_class: class_decl list_class
          | class_decl
          ;
          
class_decl: CLASS ID LP class_block RP
	  | CLASS ID COLON ID LP class_block RP; 
class_block: list_class_mem
           |
           ;

list_class_mem: class_mem_decl list_class_mem
              | class_mem_decl
              ;
              
class_mem_decl: class_attr_decl SEMI
              | class_method_decl
              ;

class_attr_decl: (VAL|VAR) (attr1 | attr2)
               ;
               
attr1: list_id COLON mptype;

attr2: mpid COMMA attr2 COMMA expr
     | mpid COLON mptype ASS expr 
     ;
     
list_id: mpid COMMA list_id
       | mpid
       ;
              
list_expr: expr COMMA list_expr
         | expr
         ;             
    
literal: LIT_INT
   | LIT_FLOAT
   | lit_boolean
   | LIT_STRING
   | lit_indexed_arr
   | lit_mul_arr
   ;
   


mptype: primitive_type
      | array_type
      | class_type
      ;

class_type: ID;
      
primitive_type: BOOLEAN
              | INT
              | FLOAT
              | STRING
              ;
            
array_type: ARRAY LS array_characteristic RS;

array_characteristic: array_element_type COMMA array_size;

array_element_type: primitive_type
                  | array_type
                  ;

array_size: expr;

class_method_decl: static_method 
                 | instance_method
                 | constructor_method
                 | destructor_method
                 ;

static_method: ID_STATIC LB list_para RB stat_block;

instance_method: ID LB list_para RB stat_block;

constructor_method: CONSTRUCTOR LB list_para RB stat_block;

destructor_method: DESTRUCTOR LB RB stat_block;

list_para: notnull_list_para
          |
          ;

notnull_list_para: para SEMI notnull_list_para
                  | para
                  ;
                  
para: list_id_ins COLON mptype; 

//STATEMENTS

stat: stat_var_con
    | stat_assign
    | stat_if
    | stat_foreach
    | stat_break
    | stat_continue
    | stat_return
    | stat_method_ins
    | stat_method_sta
    | stat_block
    ;

stat_var_con: (VAR|VAL) (stat_var_con1|stat_var_con2) SEMI;

stat_var_con1: list_id_ins COLON mptype;

stat_var_con2: ID COMMA stat_var_con2 COMMA expr
     | ID COLON mptype ASS expr 
     ;


list_id_ins: ID COMMA list_id_ins
           | ID
           ;
       
stat_assign: stat_assign_lhs ASS expr SEMI;

stat_assign_lhs: mpid
               | expr7
               ;
               
    
stat_if: part_if list_else;

part_if: IF LB expr RB stat_block;

list_else: elseif list_else
         | part_else
         |
         ;
           
elseif: ELSEIF LB expr RB stat_block;

part_else: ELSE stat_block;

//Foreach/IN statement

stat_foreach: FOREACH LB mpid IN for_expr1 DDOT for_expr2 by_expr RB stat_block;

for_expr1: expr;

for_expr2: expr;

by_expr: BY expr
          | 
          ;
          

//break statement

stat_break: BREAK SEMI;

//Continue statement

stat_continue: CONTINUE SEMI;

//Return statement

stat_return: RETURN expr? SEMI;

        
//Method invocation statement

stat_method_sta: ID DCOLON ID_STATIC LB list_expr? RB SEMI;

stat_method_ins: expr8 DOT ID LB list_expr? RB SEMI;
            
//Block statement

stat_block: LP block_body RP;
 
block_body: list_stat
         |
         ;
         
list_stat: stat list_stat
         | stat
         ;
 


//EXPRESSION

//string
expr: expr1 op_string expr1
    | expr1
    ;

//relational
expr1: expr2 op_rel expr2
     | expr2
     ;
     
//Logical2        
expr2: expr2 op_log2 expr3
     | expr3
     ;

//Adding
expr3: expr3 op_add expr4
     | expr4
     ;
     
//Multiplying     
expr4: expr4 op_mul expr5
     | expr5
     ;
     
//Logical1     
expr5: op_log1 expr5
     | expr6
     ;
     
//Sign
expr6: MINUS expr6
     | expr7
     ;
     
//Index 
expr7: expr9
     | expr8 LS expr RS
     ;

expr8: expr8 LS expr RS
     | expr9
     ;
     
//Instance access
expr9: expr9 DOT ID
     | expr9 DOT ID LB list_expr? RB
     | expr10
     ;

//Static access   
expr10: ID DCOLON ID_STATIC
     | ID DCOLON ID_STATIC LB list_expr? RB 
     | expr11
     ;
     
//NEW     
expr11: NEW ID LB list_expr? RB
      | factor
      ;
      
factor: mpid
      | lit
      | LB expr RB
      | SELF
      | NULLS
      ;

lit: LIT_INT
   | LIT_STRING
   | LIT_FLOAT
   | lit_boolean
   | lit_indexed_arr
   | lit_mul_arr
   ;
   

op_string: EQUA_DOT
         | PLUS_DOT
         ;
         
op_rel: EQUA
      | DIF
      | LESS
      | MOREE
      | LESS_EQUA
      | MORE_EQUA
      ;

op_log2: AND
      | OR
      ;
      
op_add: PLUS
      | MINUS
      ;
      
op_mul: MUL
      | DIV
      | PERCENT
      ;
      
op_log1: EXCL;

op_obj: NEW;


//id parser
mpid: ID
  | ID_STATIC
  ;

//Block comment
BLOCK_COMM: ('##' .*? '##'| '##' .*? EOF) -> skip;

//ID
ID: [A-Za-z_][A-Za-z_0-9]*;

//ID-Static
ID_STATIC: '$'[A-Za-z_0-9]+;


//Alphabet
fragment A: 'a'|'A';
fragment B: 'b'|'B';
fragment C: 'c'|'C';
fragment D: 'd'|'D';
fragment E: 'e'|'E';
fragment F: 'f'|'F';
fragment G: 'g'|'G';
fragment H: 'h'|'H';
fragment I: 'i'|'I';
fragment J: 'j'|'J';
fragment K: 'k'|'K';
fragment L: 'l'|'L';
fragment M: 'm'|'M';
fragment N: 'n'|'N';
fragment O: 'o'|'O';
fragment P: 'p'|'P';
fragment Q: 'q'|'Q';
fragment R: 'r'|'R';
fragment S: 's'|'S';
fragment T: 't'|'T';
fragment U: 'u'|'U';
fragment V: 'v'|'V';
fragment W: 'w'|'W';
fragment X: 'x'|'X';
fragment Y: 'y'|'Y';
fragment Z: 'z'|'Z';


//OPERATORS

PLUS: '+';
EXCL: '!';
DIF: '!=';
EQUA_DOT: '==.';
MINUS: '-';
AND: '&&';
MOREE: '>';
PLUS_DOT: '+.';
MUL: '*';
OR: '||';
LESS_EQUA: '<=';
DOT: '.';
DIV: '/';
EQUA: '==';
LESS: '<';
PERCENT: '%';
ASS: '=';
MORE_EQUA: '>=';

//SEPERATORS
LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

COMMA: ',';

LS: '[';

RS: ']';

COLON: ':';

DCOLON: '::';

DOLLAR: '$';

DDOT:'..';
//LITERALS

//integer literal
LIT_INT: (LIT_INT_OCT|LIT_INT_HEX|LIT_INT_DEC|LIT_INT_BIN)
    {
        x = str(self.text)
        self.text = x.replace("_","")
    }
;
fragment LIT_INT_DEC: ('0'..'9'|'_')+; 
fragment LIT_INT_HEX: '0' X ('0'..'9'|'A'..'F'|'_')+;
fragment LIT_INT_OCT: '0' ('0'..'7'|'_')+;
fragment LIT_INT_BIN: '0' B ('0'|'1'|'_')+;


//float literal
LIT_FLOAT: (LIT_FLOAT_INT LIT_FLOAT_DEC LIT_FLOAT_EXP?
	 | LIT_FLOAT_INT LIT_FLOAT_EXP
	 | LIT_FLOAT_DEC LIT_FLOAT_EXP
	 )
    {
        x = str(self.text)
        self.text = x.replace("_","")
    }
    ;    
fragment LIT_FLOAT_INT: LIT_INT_DEC;
fragment LIT_FLOAT_DEC: '.' ('0'..'9')*;
fragment LIT_FLOAT_EXP: E ('-'|'+')? ('0'..'9')+;

//boolean literal
lit_boolean: TRUES|FALSES;


//string literal
LIT_STRING:'"' STR_CHAR* '"'
    {
        y = str(self.text)
        self.text=y[1:-1]
    }
    ;

fragment STR_CHAR: ~[\b\t\n\f\r\\"]
		 | ESC_SEQ
		 | '\'"'
		 ;
fragment ESC_SEQ: '\\' [btnfr\\'];

fragment ESC_ILLEGAL: '\\' ~[btnfr\\'];
//indexed array
lit_indexed_arr: ARRAY LB list_expr RB;

             
//multi-dimensional arrays

lit_mul_arr: ARRAY LB mul_arr_elements RB;

mul_arr_elements: mul_arr_element COMMA mul_arr_elements
                | mul_arr_element
                ;
               
mul_arr_element: lit_mul_arr
               | lit_indexed_arr
               ;
              



WS: [ \t\r\n\b\f]+ -> skip; // skip spaces, tabs, newlines

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
    {
        x = str(self.text)
        raise IllegalEscape(x[1:])
    }
    ;
UNCLOSE_STRING: '"' STR_CHAR* (EOF|[\b\t\n\f\r\\])
    {
        x = str(self.text)
        p = ['\b', '\t', '\n', '\f', '\r', '\\']
        if x[-1] in p:
            raise UncloseString(x[1:-1])
        else:
            raise UncloseString(x[1:])
    }
    ;
ERROR_CHAR: .
    {
        raise ErrorToken(self.text)
    }
    ;
    