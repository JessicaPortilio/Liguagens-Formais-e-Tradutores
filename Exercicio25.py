# Crie uma função que converta polegadas em centímetros, sabendo que 1 polegada equivale a 2,54 centímetros. 
# O parâmetro é passado em polegadas e a função retorna o seu equivalente em centímetros 

def polegadas_em_centimetros(valor):
    return valor * 2.54

polegada = float(input('Informe a polegada: '))

print(polegadas_em_centimetros(polegada))