#faça um programa que leia o ano de nascimento de umjovem e informe , de acordo com sua idade 

# se ele AINDA VAI SE ALISTAR ao serciço militar

# se e a HORA DE SE ALISTAR

# se ja PASSOU DO TEMPO do alistamento

#seu programa tembem tera que mosrtar o tempo que falta ou passou do prazo

idade = int(input('quantos anos vc tem?: '))
if idade < 18:
    falta =  18 - idade
    print('falta {} anos'.format(falta))
elif idade == 18:
    print('na hora')
elif idade > 18:
    passou = idade - 18
    print('passou {} anos'.format(passou))
else:
    print(' desculpe digite novamnete :(')
