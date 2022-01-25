#faça um programa que leia o ano de nascimento de umjovem e informe , de acordo com sua idade 

# se ele AINDA VAI SE ALISTAR ao serciço militar

# se e a HORA DE SE ALISTAR

# se ja PASSOU DO TEMPO do alistamento

#seu programa tembem tera que mosrtar o tempo que falta ou passou do prazo

from datetime import date
atual = date.today().year
ano = int(input('em que ano voce nasceu?: '))
idade = atual - ano 
if idade < 18:
    re = 18 - idade
    anoAlistamento = re + atual
    print('falta {}'.format(re))
    print('seu alistamento e no ano {}'.format(anoAlistamento))
elif idade > 18:
    re = idade - 18
    print('passou {}'.format(re))
    anoAlistamento = atual - re
    print('seu alistamento foi no ano {}'.format(anoAlistamento))
else:
    print('vai se alista vc tem {}'.format(idade))



