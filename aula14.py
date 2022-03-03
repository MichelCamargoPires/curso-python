for c in range(1, 10):
    print(c)
print('fim')

a = 1
while a < 10:
    print(a)
    a = a + 1
print('fim')

n = 1
while n != 0: # ponto de parada 
    n = int(input('digite um valor'))
print('fim')

r = 's'
while r == 's':
    n = int(input('digite um bumero'))
    r = str(input('quer continuar [s/n]'))
print('fim')

b = 1
par = impar = 0
while b != 0:
    b = int(input('digite um valor'))
    if b != 0:
        if b % 2 == 0:
            par += 1
        else:
            impar += 1
print('vace digito {} numero pares e {} numero impares'.format(par, impar))
