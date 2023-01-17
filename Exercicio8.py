#Faça um algoritmo que leia um número inteiro e tenha como saída 
# uma das seguintes opções:

# par e positivo
# par e negativo
# ímpar e positivo
# ímpar e negativo

numero = int(input('Informe um número: '))

if(numero % 2 == 0):
    if (numero > 0):
        print(f'O {numero} é par e positivo')
    else:
        print(f'O {numero} é par e negativo')
else:
    if (numero > 0):
        print(f'O {numero} é ímpar e positivo')
    else:
        print(f'O {numero} é ímpar e negativo')