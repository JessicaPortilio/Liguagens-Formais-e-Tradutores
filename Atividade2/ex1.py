import ply.lex as lex
### Considere a seguinte linguagem de programação:
### Stm → Stm ; Stm | id := Exp | print
### Exp → id | num | Exp Binop Exp | ( Stm , Exp )
### ExpList → Exp , ExpList | Exp
### Binop → + | − | × | /

### Desenvolva o analisador léxico em PLY, fazendo uso das seguintes regras:
### num = somente números binários, octais e hexadecimais na forma 0b101010010,
### 0c71342 e 0x1ff10302, respectivamente.
### id = Começa com o símbolo @ seguido por letras ou números, com no máximo
### 10 caracteres.
### Os demais tokens são os terminais da linguagem.###

# "Stm" é uma instrução que pode ser uma sequência de outras instruções separadas por ";", ou uma atribuição "id := Exp", ou uma instrução "print".

# "Exp" é uma expressão que pode ser um identificador "id", um número "num", uma expressão binária composta por outras expressões "Exp Binop Exp", ou uma combinação de instruções e uma expressão "(Stm, Exp)".

# "ExpList" é uma lista de expressões separadas por ",".

# "Binop" é um operador binário que pode ser "+", "-", "×" ou "/".
tokens = [
   'ID',
   'NUM',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'SEMI',
   'ASSIGN',
   'PRINT'
]

def t_ID(t):
   r'@[a-zA-Z0-9]{1,10}'
   return t

def t_NUM(t):
   r'0b[0-1]+|0c[0-7]+|0x[0-9a-fA-F]+'
   return t

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_ASSIGN = r':='
t_PRINT = r'print'

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

lexer = lex.lex()
lex.input("""@comeca123 0b101010010;
0c71342 := 0x1ff10302 print """)

for l in lexer:
  print(l.value)
