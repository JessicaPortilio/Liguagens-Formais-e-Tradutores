# 3.Para saber se está ganhando bem, a analista de redes Fernanda,
# deseja saber quantos salários-mínimos ela ganha. Para isso ela
# precisa fazer um programa que leia o valor do salário-mínimo
# atual e o seu salário. Ao final, o programa deverá mostrar
# quantos salários-mínimos ganha Fernanda

salario_minimo = float(input('Informe o valor do salário mínimo: '))
valor = float(input('Informe seu salário: '))

qtd_salario_minimo = valor / salario_minimo

print(f'Recebe {int(qtd_salario_minimo)} salários mínimos')