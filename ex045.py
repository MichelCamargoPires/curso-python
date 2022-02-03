#crie um programa que faça  computador jogar jocknpo com voce :)

#import random
#print('''[1] PEDRA
#[2] PAPEL
#[3] TESOURA''')
#palpite = int(input('digite: '))
#sorteio = random.randint(1, 3)
#if sorteio == 1 and palpite == 3:
#    re = 'computador pedra... perdeu otario!!!'
#elif sorteio == 3 and palpite == 2:
#    re = 'computador tesoura... prtdeu otario!!!'
#elif sorteio == 2 and palpite == 1:
#    re = 'computador papel... perdeu otario!!'
#elif sorteio == 3 and palpite == 1:
#    re = 'vc ganho skynet aqui NAO computador resoura'
#elif sorteio == 2 and palpite == 3:
#   re = 'vc ganho skynet aqui NAO computador papel'
#elif sorteio == 1 and palpite == 2:
#   re = 'vc ganho skynet aqui NAO computador  pedra' 
#elif sorteio == palpite:
#    re = 'vc empatou com o computadot'

from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opçoes:
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input('qual e a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-'*40)
print('computador jogo: {}'.format(itens[computador]))
print('jogador jogo: {}'.format(itens[jogador]))
print('-'*40)
if computador == 0: #computador jogo pedra 
    if jogador == 0:
        print('EMPATA')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: #computador jogo papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE ')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: #computador jogo tesouro
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
