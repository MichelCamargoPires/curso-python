lista = ('lapis', 1.75,
         'boracha', 2,
         'caderno', 15.90,
         'estojo', 25,
         'tranferidor', 4.20,
         'compasso', 9.99,
         'mochila', 120.32,
         'caneta', 22.30,
         'livro', 34.90)

print('_' * 40)
print(f'{"LISTA DE PRECOS":^40}')
print('_' *40)

for pos in range(0, len(lista)): # contador para separar a lista e preços
    if pos %2 == 0: # para separar da lista os impar que no sao os preso 
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'RS{lista[pos]:>7.2f}') #para pegar preço que e resto da lita o valores pares 
print('_' * 40)
