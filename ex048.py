#faça um programa que que caucule a some entre todos os numeros inpores que sao multiblos de tres e que se encontram no intervalo de 1 ate 500

soma = 0 
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
print(soma)
