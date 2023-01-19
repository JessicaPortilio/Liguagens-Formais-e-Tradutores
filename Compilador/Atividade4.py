# Etapa 4 - Trabalhando com expressões regulares complexas.
# Para definição de expressões regulares o ply usa como base o python re. 
# Mais detalhes, ver aqui: https://www.w3schools.com/python/python_regex.asp

# Com o uso de expressões regulares, podemos definir elementos mais complexos 
# a exemplo de um identificador. Em linguagens de programação um identificador costuma ser 
# definido como uma sequência de caracteres. 
# Assim, para darmos suporte a definição de identificadores em nosso exemplo no PLY, 
# poderíamos fazer a seguinte definição:

import ply.lex as lex # importando a biblioteca ply para o léxico
#Definindo Tokens e seus padroes
tokens = ("PLUS", "MINUS", "ID", 'NUMBER')
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_ID = r'[A-Za-z_][0-9]*'
t_NUMBER = r'[0-9]+'
def t_newline(t): #Adiciona a função t_newline
     r'\n+' 
     t.lexer.lineno += len(t.value) #Atualiza o contador de linha a 
                                    #depender da quantidade de \n
t_ignore  = t_ignore  = ' \t' # Remove \n daqui
#Criando analisador Lexico e realizando analise lexica
lexer = lex.lex()
lexer.input("a2 _  +_  - a4 - -+ +  +\n 3 23 -2")
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos) 




# Percebam que na definição introduzida, ID consiste em qualquer 
# letra minúscula ou maiúscula ocorrendo uma ou mais vezes.

#Questão 05 -  Modifique o exemplo anterior de forma que ID também contemple _. 
# Adicionalmente dê suporte a números, no entanto, o número não pode ser o primeiro caracter de um ID. 

#Questão 06 -  Crie o token NUMBER. NUMBER reconhece qualquer número inteiro.
