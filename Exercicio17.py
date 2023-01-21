# Seu colega da universidade que trabalha em uma loja que tira xerox 
# pediu para você fazer um programa que leia o valor de uma fotocópia 
# e imprima uma tabela de 1 até 200, para que ele possa saber exatamente 
# quando deve cobrar do cliente. 
# Na figura podemos ver um exemplo dessa tabela para o valor da xerox: R$ 0,03 

valor = 0
for i in range(1, 201):
    valor += 0.03
    print(i, '%.2f' %valor, sep='    ')
