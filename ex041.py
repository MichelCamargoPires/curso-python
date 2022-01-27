# a confederaçao nacional de nataçao precisa de um programa que leia o ano de nacimento de um atleta e mortre sua categoria de acordo com a idade 

# ate 9 anos mirim

#ate 14 anos infantil 

#ate 19 anos junior 

#ate 20 anos senior

#acima master opkpok

from datetime import date
atual = date.today().year
nascimento = int(input('qual ano que vc nasceu : '))
idade = atual - nascimento
if idade <= 9:
    print('vc e mirim')
elif idade == 19:
    print('vc e junior')
elif idade == 20:
    print('vc e senior')
elif idade <= 14:
    print('vc e infantils')
else:
    print('mestre')
