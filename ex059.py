''' crie um programa que leia dois valore mostre um menu na tela:
[1]soma
[2]multiplicar
[3]maior 
[4]novos numeros 
[5]sair do programa
seu programa devera realizar a operaçao solicitada em cada caso'''

n1 = 0
n2 = 0
qual = 0
n1 = float(input('digite um numero'))
n2 = float(input('digite outro numero'))
while qual != 5:
    print('*'*20)
    print('''[1]soma
    [2]multiplicar
    [3]maior 
    [4]novos numeros 
    [5]sair do programa''')
    print('*'*20)
    qual = int(input('qual operaçao vc quer :'))
    if qual == 1:
        re = n1 + n2
        print('a soma dos valors {} e {} é {}'.format(n1, n2 ,re))
    elif qual == 2:
        re = n1 * n2
        print('a multiplicaçao de {} e {} é {}'.format(n1, n2, re))
    elif qual == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('entra {} e {} é {}'.format(n1, n2, maior))
    elif qual == 4:
        n1 = float(input('digite outro numero:'))
        n2 = float(input('digite outro numero:'))
print('fim')

    

