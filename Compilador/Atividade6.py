# Etapa 6 - WARNING: No t_error rule is defined
# t_error é uma função do PLY que sinaliza qual comportamento o analisador léxico 
# deve ter quando aparece algum lexema inválido. 
# Um exemplo de definção de t_error é dado a seguir:
import ply.lex as lex # importando a biblioteca ply para o léxico
#Definindo Tokens e seus padroes
tokens = ("PLUS", "MINUS", "ID", 'NUMBER')
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_ID = r'[A-Za-z_][0-9]*'

def t_NUMBER(t):
    r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
    t.value = float(t.value)    
    return t

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t): #Adiciona a função t_newline
     r'\n+' 
     t.lexer.lineno += len(t.value) #Atualiza o contador de linha a 
                                    #depender da quantidade de \n
t_ignore  = t_ignore  = ' \t' # Remove \n daqui

#Criando analisador Lexico e realizando analise lexica
lexer = lex.lex()
lexer.input("2.5 a2 _  +_  - a4 - +\n ")
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos) 

