# Faça uma função is_equals que receba duas listas como parâmetro e retorne True caso sejam iguais e Falso caso contrário.
# As listas são iguais se possuem exatamente os mesmos elementos e na mesma ordem


def is_equals(lista, lista2):
    if lista ==lista2:
        return True
    else:
        return False


lista = [1,2,3,4]
lista2 = [1,2,3,4]

print(is_equals(lista, lista2))