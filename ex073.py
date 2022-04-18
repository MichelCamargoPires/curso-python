time = ('Corinthians', 'Atlético', 'Bragantino', 'Flamengo', 'Santos',
'Fluminense', 'Sao Paulo', 'Coritiba', 'América', 'Botafogo', 'Cuiabá',
'Ceará', 'Internacional', 'Avaí' 'Palmeiras', 'Juventude', 'Goiás', 'Atlético', 'Fortaleza', 'Athletico')
print('=-' *15)
print(f'lista de tima {time}')
print('=-' *15)
print(f'o cinco time clasificados foram {time[0:5]}')
print('=-' *15)
print(f'os quatros ultimos times {time[-4:]}')
print('=-' *15)
print(f'times em ordem alfabeticas {sorted(time)}')
print('=-'*15)
print(f'o sp esta em {time.index("Sao Paulo")+1}° da lista ')
