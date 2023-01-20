# Dado um número n inteiro e positivo, dizemos que ele é perfeito se for igual à
# soma de seus divisores positivos diferentes de n. Construa um programa que leia
# um número do usuário e verifica se ele é perfeito ou não.

# O número 6 é perfeito, pois os divisores são: 1, 2 e 3, que somados tem seis
# como resultado.

n = int(input('Informe um número: '))
somando= 0
count = 1
total = 0
while count < 10:
    if n % count == 0:
        somando = somando + count
        print(somando, count)
        total = count
    count += 1
result =somando - total
if (result == total):
    print(f'O número "{n}" perfeito!')
else:
    print(f'O número "{n}" não é perfeito!')