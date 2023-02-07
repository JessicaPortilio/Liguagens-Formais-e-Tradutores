import sys
from ply import lex

# Tokens
tokens = ['WORD']

def t_WORD(t):
    r'\b[a-zA-Z]+\b'
    return t

def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = "Ola tudo bem"

# Set input
lexer.input(data)

# Search for word
word = ["Ola", "tudo", "vamos", "bem"]
count = 0
while True:
    tok = lexer.token()
    if not tok:
        break
    for i in word:
        if tok.value == i:
            count += 1

# Print count
print(count) 
