# Faça uma função que recebe uma lista como parâmetro e verifica se ela está ordenada crescentemente. 
# A função is_sorted vai retornar True se a lista estiver ordenada e False caso contrário.

def is_sorted_crescente(lista):
    # para saber se a lista é crescente
    inicio = 0 # vamos usar essa variável para entrar no if enquanto ele for menor que o tamanho da lista
    count= 1 # aqui é um contador para ele só retornar se é verdadeiro quando ele percorrer toda a lista
    tamanho = len(lista) # aqui estamos pegando o tamanho da lista
    for i in range(tamanho): # para i a quantidade do tamanho da lista
        inicio = i+1 # inicio =  i + 1 ex: inicio =  0 + 1
        if inicio < tamanho: # Se inicio for menor que o tamanho
            if lista[i] > lista[inicio]: # Se lista na posição i for maior que a lista na posição inicio
                return False # Retorna Falso (Lembrando que queremos ver se a lista é crescente então se lista[i] for maior que a próxima posição da lista que é lista[inicio] então não está crescente a lista)
            else:
                count+= 1 # cada vez que ele entrar aqui ele vai somando mais um
                if count == tamanho: # Se a quantidade de vez que ele entrou aqui for igual o tamanho da lista
                    return True # Então a lista é crescente

# Para decrescente basta fazer ao contrário.
def is_sorted_decrescente(lista2):
    count= 1
    inicio2 = 0
    tamanho2 = len(lista2)
    for i in range(tamanho2):
        inicio2 = i+1
        if inicio2 < tamanho2:
            if lista2[i] > lista2[inicio2]:
                #print(f'1 {lista2[i]}')
                count += 1
                if count == tamanho2:
                    return True
            else:
                return False
lista = [1,2,3,4,5]
lista2 = [5,4,1,3,2,1]
crescente = is_sorted_crescente(lista)

descrescente = is_sorted_decrescente(lista2)

print(f'É crescente? {crescente}')
print(f'É descrescente?: {descrescente}')