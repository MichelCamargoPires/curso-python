#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com nome "santo"

cidade = (input('digite  a cidade: '))

fraguimento = cidade.split()
primeiro = fraguimento[0]


if primeiro == 'santo':
    print('tem')
else:
    print('nao tem ')
    
    # fui liso
