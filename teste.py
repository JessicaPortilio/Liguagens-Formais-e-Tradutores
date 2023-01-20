n= int(input('Informe um número: '))
cont=0 
soma=0    
aux = 0;
i=0

for i in range(n):
    if n % i == 0:
       aux += i;       
    if (aux == n):
      printf("NUMERO PERFEITO");
