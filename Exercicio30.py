# Faça uma função que retorne uma lista com os N primeiros termos da série de Fibonacci
# A série de Fibonacci é:
# 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci():
    n , n1 = 1, 1
    count = 0
    lista = []
    while count < 10:
        lista.append(n)
    
        soma =n + n1
        n = n1
        n1 = soma
        count += 1
    for i in range(len(lista)):
       return lista


lista = fibonacci()

for i in lista:
    print(i)