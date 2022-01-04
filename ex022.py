#crie um programa que leia o nome completo de uma pessoa e mostre

#o nome com todas as letras maiuscula 

#o nome com todas em minusculas 

#quantas letras ao todos sem espacos

# quantas letras tem o primeiro nome 

nome = input('digite seu nome: ')
print('seu nome em maiusculo ',nome.upper())
print('seu nome em minusculo ',nome.lower())
print('seu nome tem: ',len(nome),'letras')
print('seu nome sem espaços ',len(nome.split()))
nomeEnLinta = nome.split()
print('seu primeiro nome ',nomeEnLinta[0])
primeiro = nomeEnLinta[0]
print('seu primeiro nome tem ',len(primeiro),'letras')
