# Escreva um programa que leia um valor inicial A 
# e imprima a sequência de valores do cálculo do fatorial de A! e o seu resultado.
# Por exemplo, imagine que o número lido seja 5 e teríamos o seguinte padrão de resposta:
# 5! = 5 x 4 x 3 x 2 x 1 = 120


n = int(input('Informe um número: '))

fatorial = 1
nome = []
print(n, '! = ', sep='', end='')
while n > 0:
    fatorial = fatorial * n
    print(n , end='')
    n-=1
    if n >= 1:
        print(' * ', end='')
    
print(' =', fatorial, end="")