'''melhore o jogo do desafio 028 onde o computador vai ''pensar '' em um numero
entre 0 e 10 . so que agora o jogador vai tentar adivinhar ate  acerter ,, mostrar 
no final quantos necessarios pata vencer '''


paupite = 0
import random 
sorteio = random.randint(1, 10)
while sorteio != paupite:
    paupite = int(input('qual seu palpite: '))
    print('soretio {} e paupite {}'.format(sorteio, paupite))



