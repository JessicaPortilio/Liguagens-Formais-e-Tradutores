# Faça uma função que retorne o número primo mais próximo de 1000 
import random
def primo():
    valor = random.randint(990,1000)
    if valor % 2 != 0:
        return valor
    else:
        return primo()
        

print(primo())
        
