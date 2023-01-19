#Objetivos da Atividade:
#Apresentar como utilizar a ferramenta PLY para realização da etapa de análise léxica.

#Etapa 1 -  Análise Léxica no PLY.
#O PLY pode gerar analisadores léxicos a partir de expressões regulares. 

#Para compreensão de como utilizar o PLY na análise léxica, comecemos pelo seguinte trecho de código:

import ply.lex as lex # importando a biblioteca ply para o léxico
#Definindo Tokens e seus padroes
tokens = ("PLUS", "MINUS")
t_PLUS    = r'\+'
t_MINUS   = r'-'

#t_ignore  = ' \t'
#Criando analisador Lexico e realizando analise lexica
lexer = lex.lex()
lexer.input("+---+++")
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos) 

#Questão 01 - O que aconteceu após a execução do código?
#Ele printa na tela 
# O tipo de token especificando
# O valor do token especifico
# lineno O número de linha em que o token aparece na origem do modelo.
# Lexpos mostra a coluna que ele está
# lex.py não executa nenhum tipo de rastreamento automático de colunas. 
# No entanto, ele registra posicionalmente informações relacionadas a cada token no atributo lexpos. 
# Usando isso, geralmente é possível calcular informações de coluna como uma etapa separada. Por exemplo, 
# basta contar para trás até chegar a uma nova linha.
