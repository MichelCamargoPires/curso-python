palavra = ('aprender', 'programar', 'linguagem')

for p in palavra: # separar a lista 
    print(f'\nna palavra {p.upper()} temos ', end='')
    for letra in p: # separar a palava em letras 
        if letra.lower() in 'aeiu': # encontrar essas letras dentro das palavras 
            print(letra, end=' ')
