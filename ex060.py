'''faça um programa que leia um numero qualquer e mostres seu fatorial 

ex
5! = 5x4x3x2x1=120'''

n = int(input('digite um numero para ser fatorado: '))
c = n
f = 1
while c > 0: 
    print('{}'.format(c),end='')
    print(' x 'if c > 1 else '=', end='')
    f = f * c
    c -= 1
print(f)
