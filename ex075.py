num = (int(input('digite um numero: ')),
       int(input('digite um numero: ')),
       int(input('digite um numero: ')),
       int(input('digite um numero: ')))
print('o numenro que vc digito forao',end=' ')
for n in num:
   print(f'{n}',end=' ')
print(f'\no numro 9 parace {num.count(9)} vezes')
if 3 in num:
    print(f'o tres esta na posiçao {num.index(3)+1}°')
else:
    print('a quantidade de numero pares sao 0')
print('os valores impar sao',end=' ')
for n in num:
    if n %2 == 0:
        print(n, end=' ')
        
