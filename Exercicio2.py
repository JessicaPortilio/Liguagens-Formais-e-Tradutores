# 2.Para melhorar sua performance na corrida, o treinador do
# corredor João Bolt aconselhou que ele perdesse alguns quilos.
# Com uma rigorosa dieta, Bolt conseguiu baixar 6% do seu peso a
# cada mês, durante três meses. Faça um programa que leia o
# peso inicial de Bolt e o peso após os três meses

Peso = float(input('Informe seu peso: '))
Peso_atual = Peso * 0.94 * 0.94 * 0.94
print(f'Seu peso atual é {Peso_atual}')