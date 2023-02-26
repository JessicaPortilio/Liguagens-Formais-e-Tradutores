import ply.lex as lex
import ply.yacc as yacc


def criptografar(palavra):
    palavra = palavra.upper()
    resultado = ''
    for letra in palavra:
        if letra.isalpha(): # Verifique se todos os caracteres do texto são letras:
            resultado += chr(ord('A') + (ord(letra) - ord('A') + 1) % 26) # A ord()função retorna o número que representa o código unicode de um caractere especificado.
        else:
            resultado += letra
    return resultado

tokens = ('CRIPTO', 'TEXTO')

t_ignore  = ' \t\n'

def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}'")
    t.lexer.skip(1)

def t_CRIPTO(t):
    r'<cripto>[A-Za-z]+<\/cripto>'
    t.value = f"<cripto>{criptografar(t.value[8:-9])}</cripto>"
    return t

def t_TEXTO(t):
    r'[A-Za-z]+'
    return t

lexer = lex.lex()

entrada = "ola mundo <cripto>SEGREDO</cripto> tudo bem"
lexer.input(entrada)
saida = ""

while True:
    tok = lexer.token()
    if not tok:
        break
    saida += tok.value

print(f"Entrada: {entrada}")
print(f"Saida: {saida}")
