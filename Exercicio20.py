# Faça um programa que leia os valores a, b e c 
# de uma equação de segundo grau e calcule as suas raízes.
#ax²+bx+c=0

a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))

import math

print(math.sqrt(a + b + c))

