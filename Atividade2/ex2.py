import ply.lex as lex

reserved = {'reset' : 'reset', 
            'set' : 'set', 
            'ping' :'ping'}

tokens = ['ID', 'NUM', 'NUMBER'] +  list(reserved.values())
t_NUMBER = r'[0-9]+'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        return None
    return t

def t_NUM(t):
    r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
    t.value = float(t.value)   
    return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
  print(f"Illegal character '{t.value[0]}'")
  t.lexer.skip(1)

lexer = lex.lex()

lex.input("reset id reset ola ping set id 22.4 set id 8 ping ola 9.7 set id 888 ping reset id")

for l in lexer:
  print(l)