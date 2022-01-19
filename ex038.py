#escreva um programa que leia dois numero inteiros e compare-os mostrando uma mensagem 

#o primeiro valor e maior 

#o segunto e maior
 
#nao exite valar maior os dois sao iguais 

numero1 = int(input('digite um numero: '))
numero2 = int(input('digite um outro: '))
if numero1 > numero2:
    print('numero {} e maior'.format(numero1)) 
elif numero1 < numero2:
    print('numero {} e maior'.format(numero2))
else:
    print('{} e {} sao igual'.format(numero1, numero2))
