'''crie um programa que laia varios numero inteiros pelo teclado . o programa 
so vai para quando o 999 , que e o condiçao de parada . no final mostre quantos numeros
foram digitados qual foi a soma deles (descosidere o flag)'''

n = s = c = 0
while True:
    n = int(input('digite um numero para fazer uma soma: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'a sua soma foi {s} e vc digitou {c}')
