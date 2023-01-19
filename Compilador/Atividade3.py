import ply.lex as lex # importando a biblioteca ply para o léxico
#Definindo Tokens e seus padroes
tokens = ("PLUS", "MINUS", "TIMES", "DIVIDE", "LPAREN", "RPAREN")
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

t_ignore  = ' \t\n'

#Criando analisador Lexico e realizando analise lexica
lexer = lex.lex()
lexer.input("34 5+\n  - --+\n +  +")

for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos) 
#Etapa 3 - Reconhecendo a linha atual do Token.
def t_newline(t): #Adiciona a função t_newline
     r'\n+' 
     t.lexer.lineno += len(t.value) #Atualiza o contador de linha a 
                                    #depender da quantidade de \n

t_ignore  = t_ignore  = '\t' # Remove \n daqui


#Questão 03 - Adicionando novos Tokens.
#Utilizando o exemplo anterior, adicione os seguintes tokens *, /, (, ) 
# e dê a eles os seguintes nomes, respectivamente: TIMES, DIVIDE, LPAREN, RPAREN
