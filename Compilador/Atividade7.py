# Etapa 7 - Trabalhando com estados
# A depender da linguagem, pode ser necessário ter diferentes estados para análise léxica. 
# Por padrão, a análise léxica PLY apresenta apenas o estado denominado INITIAL. 

# Porém, o desenvolvedor pode querer que a ocorrência de um determinado token acione 
# um tipo diferente de análise léxica. PLY suporta um recurso que permite colocar o analisador léxico 
# em uma série de estados diferentes. Cada estado pode ter seus próprios tokens e regras de análise. 

# Para definir um novo estado de análise, primeiro ele deve ser declarado. 
# Isso é feito incluindo uma declaração de "estados" em seu arquivo lex. Por exemplo:


#states = (
#    ('foo','exclusive'),
#    ('bar','inclusive'),
#)

# Esta declaração declara dois estados, 'foo' e 'bar'. Estados podem ser 'exclusive' ou 'inclusive'. 
# Num estado exclusive o analisador léxico retornará tokens e aplicará regras definidas especificamente 
# para esse estado. 

# Num estado inclusivo, tokens e regras do estado são adicionados ao conjunto padrão de regras do estado INITIAL. Assim, o analisador léxico retornará tanto os tokens definidos por padrão quanto aqueles definidos para o estado inclusivo.

#Após declaração dos estados, tokens e regras são declaradas incluindo o nome do estado na declaração do token/regra. Por exemplo:

#foo_NUMBER = r'\d+'                      # Reconhece 'NUMBER' no estado 'foo'        
#def foo_newline(t):                              #Reconhece quebra de linha no estado foo.
#  r'\n'
#  t.lexer.lineno += 1

# Por último, definimos o padrão que levará a transição de estado. A análise léxica começa utilizando as regras associadas ao estado INITIAL. No exemplo a seguir, mudamos para o estado foo quando encontramos a tag <foo>, mudamos para o estado INITIAL quando encontramos </foo>.

#def begin_foo():
   #r'<foo>' 
  #t.lexer.begin('foo')  

#def foo_end_foo():
  # r'</foo>' 
  #t.lexer.begin('INITIAL')  

#A seguir, apresentamos o código completo para realização de testes:

import ply.lex as lex

tokens = ('NUMBER', 'WORD')
states = (('foo', 'exclusive'), )

t_WORD = r'[a-zA-Z]+'
t_ignore = r' \t'
t_foo_ignore = r' \t'
t_foo_NUMBER = r'\d+'  # Reconhece 'NUMBER' no estado 'foo'


def t_foo_newline(t):  #Reconhece quebra de linha no estado foo.
  r'\n'
  t.lexer.lineno += 1


def t_error(t):
  print('error in INITIAL state, %s' % t.value[0])
  t.lexer.skip(1)


def t_foo_error(t):
  print('error in foo state, %s' % t.value[0])
  t.lexer.skip(1)


def t_begin_foo(t):
  r'<foo>'
  t.lexer.begin('foo')


def t_foo_end_foo(t):
  r'\</foo\>'
  t.lexer.begin('INITIAL')


lexer = lex.lex()
lex.input("lft  muito legal 3322 <foo> 34423 amer </foo>")
for l in lexer:
  print(l.value)


#Questão 08 - Execute o código. A entrada fornecida apresenta algum erro léxico? Ajuste a entrada de forma que a mesma seja uma entrada válida léxicamente.

#Questão 09 - Adicione o reconhecimento do token + no estado foo.

#Questão 10 - Adicione o estado bar. 
# O estado bar é inclusive. Nele, devem ser reconhecidos palavras e números. 
# O estado bar se torna ativo quando é identificada a ocorrência de <bar>. Quando é detectado <\bar> o analisador deve voltar para o estado INITIAL. 

