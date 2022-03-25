'''faça um programa que jogue  par ou inpar com vc intenrompa o jogo perder mostre o talata de 
de vitorias consecutivas que ele conseguiu no  fim do jogo 
'''
import random
sort = cont = 0
while True:
    ip = str(input('impar ou par[i/P]?: '))
    paupite = int(input('qual o numero vc quer?: '))
    sort = random.randint(1, 10)
    soma = sort + paupite
    resto = soma % 2
    if ip == 'i':
        if resto == 1:
            print('-'*30)
            print('vc ganho')
            print('-'*30)
            cont =+ 1
        elif resto == 0:
            break
    if ip == 'p':
        if resto == 0:
            print('-'*30)
            print('vc ganhou ')
            print('-'*30)
            cont += 1
        elif resto == 1:
            break
print(f'vc ganhou do pc {cont}')
