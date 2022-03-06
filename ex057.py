'''faça um programa que leia o sexo de uma pessoa . mas so aceite os valores 
M ou f coso esteja errado peça para digitar novamente'''

nome = 0
while nome != 'f' and nome !='m':
    nome = str(input('qual seu genero [m/f]: '))
    if nome != 'f' and nome != 'm':
        print('vc escreveu errado!!')
print('seu genero e {}'.format(nome))
