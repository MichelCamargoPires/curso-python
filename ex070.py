'''crie um progtama que leia varios nprodutos o programa devera
perguntar se o usuario vai continuar no final .mostra:

a) qual eo totsl gasto na compra 

b) quanto produto cust amais de 1000

c)quais eo nome do produto mais barato'''
total = mil = cont = menor = 0
barato = ''
while True:
    preco = float(input('qual o valor do produto:'))
    produto = str(input('qual o nome do produto: '))
    cont += 1
    total += preco
    if preco > 1000:
        mil += 1 
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'NS':
        resp = str(input('vc quer continuar [N/S]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'total: {total}')
print(f'passo de mil: {mil}')
print(f'o produto mais barato foi {barato} eo valor dele foi {menor}')
