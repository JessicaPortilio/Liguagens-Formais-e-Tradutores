# A série de Fibonacci é formada pela sequência:

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

# Escreva um programa que gere a série de Fibonacci até o enésimo termo

n , n1 = 1, 1
count = 0

while count < 10:
    print(n)
    
    soma =n + n1
    n = n1
    n1 = soma
    count += 1