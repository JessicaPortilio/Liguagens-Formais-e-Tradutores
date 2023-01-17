# Na loja de material de construção de Seu Marcos ele aplicou 
# a seguinte lógica de lucro sobre os produtos. 
# Se o valor da compra do produto for menor que R$ 10,00 
# o lucro deve ser de 30%, caso contrário o lucro deve ser de 20%. 
# Faça um programa que leia o valor de um produto e calcule o
# preço final e o valor do lucro obtido com a venda dele.

valor = float(input('Valor da compra: '))

if (valor < 10):
    lucro = valor * 0.70
    resultado = valor - lucro
    print(f'O valor do produto foi {valor} e o lucro foi de {resultado}')
else:
    lucro = valor * 0.80
    resultado = valor - lucro
    print(f'O valor do produto foi {valor} e o lucro foi de R$:{resultado}')