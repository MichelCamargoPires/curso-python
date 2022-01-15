#faça um programa que leia um ano qualquer e mostre se ele e  bissexto
from datetime import date
ano = int(input('quantos dias tem o seu ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('bissexto')
else:
    print('seu ano e bissexu')
