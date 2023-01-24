# O programa consiste um fazer um jogo que
# permita que o computador possa adivinhar
# um número de 1 a 100 que o usuário
# imaginar

# O computador vai gerar um número e
# perguntar ao usuário se acertou ou se ele
# pensou em uma valor maior ou menor.
# Baseado nisso, o próximo valor gerado pelo
# computador deve ser ajustado para gerar
# outro número nessa nova faixa

import random

valor = random.randint(1, 100)
print(f'Você pensou em {valor}')
resposta = input('Eu aceitei? ')
maior_menor = input('Você pensou em um número maior ou menor? ')

s = True

while (s):
    if resposta == 'sim':
        print('Parabéns você aceitou!')
        s = False
    else:
        if maior_menor == 'menor':
            valor = random.randint(1, valor)
            print(f'Você pensou em {valor}')
            resposta = input('Eu aceitei? ')
            maior_menor = input('Você pensou em um número maior ou menor? ')
            if resposta == 'sim':
                print('Parabéns você aceitou!')
                s = False
        elif maior_menor == 'maior':
            valor = random.randint(valor, 100)
            print(f'Você pensou em {valor}')
            resposta = input('Eu aceitei? ')
            maior_menor = input('Você pensou em um número maior ou menor? ')
            if resposta == 'sim':
                print('Parabéns você aceitou!')
                s = False