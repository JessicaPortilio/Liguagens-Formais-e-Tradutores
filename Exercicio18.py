# Escreva um programa que determine se um número digitado pelo usuário é primo ou não. 
# Um número é chamado de primo quando é divisível somente por um e por ele mesmo. 

num = int(input('Informe um número primo: '))

if num % 2 != 0:
    print(f'O número digitado {num} é primo!')
else:
    print(f'O número digitado {num} não é primo!')
