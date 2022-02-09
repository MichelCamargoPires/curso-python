#desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares . se o valor digitado for impar desconsidere 
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite {}º numero: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('a soma dos  {} valore inpar somados dao {}'.format(cont, soma))
