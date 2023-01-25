# Faça um programa que leia os valores a, b e c 
# de uma equação de segundo grau e calcule as suas raízes.
# ax²+bx+c=0


a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))

import math
delta =b * b - 4 * a * c

raiz1 = (-b + (math.sqrt(delta))) / 2 * a

raiz2 = (-b - (math.sqrt(delta))) / 2 * a

print(f'Valor de x1: {raiz1}')
print(f'Valor de x2: {raiz2}')