'''faça um programa que mostre a tabuada de varios numeros um de cava vez 
para cada valor digitado pelo usuario .o programa sera o numero solicidado for negativo '''


a = 1
while True:
    tab = int(input('digite um numero: '))
    if tab < 0: 
        break
    for a in range (1, 11):
        print('{} x {} = {}'.format(tab, a, a * tab))
        a += 1
print('fim')
        
