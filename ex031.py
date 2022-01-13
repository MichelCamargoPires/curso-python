#desenvolva um programa que pegunte a distancia de uma viagem em km .
#calcule o preço da passagem,cobrada r$0.50 por km para viagens ate 200km e r$0.45 para viagens mais longas


viagem = float(input('quantos km vc vai viajar: '))
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('sua viagem custo {}'.format(preço))
    
