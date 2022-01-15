#escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu almento

#para salarios a r$1.250,00 calcule um aumento de 10%

#para os inferiorres ou ingual e de 15%

salario = float(input('qual seu salario'))
maior = (salario * 10 / 100) + salario
menor = (salario * 15 / 100) + salario
if salario > 1250:
    print('seu almento foi de 10% {}'.format(maior))
else:
    print('seu salario teve um almento de 15% {}'.format(menor))

