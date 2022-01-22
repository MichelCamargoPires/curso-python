#crie um programa que faça  computador jogar jocknpo com voce :)
import random
print('''[1] PEDRA
[2] PAPEL
[3] TESOURA''')
palpite = int(input('digite: '))
sorteio = random.randint(1, 3)
if sorteio == 1 and palpite == 3:
    re = 'computador pedra... perdeu otario!!!'
elif sorteio == 3 and palpite == 2:
    re = 'computador tesoura... prtdeu otario!!!'
elif sorteio == 2 and palpite == 1:
    re = 'computador papel... perdeu otario!!'
elif sorteio == 3 and palpite == 1:
    re = 'vc ganho skynet aqui NAO computador resoura'
elif sorteio == 2 and palpite == 3:
    re = 'vc ganho skynet aqui NAO computador papel'
elif sorteio == 1 and palpite == 2:
    re = 'vc ganho skynet aqui NAO computador  pedra' 
elif sorteio == palpite:
    re = 'vc empatou com o computadot'


print(re)
