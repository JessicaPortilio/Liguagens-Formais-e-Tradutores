# 1. A faculdade NerdsPrimeiro utiliza média ponderada ao invés de
# média aritmética. São três notas por período, sendo que as
# duas primeiras têm peso 3 (três) e a terceira tem peso 4
# (quatro). Faça um programa que leia três de notas de um aluno
# e calcule sua média ponderada

nota1 = float(input('Informe a primeira nota do aluno: '))  
nota2 = float(input('Informe a segunda nota do aluno: '))
nota3 = float(input('Informe a terceira nota do aluno: '))

media = ((nota1 * 3) + (nota2 * 3) + (nota3 * 4)) / (3 + 3 + 4)
if (media >= 5):
    print(f'A média do aluno foi {media}, foi aprovado!')
else:
    print(f'A média do aluno foi {media}, foi reprovado!')