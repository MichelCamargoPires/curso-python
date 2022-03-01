#desenvolva um programa que leia o nome , idade , sex de 4 pessoas  e no final mostre 

# a media de idade do grupo 

# qual eo nome do homem mais velho 

#qyabtas mulhers tem menos de 20 anos 
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('------ {}° PESSOA --------'.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1 
mediaidade = somaidade / 4
print('a media de idade do grupo e de {} anos '.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {} anos'.format(maioridadehomem, nomevelho))    
print('ao toto sao {} mulher com menos de 20 anos'.format(totmulher20))
