# Para ajudar o TRE, você fez um programa que lê a idade de uma
# pessoa e informa a condição do eleitor conforme a tabela abaixo.

# Idade                             Condição

# Menor de 16 anos                  Não está apto a votar

# Entre 18 e 64 anos                Obrigatório

# Maior ou igual a 16 e menor que
# 18 OU maior ou igual a 65         Facultativo

idade = int(input('Informe a sua idade: '))

if(idade < 16):
    print('Não está apto a votar!')
elif(idade > 18 and idade <= 64):
    print('Obrigatório')
elif(idade >= 16 and idade < 18 or idade >= 65):
    print('Faultativo')