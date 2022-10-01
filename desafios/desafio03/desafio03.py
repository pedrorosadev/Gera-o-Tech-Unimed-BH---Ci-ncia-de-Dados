print('='*10 + 'Desafio 03' + '='*10)

time_spent = int(input('\nTempo Gasto(horas): '))
mean_speed = int(input('Velocidade Média(km/h): '))

liter =  mean_speed * time_spent 
liters_needed = liter / 12

print(f'\nQuantidade de Litro necessária para a viagem: {liters_needed:.3f}')