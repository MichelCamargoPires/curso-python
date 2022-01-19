#escreva um programa que leia um numero inteiro qual quer e paça para o usuario escolher qual qua base da conversao 

#para binario

#para octol

#para hexedecimal

num = int(input('digite um valor inteiro '))
print('''escolha uma das camversao:
[1] converter para BINARIO
[2] converter para OCTAL 
[3] converter para HEXADECIMAL''')
opcao = int(input('sua opcao: '))
if opcao == 1:
    print(' {} convertido para binario e {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal e {}'.format(num, hex(num)[2:]))
else:
    print('opcao invalida, tente novamente ')
