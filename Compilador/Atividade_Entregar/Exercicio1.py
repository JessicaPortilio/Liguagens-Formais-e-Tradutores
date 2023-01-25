# Implementar um analisador léxico que reconheça qualquer sequência de palavras.

# 1.Para uma sequência de palavras pertencentes a uma mesma linha, deve ser gerado o Token Linha.
# 2.Palavras que apresentam qualquer caractere diferente de letra, deve ser notificado erro léxico ao usuário
# 3.O analisador deve dar suporte a avaliação de indentações/dedentações.

import ply.lex as lex # importando a biblioteca ply para o léxico

#Definindo Tokens e seus padroes
tokens = ("ID", "BRANCO", "DEDENT", "INDENT")

t_ID = r'[a-zA-Z]+'  # Palavras que apresentam qualquer caractere

def t_error(t):
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t): #Adiciona a função t_newline
     r'\n+' 
     t.lexer.lineno += len(t.value) #Atualiza o contador de linha a 
                                    #depender da quantidade de \n

#Aqui tem uma função que pega os caracteres em branco
num_count =0
def t_BRANCO(t):
    r'\s' # OBS: professor na dica o professor falou pra aqui ser "\t", mas quando eu coloco ele não funciona =(
    global num_count
    num_count += 1 # ele vai contando os caracter em branco
    t.value = t.value
    print(f'Contador: {num_count}') 
    return t

# Obs professor mesmo com a dica que o professor meu deu não conseguir fazer funcionar


#t_ignore  = t_ignore  = ' \t' # Remove \n daqui


#Criando analisador Lexico e realizando analise lexica
lexer = lex.lex() 

lexer.input("""def permif len
def perm
65657
""") # Redefina o lexer e armazene uma nova string de entrada.
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos) 
