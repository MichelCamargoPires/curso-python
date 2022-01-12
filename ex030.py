#crie um programa que leia um numero e mostre se ele e par ou impar

numero = int(input('digite um numero: '))
acho = numero % 2
if acho == 1:
    print('seu numero e impar')
else:
    print('seu numero e par')
