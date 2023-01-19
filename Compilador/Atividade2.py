# Etapa 2 - Reconhecendo caracteres inúteis.
# Em linguagens de programação, são vários os elementos que são 
# inúteis para as demais etapas de análise (sintático e semântico). 
# Um elemento importante, porém inútil para demais etapas são os espaços em branco, 
# quebras de linha ou tabulações. 
# Eles são importantes pois servem para delimitar lexemas de uma linguagem de programação, 
# no entanto, esses delimitadores não geram tokens e assim, não o utilizamos nas demais etapas de análise.  
# Para o reconhecermos e eliminarmos no ply, usamos a variável t_ignore. 
# O exemplo anterior com essa característica fica:

import ply.lex as lex # importando a biblioteca ply para o léxico
#Definindo Tokens e seus padroes
tokens = ("PLUS", "MINUS")
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_ignore  = ' \t\n'
#Criando analisador Lexico e realizando analise lexica
lexer = lex.lex()
lexer.input("+\n  - --+\n +  +")
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos) 


#Questão 02 - O que mudou comparado ao código anterior? Os valores informados estão corretos?
#Sim, estão correto. O que mudou é que agora ele ignora o espaço em branco, ele ignora o pulo de linha.
