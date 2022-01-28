r1 = float(input('primeiro sogmento '))
r2 = float(input('segundo seguimento '))
r3 = float(input('terceiro seguimento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar triangulo ',end='')#PARA JUNTAR UMA LINHA NA OUTRA  
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 =! r2 =! r3:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('nao pode formar triangulo')
