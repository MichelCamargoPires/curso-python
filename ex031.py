#desenvolva um programa que pegunte a distancia de uma viagem em km .
#calcule o preço da passagem,cobrada r$0.50 por km para viagens ate 200km e r$0.45 para viagens mais longas


viagem = float(input('quantos km vc vai viajar'))
baixo = viagem * 0.50
alta = viagem * 0.45
if viagem <= 200:
    print('sua viagem vai custar{}'.format(baixo))
else:
    print('sua pasagem vai custar{}'.format(alta))
