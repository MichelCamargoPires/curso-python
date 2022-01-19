#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa . o programa vai perguntar o VALOR DA CASA,o SALARIO do comprador  
#QUANTOS ANOS  ele vai pagar

#calcule o valor da prestaçao mensal sabendo que ela nao pode exder 30% do salario ou estao o emprestimo sera negado

valorDaCasa = float(input('qual o valor da casa: '))
print('-------------------------------------')
salario = float(input('quanto vc ganha: '))
print('-------------------------------------')
anos = int(input('quantos anos vc vai pagar: '))
parcela = valorDaCasa / (anos * 12 )
psSalario = salario * 30 / 100
if parcela <= psSalario :
    print('aprovado')
else:
    print('negado')
print('parcela da sua casa e: {:.2f}'.format(parcela))
print('-------------------------------------')
print('30% do seu salario{:.2f}'.format(psSalario))
print('-------------------------------------')
