# Faça uma função que receba uma lista e 
# exiba os elementos da última metade na frente dos elementos da primeira metade


def metade(lista):
    tamanho = len(lista)
    metade = tamanho // 2
    return lista[metade:]


lista = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14]


print(metade(lista))








