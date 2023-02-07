import ply.lex as lex

tokens = ['NUM', 'NUMBER']
t_NUMBER = r'[0-9]+'
# Define a regra para reconhecer números inteiros e floats
def t_NUM(t):
    r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
    t.value = float(t.value)   
    return t

# Ignora espaços e tabs
t_ignore = ' \t'

# Constroi o analisador léxico
lexer = lex.lex()

# Testa o analisador léxico com alguns exemplos de números
test_data = '123 456.7 89.010 1.23456'

lexer.input(test_data)

for l in lexer:
    print(l.value)
        