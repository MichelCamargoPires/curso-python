#faça um programa que leia o ano de nascimento de umjovem e informe , de acordo com sua idade 

# se ele AINDA VAI SE ALISTAR ao serciço militar

# se e a HORA DE SE ALISTAR

# se ja PASSOU DO TEMPO do alistamento

#seu programa tembem tera que mosrtar o tempo que falta ou passou do prazo

ano = int(input('quantos anos vc tem?: '))
idade = 2022 - ano 
if idade < 18:
    re = 18 - idade
    print('falta {}'.format(re))
elif idade > 18:
    re = idade - 18
    print('passou {}'.format(re))
else:
    print('vai se alista')

