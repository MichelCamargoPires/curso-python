#desenvolva uma ogica que leia o peso e altura de uma pessoa e calcule o imc e mostre de acordo com a tabela 

# abaixo de 18.5 abaixo do peso

# entre 18.5 e 25 peso ideal

#25 ate 30 sobrepeso

# 30 ate 40 obesidade morbida 

peso = float(input('digite seu pesso: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura * altura)
print(imc)
if imc <= 18.5:
    print('vc esta abaixo do peso {}'.format(imc))
elif imc <= 25.0:
    print('vc esta no peso ideal {}'.format(imc))
elif imc <= 30:
    print('vc esta com sobrepeso {}'.formar(imc))
else:
    print('vc esta com obesidade morbida {}'.formt(imc))
