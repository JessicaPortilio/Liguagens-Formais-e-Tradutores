# Faça uma função lambda que permita saber se um número é par ou impar. 
# A função deve retornar um boolean (True para par e False para ímpar)


par_impar = lambda x : True if (x % 2 == 0) else False

numero = int(input('Informe um número: '))
print(par_impar(numero))