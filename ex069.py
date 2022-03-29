'''crie um programa que leia a idade e o sexo de varios pessoas a cada pessoa 
cadastrada o programa devera pergunatar se o usuario quer ou nao continuar no final 
motrar 

a) quantas pessoas tem maisn de 18

B) quantos homens formam cadastrados 

c) quantas mulhers tem menos de 20 anos '''
contD = contM = contF = contFV = 0 
while True:
    idade = int(input('qual a idade?: '))
    sex = str(input('qual seu sexo [f/m]'))
    text = str(input('quer continuar? '))
    if sex == 'm':
        contM += 1
        if idade >= 18:
            contD += 1
    elif sex == 'f':
        if idade < 20:
            contFV += 1
        elif idade >= 18:
            contD += 1
    if text == 'n':
        break
print(f'tem {contD} pessoa maior de 18')
print(f'tem {contM} homens cadartrados ')
print(f'tem {contFV} meninas com menos de 21')
        

    
