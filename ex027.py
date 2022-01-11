# faça um programa que leia o nome completo de uma pessoa, mostrando o primeioro eo ultimo nome

# ana maria de souza

# primeiro ana

# ultimo souza

nome = str(input('digite seu nome'))

frag = nome.split()

print('seu primeiro nome: {}'.format(frag[0]))
print('seu ultimo nome: {}'.format(frag[len(frag)-1]))# isso conta  a str e mostra o ultimo nome 
