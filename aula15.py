'''cont = 1
while True:
    print(cont, '-> ',end='')
    cont += 1
print('acabo')'''# programa infino 

# white finito 
n = cont = 0
while cont < 3:
    n = int(input('digite um numero: '))
    cont += 1
print('fim do primeiro tex')
n2 = 0
# white ininito ate vc digitar 999
while n2 != 999:
    n2 = int(input('digite um valor ')) 
print('fim do terseiro text')
#solusao do fim do laço sem somara o fim 
n3 = s = 0
while True:
    n3 = int(input('digite um valor '))
    if n3 == 999:
        break
    s += n3
print('a soma vale {}'.format(s))
print(f'a soma vale {s}')# forma nova de imprimier 
