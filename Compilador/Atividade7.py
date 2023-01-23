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

# Num estado inclusivo, tokens e regras do estado são adicionados ao conjunto padrão de regras do estado INITIAL. 
# Assim, o analisador léxico retornará tanto os tokens definidos por padrão quanto aqueles definidos para o 
# estado inclusivo.

#Após declaração dos estados, tokens e regras são declaradas incluindo o nome do estado na declaração do token/regra. 
# Por exemplo:

#foo_NUMBER = r'\d+'                      # Reconhece 'NUMBER' no estado 'foo'        
#def foo_newline(t):                              #Reconhece quebra de linha no estado foo.
#  r'\n'
#  t.lexer.lineno += 1

# Por último, definimos o padrão que levará a transição de estado. A análise léxica começa utilizando 
# as regras associadas ao estado INITIAL. 
# No exemplo a seguir, mudamos para o estado foo quando encontramos a tag <foo>, 
# mudamos para o estado INITIAL quando encontramos </foo>.

#def begin_foo():
   #r'<foo>' 
  #t.lexer.begin('foo')  

#def foo_end_foo():
  # r'</foo>' 
  #t.lexer.begin('INITIAL')  

#A seguir, apresentamos o código completo para realização de testes:

import ply.lex as lex

tokens = ('NUMBER', 'WORD', 'ID', 'MAIS')

# Para definir um novo estado de lexing, primeiro ele deve ser declarado. 
# Isso é feito incluindo uma declaração de "estados" em seu arquivo lex. 
states = (
    ('foo','exclusive'),
    ('bar','inclusive'),
)


# Depois que um estado é declarado, 
# os tokens e as regras são declarados incluindo o nome do estado na declaração do token/regra.
t_WORD = r'[a-zA-Z]+'
t_bar_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ignore = r' \t'
t_foo_MAIS = r'\+'
t_foo_ignore = r' \t'
t_foo_NUMBER = r'\d+'  # Reconhece 'NUMBER' no estado 'foo'

t_NUMBER = r' \d+' 

def t_foo_newline(t):  #Reconhece quebra de linha no estado foo.
  r'\n'
  t.lexer.lineno += 1


def t_error(t):
  print('error in INITIAL state, %s' % t.value[0])
  t.lexer.skip(1)


def t_foo_error(t):
  print('error in foo state, %s' % t.value[0])
  t.lexer.skip(1)

def t_bar_error(t):
  print('error in bar state, %s' % t.value[0])
  t.lexer.skip(1)


def t_begin_foo(t):
  r'<foo>'
  t.lexer.begin('foo')

def t_begin_bar(t):
  r'<bar>'
  t.lexer.begin('bar')

# Para sair de um estado, você usa begin() para voltar ao estado inicial. Por exemplo:
def t_foo_end_foo(t):
  r'\</foo\>'
  t.lexer.begin('INITIAL')

def t_bar_end_bar(t):
  r'\</bar\>'
  t.lexer.begin('INITIAL')


lexer = lex.lex()
lex.input("<foo> + 3322 </foo> lft muito legal 3322  <bar> lft muito legal 3322 </bar>")
for l in lexer:
  print(l.value)


#Questão 08 - Execute o código. A entrada fornecida apresenta algum erro léxico? Sim apresenta!
# Ajuste a entrada de forma que a mesma seja uma entrada válida léxicamente.

#Questão 09 - Adicione o reconhecimento do token + no estado foo.

#Questão 10 - Adicione o estado bar. 
# O estado bar é inclusive. Nele, devem ser reconhecidos palavras e números. 
# O estado bar se torna ativo quando é identificada a ocorrência de <bar>. 
# Quando é detectado <\bar> o analisador deve voltar para o estado INITIAL. 

