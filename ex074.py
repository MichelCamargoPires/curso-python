from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
randint(1, 10),randint(1, 10))
print('os valores sortiados forao',end=' ')
for n in num: # tirar pontos 
  print(f'{n}',end=' ') # oganizar 
print(f'\no maior valor sortiado foi {max(num)}') # para ver qual o numero maior da tupla 
print(f'menor numero sorteado foi {min(num)}')
