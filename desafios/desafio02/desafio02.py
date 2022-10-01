print('='*10 + 'Desafio 02' + '='*10)

hotdogs = int(input('\nCachorros-Quentes Consumido no Total: '))
participants = int(input('Participantes Totais: '))

if(hotdogs >= 1 and participants <= 1000):
    mean_hotdogs = hotdogs / participants
    print(f'\nNúmero médio de Cachorros-Quentes Consumido: {mean_hotdogs:.2f}')
else:
    print('\nValores inválidos para efetuar o cálculo :(\nTente novamente.')
