
cont = ('zero', 'um','dois', 'tres', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove',
'dez', 'onze', 'doze', 'treze', 'quatose',
'quise', 'dezeses', 'dezessete', 'desoito', 'desnove', 'vinte')

while True:
    num = int(input('digite um numero'))
    if 0 <=  num <=20 :
        print('tente novamente ')
        break
print(f' o numero {num} se chama {cont[num]}')
