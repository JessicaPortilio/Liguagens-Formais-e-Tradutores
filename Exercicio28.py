# Faça uma função lambda que permita calcular o valor do imposto de um produto passado como parâmetro. 
# O imposto é 30% do valor do produto.

imposto = lambda produto: produto * 30 / 100

valor = float(input('Informe o valor do produto: '))

resultado = imposto(valor)

print(f'O valor do imposto pago pelo produto será de R${resultado}')
