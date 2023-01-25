#Crie uma função que recebe como parâmetro o número do mês e ela vai retornar o nome do mês 
# e a quantidade de dias. Não leve em consideração anos bissextos 

def mes(valor):
    if valor >=1 and valor <=12: 
        if valor == 4 or valor == 6 or valor==9 or valor == 11:
            if valor == 4:
                return 'abril de 30 dias'
            if valor == 6:
                return 'junho de 30 dias'
            if valor == 9:
                return 'setembro de 30 dias'
            if valor == 11:
                return 'novembro de 30 dias'
        elif valor == 1 or valor == 3 or valor == 5 or valor == 7 or valor == 8 or valor == 10 or valor == 12:
            if valor == 1:
                return 'janeiro de 31 dias'
            if valor == 3:
                return 'março de 31 dias'
            if valor == 5:
                return 'maior de 31 dias'
            if valor == 7:
                return 'julho de 31 dias'
            if valor == 8:
                return 'agosto de 31 dias'
            if valor == 10:
                return 'outubro de 31 dias'
            if valor == 12:
                return 'dezembro de 31 dias'   
        else:
            return 'fevereiro de 28 dias' 
    else:
        return 'Informe um número de 1 à 12!'


print(mes(1))