n = cont = soma = 0
n = int(input('digite um numero diferente de 999: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('digite um numero diferente de 999: '))
print('vc digitou {} e a soma deles e {}'.format(cont, soma))
