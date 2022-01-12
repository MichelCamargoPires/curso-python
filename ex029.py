# escreva um programa que leia a velocidade de um carro

#se ele ultrapassar 80km/h. mostra uma mensagem dizando que ele foi multado

#a mula vai custa r$ 7,00 por cada km acima do limite


velocidade = int(input('qual sua velocidade '))
multa = (velocidade - 80) * 7
if velocidade < 80:
    print('vc esta na velocidade correta')
else:
    print('vc foi multado, valor da multa {}.00r$'.format(multa))
