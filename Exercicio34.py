# Gere uma lista de números 30 randômicos entre 1 e 100 e a partir 
# dessa lista substitua todos os números pares por zero

import random
lista = []
for i in range(30):
    numero = random.randint(1, 100)
    lista.append(numero)

lista2 = [0 if x % 2 == 0 else x for x in lista]

print(lista2)