nome = str(input('qual seu nome? '))
if nome == 'michel':
    print('que nome bonito vc tem')
else:
    print('seu nome e tao normal')
print('bom dia {}'.format(nome))

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digutre a outra nota: '))
m = (n1 + n2)/2
print('sua nota foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua media foi boa ! PARABENS')
else:
    print('sua media foi ruim !ESTUDE MAIS ')


print('parabens'if m >= 6 else'estude mais') #  /////// condiçao simplificada nao gostei kkkk
