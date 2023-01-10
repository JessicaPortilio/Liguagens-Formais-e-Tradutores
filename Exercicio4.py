# 4. Para iluminar espaços residenciais, as normas pedem que se use
# 18W para cada m2. Faça um programa que receba as duas
# dimensões de um cômodo (em metros) e calcule qual a
# potência de iluminação que deverá ser utilizada

largura = int(input('Informe a largura do cômodo que deseja iluminar: '))
comprimento = int(input('Informe o comprimento do mesmo cômodo que deseja iluminar: '))

metro_quadrado = largura * comprimento
watt = metro_quadrado * 18
print(f'Cômodo {metro_quadrado}m2: Será preciso potência {watt}W para a iluminação')
