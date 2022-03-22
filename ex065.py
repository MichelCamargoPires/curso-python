from traceback import print_tb


resp = 'S'
maior = menor = cont = soma = p = n = 0
while resp != 'N':
    n = int(input('digite um numero: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('quer continuar: ')).upper().strip()[0]
media = soma / cont
print('vc digitou {} numero e a media {}'.format(cont, media))
print('o maior numero foi {} menor foi {}'.format(maior, menor))
