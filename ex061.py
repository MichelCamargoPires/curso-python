''' rafaça o DESAFIO 051. lendo o primeiro termo ea razao de uma PA . mostrando 
as 10 primeiras termos da progressao usando a estrutura while'''

num = int(input('digite o primeiro numero: '))
print('-'*25)
pa = int(input('digite a pa: '))
decimo = num + (10 - 1) * pa 
for c in range (num, decimo, pa ):
    print('{}'.format(c), end=' * ' )
print('acabou')

#terminar
