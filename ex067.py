
a = 1

while True:
    tab = int(input('digite um numero: '))
    while a < 10:
        a += 1
        print('{} x {} = {}'.format(tab, a, a * tab))
