import ply.lex as lex

# Lista de tokens reconhecidos pelo lexer
tokens = [
    'NUMERO_REAL',
    'NUMERO_ROMANO',
    'NUMERO_TELEFONE'
]

# Expressões regulares para reconhecimento de números reais
def t_NUMERO_REAL(t):
    r'-?\d+(\.\d+)?((E|e)[+-]?\d+)?'
    t.value = float(t.value)
    return t

# Expressões regulares para reconhecimento de números romanos
def t_NUMERO_ROMANO(t):
    r'(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'
    roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    prev = 0
    for c in t.value:
        curr = roman_map[c]
        total += curr
        if curr > prev:
            total -= 2 * prev
        prev = curr
    if total > 1999:
        t.value = 0
    else:
        t.value = total
    return t

# Expressões regulares para reconhecimento de números de telefone
def t_NUMERO_TELEFONE(t):
    r'(\+\d{2})?\s?(\(\d{2}\))?\s?(\d{2})?\s?\d{4,5}[.-]\d{4}'
    t.value = t.value.replace(' ', '')
    t.value = t.value.replace('(', '')
    t.value = t.value.replace(')', '')
    t.value = t.value.replace('.', '')
    t.value = t.value.replace('-', '')
    return t

# Regras de ignorar espaços em branco e outros caracteres indesejados
t_ignore = ' \t\r'

# Função que lida com erros (para fins de debug)
def t_error(t):
    print("Erro: caractere inválido '%s'" % t.value[0])
    t.lexer.skip(1)

# Constrói o lexer
lexer = lex.lex()

# Testa o lexer com uma entrada de exemplo
lexer.input("1.0")
while True:
    tok = lexer.token()
    print(tok)
