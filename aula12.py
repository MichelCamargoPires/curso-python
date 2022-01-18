nome = str(input('qual e seu nome: '))
if nome == 'michel': # operaçao simples
    print('que nome bonito {}'.format(nome))
elif nome =='pedro' or nome == 'maria' or nome == 'paulo': # estrutura consisional aninhada 
    print('seu nome e bem popular no brasil {}'.format(nome))
elif nome in 'ana claudia jessica julina':
    print('belo nome feminino {}'.format(nome))
else: # operaçao condicional composta // o else e opcional
    print('seu nome e bem comum {}'.format(nome))
print('tenha um bom dia {}'.format(nome))

# estrutura consicional aninhadas
