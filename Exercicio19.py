# Para calcular o número de vacinas que uma cidade deverá receber, 
# o prefeito teve que fazer um cadastro onde cada morador informou a sua idade. 
# O grupo prioritário é composto de idosos acima de 60 anos e devem tomar duas doses da vacina. 
# Crianças abaixo de cinco anos não devem tomar vacina. 
# O restante da população é o grupo normal e tomará apenas uma dose da vacina. 
# Faça um programa que leia a idade de um conjunto de pessoas e indique quantas pessoas são do grupo prioritário, 
# quantas são do grupo normal, quantas são crianças e quantas doses são necessárias para vacinar 100% da população.

população = int(input('Informe a quantidade da população: '))
total_idosos = 0
total_criancas = 0
total_pessoas = 0
vacina = 0
for i in range(população):
    idade = int(input('Informe sua idade: '))
    if idade > 60:
        total_idosos += 1
        
    elif idade < 5 :
        total_criancas += 1
        
    else:
        total_pessoas += 1
vacina = (total_idosos * 2) + total_pessoas
print(f'A quantidade de Idosos que devem tomar duas doses da vacina são: {total_idosos}!')
print(f'A quantidade de Crianças que não deve tomar vacina são: {total_criancas}!')
print(f'A quantidade do restante da população do grupo normal que devem tomar uma dose da vacina são: {total_pessoas}!')
print(f'Quantidade de doses que são necessários para vacinar a população são: {vacina}')

