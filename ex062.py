print('gerador de pa')
print('--'*10)
primeiro = int(input('primeiro termo: '))
razao = int(input('razao da pa: '))
termo = primeiro
const = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while const <= 10:
        print('{} ->>'.format(termo),end='')
        termo += razao
        const += 1
    print('vai incara')
mais = int(input('mais quanto: '))


terminar
