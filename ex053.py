#crie um programa que leia uma frase qualquer e mostre de ela e um PALINDROMO desconsederando espaços

# arara

frase = str(input('digite uma frase: ')).strip().upper()
separar = frase.split()
junto = ''.join(separar)
inveso =''
for letra in range(len(junto) -1 ,-1,-1):  
    inveso += junto[letra]  
print(inveso)
if inveso == frase:
    print('{} e um palidromo'.format(frase))
else:
    print('afase {} nao e um palidromo'.format(frase))
