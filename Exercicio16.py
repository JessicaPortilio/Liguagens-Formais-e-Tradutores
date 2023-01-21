# Na sua última viagem para o Vale do Silício, na California, 
# você estava sentindo muito frio, mas quando você olhava para o termômetro ele marcada temperaturas bem altas. 
# Depois você ficou sabendo que lá a temperatura é medida em graus Fahrenheit. 
# Para te auxiliar um pouco com a escala que você está acostumado, 
# faça um programa que imprima a tabela de equivalência de graus Fahrenheit para centígrados. 
# Os limites são de 40 a 80 graus Fahrenheit com intervalo de 1 grau.  
# A fórmula para conversão é: C = 5 * (F -32) / 9
# Onde F são os graus em Fahrenheit.

minimo = 40
maximo = 81

for F in range(minimo, maximo, 1):
    c = 5 * (F - 32) / 9
    print(f'Temperatura em %.0f °F para %.0f °C' %(F, c))
