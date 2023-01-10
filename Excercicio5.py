# Ana Júlia quer passar alguns dias de férias na Espanha. Ela
# calculou que 100 euros é suficiente para alimentação e passeios
# em cada um dos dias. Ela precisa saber quantos reais irá gastar
# nesses dias. Para isso ela fez um algoritmo que vai ler a cotação
# atual do euro e a quantidade de dias que vai passar. O
# programa deverá mostrar a quantidade de reais necessários
# para a viagem.

# Declarando as libs do Python:
import requests
import json

# Acessando a API:
requisicao = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')

# Desserialização do retorno da API:
cotacao = requisicao.json()

# Conhecendo a estrutura de dados:

#print(cotacao)

# Manipulando as informações:
#print('#### Cotação do Euro ####')

#print('Moeda: ' + cotacao['EUR']['name'])

#print('Data: ' + cotacao['EUR']['create_date'])

#print('Valor atual: R$' + cotacao['EUR']['bid'])

valor_atual_euro = cotacao['EUR']['bid']


Valor_em_real_100_euro = 100 * float(valor_atual_euro)
dias = int(input('Quantos dias de viaje? '))
print(f'Você vai precisar de R$: {Valor_em_real_100_euro * dias} para passar {dias} na Europa!')