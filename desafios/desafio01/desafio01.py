print('='*10 + 'Desafio 01' + '='*10)

distance = int(input('\nDistância entre os Palantír\'s: '))
diameter1 = int(input('Diâmetro do Palantír de Sauron: '))
diameter2 = int(input('Diâmetro do Palantír de Saruman: '))

icm = distance / (diameter1 + diameter2)
print(f'\nInterferência de Comunicação Mágica: {icm:.2f}')
