''' rafaça o DESAFIO 051. lendo o primeiro termo ea razao de uma PA . mostrando 
as 10 primeiras termos da progressao usando a estrutura while'''

print('gerador de pa')
print('--'*10)
primeiro = int(input('primeiro termo: '))
razao = int(input('razao da pa: '))
termo = primeiro
const = 1
while const <= 10:
    print('{} ->>'.format(termo),end='')
    termo += razao
    const += 1
print('fim')

