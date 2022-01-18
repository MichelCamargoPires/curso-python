print('\033[1;31;43mola mundo!\033[m')#letra vemelha, back amarelo
print('\033[4;30;45mola mundo!\033[m')#letra underkine, back em lilas 
print('\033[0;33;44mola mundo!\033[m')#letra amarela .back em azul
print('\033[7;33;44mola mundo!\033[m')#letra amarela, back azul negativo

# aprofunda na locura 

a = 3 
b = 5
print('Os valores sao \033[32;44m{}\033[m e \033[31;44m{}\033[m'.format(a, b))

#vamos separar a locura 

nome ='michel'
print('muito prazer em te conhecer, {}{}{}'.format('\033[4;34m',nome,'\033[m'))

#criar uma variavel com as cor 

cores = {'linpar':'\033[m', 
        'azul':'\033[34m', 
        'amarelo':'\033[7;30m'
        'pretoebranco':'\033[7;30m'}

print('ola muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['linpar']))
        
