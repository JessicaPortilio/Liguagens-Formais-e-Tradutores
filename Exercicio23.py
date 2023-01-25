# Faça uma função que receba um valor inteiro como parâmetro que representa tempo em segundos 
# e devolva uma string com o formato: XXh XXmin XXseg.
#Vejamos os seguintes exemplos:
# 65 = 1min 5seg
# 3601 = 1h 1seg
# 120 = 2min
# 9603 = 2h 40min 3seg

def converter_tempo(segundo):
    hora = segundo // 3600 # transformando segundo em hora
    segundo %= 3600 #pegando o resto da hora
    minuto = segundo // 60 # transformando em minuto
    segundo %= 60 # e pegando o resto do minuto
    
    return f'%.0fH:%.0fmin:%.0fseg'%(hora, minuto, segundo)
 

tempo = int(input('Informe o tempo: '))
print(converter_tempo(tempo))
