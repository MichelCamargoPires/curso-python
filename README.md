#desenvova um programa que leia o comprimento de tres retas e diga ao usuario se ela podem ou naoformar um triangulo               

n1 = float(input('digite o primeiro valor: '))
n2 = float(input('digite o segundo valor: '))
n3 = float(input('digite o terseiro valor:'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('seu seguimento pode formar um triagulo')
else:
    print('seu deuimento pode formst um triangulo: ')
