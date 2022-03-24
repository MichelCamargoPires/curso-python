
a = 1
while True:
    tab = int(input('digite um numero: '))
    for a in range (1, 11):
        a += 1   
        print('{} x {} = {}'.format(tab, a, a * tab))
        if tab < 0:
            break
