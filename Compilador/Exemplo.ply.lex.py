#O exemplo a seguir mostra como lex.py é usado para #escrever um tokenizador simples.

 # ------------------------------------------------------------
 # calclex.py
 #
 # tokenizer for a simple expression evaluator for
 # numbers and +,-,*,/
 # ------------------------------------------------------------
import ply.lex as lex
 
# List of token names.   This is always required
 
tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES',
'DIVIDE', 'EQUALS', 'LPAREN', 'RPAREN']
 
# Regular expression rules for simple tokens
t_PLUS = r'\+' # Esses nomes devem corresponder
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
 
# essa regra corresponde a números e converte a cadeia de caracteres em um inteiro Python.
def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)    
  return t
 
# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()
 
lex.input("x= 434 + 543")

for token in lexer:
  print(token.type, token.value)
