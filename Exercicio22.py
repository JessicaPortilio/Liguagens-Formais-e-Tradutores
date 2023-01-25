# Faça uma função que troque o conteúdo de duas variáveis entre si 

def troca_conteudo(a, b):
    trocar = a
    a = b
    b = trocar
    return a, b

print(troca_conteudo(3, 6))