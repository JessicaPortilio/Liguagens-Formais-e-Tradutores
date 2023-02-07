# -------------------------
# main.py
#----------------------

import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import tokens

def p_exp_soma(p):
    '''exp : exp SOMA exp1'''
    p[0] = p[1] + p[3]

def p_exp_subtracao(p):
    '''exp : exp SUBTRACAO exp1'''
    p[0] = p[1] - p[3]

def p_exp_exp1(p):
   '''exp : exp1'''
   p[0] = p[1]

def p_exp1_mult(p):
    '''exp1 : exp1 MULTIPLICACAO exp2'''
    p[0] = p[1] * p[3]

def p_exp1_div(p):
    '''exp1 : exp1 DIVISAO exp2'''
    p[0] = p[1] / p[3]

def p_exp1_exp2(p):
    '''exp1 : exp2'''
    p[0] = p[1]

def p_exp2_num(p):
    '''exp2 : NUMERO'''
    p[0] = p[1]

def p_error(p):
    print("Erro sintático na linha {}".format(p.lineno))

parser = yacc.yacc()              #Criação do analisador sintático
 
#result = parser.parse(debug=True) #Execução da análise sintática.

#print(result)

def main():
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)



main()
# Exercício 1: Execute o código anterior. A execução foi bem sucedida?
# Não, pois está dando erro no parser yacc.yacc() e o exp1 não está definido
#Exercício 2: Mapeie as demais regras da gramática citada. As regras que devem ser mapeadas estão em negrito. 

#exp → exp + exp1 | exp - exp1 | exp1 
#exp1 → exp1 * exp2 | exp1 / exp2 | exp2#
#exp2 → num 

#Exercício 3: Execute novamente o código com as mudanças. A execução foi bem sucedida?
# Sim agora funcionou!

# Exercício 4: Introduza a mudança de p_exp_soma(p) ao código. Execute novamente. A calculadora já está funcionando?

#Exercício 5: Construa a árvore de derivação que representa a expressão 3 + 4.

         # +
        # / \
        #3   4
#Exercício 6: Desenvolva código para todos os demais métodos  do sintático. Execute o código. E agora. A calculadora funciona?
#  O código acima implementa todas as regras da gramática necessárias para o funcionamento da calculadora.


