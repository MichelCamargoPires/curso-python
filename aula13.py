#paço c no intervalo (0, 3):
    #se:
        #pega
    #passo
    #pula
#passo
#pega

for c in range(1, 6): # fazer repetir 6x
    print('oi') # repeir porque esta dentro do laço 
print('fim') # finalizaçao do programa fora do laço 

for c in range(1, 10):
    print(c) # c de contador 
print('fim')

for c in range(6, 0, -1): # comtar de tras pra frente 
    print(c)
print('fim')

for c in range(0, 7, 2): #conatar de 0 a 7 de dois em dois
    print(c)
print('fim')

n = int(input('digite um numero'))
for c in range (0, n + 1):
    print(c)
print('fim')

i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo'))
for c in range(i, f + 1, p):
    print(c)
print('fim')

for c in range(0, 3):
    n = int(input('digite um valor '))
print('fim')

s = 0 
for c in range(0, 4):
    num = int(input('digite outro numero'))
    s += num
print('a soma de todas os valores foi {}'.format(s))
