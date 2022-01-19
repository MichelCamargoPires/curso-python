# crie um programa que leia duas notas e calcule a media . mostrando no final. de acordo com a media anttingida

# media abaixo da 5.0 reprovado

# media 5,0 e 6.9 recuperaçao

#media 7.0 ou superior aprovado

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('sua media foi {} vc foi reprovado'.format(media))
elif media > 7.0:
    print('vc foi aprovado sua nova foi {} vc foi aprovado'.format(media))
else:
    print('vc esta de recupercao sua nota foi {}'.format(media6))
