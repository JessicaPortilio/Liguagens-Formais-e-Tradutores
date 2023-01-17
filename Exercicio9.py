# O BancoDigital oferece empréstimos que são 
# baseados no rendimento do cliente.
# Contudo, o valor máximo da prestação 
# não pode ser maior que 15% da renda.
# Faça um programa que permita digitar o salário bruto, 
# o valor total do empréstimo e o número de parcelas. 
# O algoritmo deverá informar se o empréstimo pode ser concedido ou não.

salario_bruto = float(input('Informe seu salário bruto: '))

total = salario_bruto * 0.85
renda = salario_bruto - total

emprestimo = float(input('Informe o valor do empréstimo: '))
qtd_parcelas = int(input('Informe para quantas vezes: '))

parcelado = emprestimo / qtd_parcelas

if (parcelado <= renda):
    print(f'Seu empréstimo de R${emprestimo} foi aprovado e ficou {qtd_parcelas}x de R${parcelado}')
else:
    print(f'Seu empréstimo de R${emprestimo} não foi aprovado, pois a sua parcela de R${parcelado} é maior que 15% da sua renda {renda}')