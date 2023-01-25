# Etapa 5 - Trabalhando com funções
# O PLY também permite usar função como forma de definir padrões 
# para o reconhecimento de lexemas válidos na linguagem. 
# Ao invés de atribuirmos a expressão regular em uma variável t_NOME_DO_TOKEN, 
# definimos uma função t_NOME_DO_TOKEN, onde na linha seguinte aparece uma string 
# contendo uma expressão regular. Nas demais linhas é possível adicionarmos comportamento 
# que afetará a forma como é feita a análise léxica desse lexema. 
# A seguir apresentamos um exemplo para reconhecimento de caracteres inteiros 
# através de uma função.
import ply.lex as lex # importando a biblioteca ply para o léxico
#Definindo Tokens e seus padroes
tokens = ("PLUS", "MINUS", "ID", 'NUMBER')
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_ID = r'[A-Za-z_][0-9]*'

# esta regra corresponde a números e converte a string em um inteiro
def t_NUMBER(t):
    r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
    t.value = float(t.value)    
    return t
    
# Defina uma regra para que possamos rastrear números de linha 
def t_newline(t): #Adiciona a função t_newline
     r'\n+' 
     t.lexer.lineno += len(t.value) #Atualiza o contador de linha a 
                                    #depender da quantidade de \n
t_ignore  = t_ignore  = ' \t' # Remove \n daqui
#Criando analisador Lexico e realizando analise lexica
lexer = lex.lex()
lexer.input("2.5 a2 _  +_ 5.0 - a4 - +\n ")
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos) 



# Questão 07 - Modifique a função anterior, de forma que ela reconheça números de ponto flutuante.
