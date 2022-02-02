#elabore um pragrama que calcule o valor a ser pago por um produto preço normal e condiçao de pagamento

#a vista DINHEIRO / CHEQUE 10% DESCONTO

# AVISTA CARTAO 5% DE DESCONTO

#EM ATE 2X NO CARTAO PREÇO NORMAL 

#3X OU MAIS NO CARTAO 20% DE JUROS
print('=====lojas michel=====')
produto = float(input('preso do produto: '))
print('''============================
***vc vai pagar como***
======================================''')
print(''' a vista ou cheque digite [1]
--------------------------------------
a vista no cartao digite ...       [2]
--------------------------------------
em ate 2x digite ...               [3]
--------------------------------------
em 3x digite...                    [4]''')
print()
pagamento = int(input('qual a forma de pagamento: '))
if pagamento == 1:
    total = produto - (produto * 10 / 100 )
    print('vc tem o desconto de 10% seu produto vai custar {} R$'.format(total))
elif pagamento == 2:
    total = produto - (produto * 5 /100)
    print('vc tem o desconto de 5% seu produto vai custar {} R$'.format(total))
elif pagamento == 3:
    print('vc vai pagar o preso normal {} R$'.format(produto))
elif pagamento == 4:
    total = produto + (produto * 20 /100) 
    print('vc tem juros de {} R$'.format(total))
else:
    total = produto
    print('essa opçao [{}] e invalalida'.format(pagamento))
