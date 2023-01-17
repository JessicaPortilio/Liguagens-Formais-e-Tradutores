# Na área de segurança da informação, 
# a senha é um ponto importante e normalmente existem algumas regras 
# que devem ser seguidas para a construção de senhas mais seguras. 
# Faça um algoritmo que leia uma senha e indique se a ela
# poderá ser usada ou não. As regras para esta senha são as seguintes:

# Deve ter exatamente quatro dígitos

# Não pode repetir o mesmo número em as quatro posições. 
# Ex: 2222 não pode!

senha = input('Informe a sua senha: ')
qtd_numero = len(senha)
senha = list(senha)
if senha[0] == senha[1] and senha[0] == senha[2] and senha[0] == senha[3]:
    print('Não pode repetir o mesmo digito em as quatro posições.')
else:
    print('Senha válida')
