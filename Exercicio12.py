# Faça um programa que leia um conjunto de valores inteiros e positivos. Imprima
# o maior e o menor valor. Considere que:

# Para finalizar a leitura dos valores será digitado o valor zero;

# Para valores negativos deve ser dada uma mensagem de erro;

# Valores negativos e o próprio valor de parada não devem ser computados.

n = 1

while(n > 0):

    valor = int(input('Informe o primeiro número: ')) 
    if valor == 0:
        break;
    elif valor < 0:
        print('Somente é permitido valores positivos e inteiros!')
        valor = int(input('Informe o primeiro número: ')) 

    valor2 = int(input('Informe o segundo número: '))
    if valor2 == 0:
        break;
    elif valor2 < 0:
        print('Somente é permitido valores positivos e inteiros!')
        valor2 = int(input('Informe o primeiro número: ')) 
        
    if valor > valor2:
        print(f'O maior valor {valor} e o menor valor {valor2}')
    else:
        print(f'O maior valor {valor2} e o menor valor {valor}')
