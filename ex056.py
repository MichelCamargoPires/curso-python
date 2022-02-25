#desenvolva um programa que leia o nome , idade , sex de 4 pessoas  e no final mostre 

# a media de idade do grupo 

# qual eo nome do homem mais velho 

#qyabtas mulhers tem menos de 20 anos 
somaidade = 0
mediaidade = 0
for p in range(1, 5):
    print('------ {}° PESSOA --------'.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]')).strip()
    somaidade += idade

mediaidade = somaidade / 4
print(mediaidade)

# terminar
    
