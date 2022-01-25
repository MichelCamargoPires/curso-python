#faça um programa que leia o ano de nascimento de umjovem e informe , de acordo com sua idade 

# se ele AINDA VAI SE ALISTAR ao serciço militar

# se e a HORA DE SE ALISTAR

# se ja PASSOU DO TEMPO do alistamento

#seu programa tembem tera que mosrtar o tempo que falta ou passou do prazo

from datetime import date
atual = date.today().year
print('''[1] para masculino 
[2] para feminino''')
sexo = int(input('digite: '))
ano = int(input('em que ano voce nasceu?: '))
idade = atual - ano 
if  sexo == 2:
    print('vc e do sexo feminino vc nao e obrigada a se alista')
    print('''[1] para se alista
[2] nao se alista''')
    opcao = int(input('digite: '))
    if opcao == 2:
        print('ok vc deseja se alistar ')
    elif idade < 18:
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
        print('vc tem {} vc ja pode se alistar'.format(idade))
elif idade < 18:
    re = 18 - idade
    anoAlistamento = re + atual
    print('falta {}'.format(re))
    print('seu alistamento e no ano {}'.format(anoAlistamento))

elif idade > 18:
    re = idade - 18
    print('passou {}'.format(re))
    anoAlistamento = atual - re
    print('seu alistamento foi no ano {}'.format(anoAlistamento))
