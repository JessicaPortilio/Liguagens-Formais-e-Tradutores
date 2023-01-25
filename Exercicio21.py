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
# o computador pode adivinhar um número de 1 a 100
numero_menor = 1
numero_maior = 100

# Aqui vou pegar a informação se o número pensado foi maior ou menor do que o computador escolheu
maior_menor = ''
# aqui eu pego um número de 1 a 100 aleatóriamente
valor = random.randint(numero_menor, numero_maior)

print(f'Você pensou em {valor}')

resposta = input('Eu aceitei? ')
s = True
while s:
    if resposta == 'não':
        maior_menor = input('Você pensou em um número maior ou menor? ')
        if maior_menor == 'maior':
            numero_menor = valor + 1
            valor = random.randint(numero_menor, numero_maior)
            print(f'Você pensou em {valor}')
            resposta = input('Eu aceitei? ')
            if resposta == 'sim':
                print(f'Você aceitou!')
                s = False
        else:
            numero_maior = valor - 1
            valor = random.randint(numero_menor, numero_maior)
            print(f'Você pensou em {valor}')
            resposta = input('Eu aceitei? ')
            if resposta == 'sim':
                print(f'Você aceitou!')
                s = False
    else:
        print(f'Você aceitou!')
        s = False
