# Gere uma lista de números 50 randômicos entre 1 e 100 
# e a partir dessa lista filtre apenas aqueles que são múltiplos de 3


import random
lista = []
for i in range(50):
    numero = random.randint(1, 100)
    lista.append(numero)

lista2 = [x if x % 3 == 0 else '' for x in lista]

print(lista2)

tamanho = len(lista2)
count = 0
while count < tamanho:
    if '' in lista2:
        lista2.remove('')
    count += 1
print(lista2)