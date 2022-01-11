# faça um programa que leia uma frase pelo teclado e mostre

# quantas vezes aparece a letra "a"

# em que posiçao ela aparece a primeira vez

# em que posiçao ela aparece por ultima vez

frase = str(input('digite uma frase')).upper()

contar_a = frase.count('A')
encontra_primeiro_a = frase.find('A')+1 #1+ e para pular uma casa para ficar mais bonito
encontra_ultimo_a = frase.rfind('A')+1 #r e para dizer que e pra contar da direita para esquerda 

print('tem {} "a" na frase'.format(contar_a))
print('o primeiro "a" foi encontrado na posiçao {} da frase'.format(encontrar_primeiro_a))
print('o ultimo "a" que foi encontrado foi {}'.format(encontrar_ultimo_a))
