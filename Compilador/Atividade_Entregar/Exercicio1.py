# Implementar um analisador léxico que reconheça qualquer sequência de palavras.

# 1.Para uma sequência de palavras pertencentes a uma mesma linha, deve ser gerado o Token Linha.
# 2.Palavras que apresentam qualquer caractere diferente de letra, deve ser notificado erro léxico ao usuário
# 3.O analisador deve dar suporte a avaliação de indentações/dedentações.

import ply.lex as lex # importando a biblioteca ply para o léxico
#Definindo Tokens e seus padroes
tokens = ("ID",)

t_ID = r'[a-zA-Z]+'

def t_error(t):
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t): #Adiciona a função t_newline
     r'\n+' 
     t.lexer.lineno += len(t.value) #Atualiza o contador de linha a 
                                    #depender da quantidade de \n
t_ignore  = t_ignore  = ' \t' # Remove \n daqui

#Criando analisador Lexico e realizando analise lexica
lexer = lex.lex() 
lexer.input("Vamos testar \n 345 continuar") # Redefina o lexer e armazene uma nova string de entrada.
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos) 


