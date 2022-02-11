# desenvolva um programa que leia o primeiro termo ea razao de uma PA no final mostrande as 10 primeiras termos dessa progressao

num = int(input('digite o primeiro numero: '))
print('-'*25)
pa = int(input('digite a pa: '))
decimo = num + (10 - 1) * pa 
for c in range (num, decimo, pa ):
    print('{}'.format(c), end=' * ' )
print('acabou')
