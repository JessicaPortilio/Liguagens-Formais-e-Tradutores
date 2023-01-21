# A Kryptonita, o material radioativo que torna o Superman mais fraco,
# perde metade de sua massa a cada 50 segundos. 
# Dada a massa inicial, em gramas, deve-se calcular o tempo necessário 
# para que essa massa se torne menor que 0,5 grama, 
# que é quando não afeta mais os poderes do Superman. 
# Faça um programa para escrever a massa inicial, 
# a massa final e quanto tempo o Superman ficará fraco, 
# sendo que o tempo deve ser calculado em horas, minutos e segundos.

massa_Inicial = float(input('Informe a massa inicial em gramas: '))

massa_Final = massa_Inicial

tempo_Total = 0

while massa_Final >= 0.5:
    massa_Final = massa_Final / 2
    tempo_Total = tempo_Total + 50;

print(f'Massa inicial: {massa_Inicial} gramas.')
print(f'Massa final: {massa_Final} gramas.')

print(f'Tempo total: {tempo_Total} segundos')
tempo_Hora = (tempo_Total / 3600)
tempo_Minuto = (tempo_Total % 3600)  / 60
tempo_Segundo = (tempo_Total % 3600) % 60
print(f'Tempo que o Superman ficará fraco será {tempo_Hora}hr {tempo_Minuto}mn e {tempo_Segundo}sgs.')
print('O tempo que o Superman ficará fraco será %.0f Hora e %.2f' %tempo_Hora,tempo_Minuto)
