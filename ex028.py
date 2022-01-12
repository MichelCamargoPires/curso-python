#escreva um origrama que "pensa" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero
#escolhido pelo computador

# o programa devera escrever na tela se o usuavio venceuou perdeu

import random
paupite = int(input('qual seu palpite: '))
sorteio = random.randint(1, 5)
print(sorteio)
if paupite == sorteio:
    print('vc deu sorte ')
else:
    print('vc errou')
    
