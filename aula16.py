from itertools import count


lanche = ('hamburguer', 'suco', 'pizza', 'pudin')

print(lanche[1]) # imdice um 
print(lanche[-2]) # conta de tras para frente
print(lanche[1:3]) # vai do elemento 1 ao 3
print(lanche[2:]) # vai do 2 ate o fim
print(lanche[-2:]) # vai do 2 ate o fim
print(lanche) # mostra a tupla inteira 

        # tublas sao imutaveis 

for comida in lanche:
    print(f'eu vo comer {comida}')
print('comi pra caramba ')

print(len(lanche)) # mostra a quantidade de itens dento da tupla

for cont in range(0, len(lanche)):
    print(lanche[cont]) # vai mostrar os itens em ordem 

for pos, comida in enumerate(lanche): # dar nome e numerar 
    print(f' eu vou comer {comida} na posicao {pos}')

print(sorted(lanche)) # vai organizar de A a Z 

        # outra tupla

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # junta as tupla
print(c)

print(len(c))
print(c.count(5)) # quantas vezes esta aparecendo o numero 5 
print(c.index(8))
print(c.index(5, 1)) # achar o numero apartir da posicao 

pessoa = ('michel', 21, 'm', 72)
print(pessoa)
