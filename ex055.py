#faça um programa que leia o peso de cinco pessoas . no final motres  qual foi o maior eo menor pesso lido
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('qual seu pesso'))
    if p == 1: #pemeiro 
        menor = p # resebe como o mesmo peso
        maior = p
    else:
    if peso > maior: # se o peso for maior
        maior = peso # pesso resebe maior 
    if peso < menor:
        menor = peso
print('maior peso e {} eo menor pesso e {}'.format(maior, menor))
