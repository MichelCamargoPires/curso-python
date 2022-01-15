#escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu almento

#para salarios a r$1.250,00 calcule um aumento de 10%

#para os inferiorres ou ingual e de 15%

salario = float(input('qual seu salario'))
if salario > 1250:
    novo = (salario * 10 / 100) + salario
else:
    novo = (salario * 15 / 100) + salario
print('seu salario teve um almento {}'.format(novo))


   
