#crie em programa que leia o ano de nascimento de sete pssoa e mostre quantas pessoas ja atingirao a maioridade e qantas nao 
# conciderar maior 21

from datetime import date
contmaior = 0
contmenor = 0
hoje = date.today().year
for pessoas in range(1, 7):
    dados = int(input('digite o ano que vc nasceu: '))
    nasceu = hoje - dados
    if nasceu >= 21:
        contmaior += 1
    elif nasceu <= 20:
        contmenor += 1
print('maior {}'.format(contmaior))
print('menor {}'.format(contmenor))
