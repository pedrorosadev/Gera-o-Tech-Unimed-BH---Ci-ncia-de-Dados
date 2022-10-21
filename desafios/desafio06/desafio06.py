print('='*10 + ' Desafio 06 ' + '='*10)

salary = int(input('\nDigite seu salário: ')) 

if (salary >= 0 and salary <= 600):
    readjustment = (salary * 17/100)
    currentSalary = salary + readjustment
    percentual = (readjustment * 100) / salary

    print(f'\nNovo salário: {currentSalary:.2f}')  
    print(f'\nReajuste Ganho: {readjustment:.2f}')
    print(f'\nEm percentual: {percentual:.0f}%')

elif (salary >= 600.01 and salary <= 900):
    readjustment = (salary * 13/100)
    currentSalary = salary + readjustment
    percentual = (readjustment * 100) / salary

    print(f'\nNovo salário: {currentSalary:.2f}')  
    print(f'\nReajuste Ganho: {readjustment:.2f}')
    print(f'\nEm percentual: {percentual:.0f}%')

elif (salary >= 900.01 and salary <= 1500):
    readjustment = (salary * 12/100)
    currentSalary = salary + readjustment
    percentual = (readjustment * 100) / salary

    print(f'\nNovo salário: {currentSalary:.2f}')  
    print(f'\nReajuste Ganho: {readjustment:.2f}')
    print(f'\nEm percentual: {percentual:.0f}%')

elif (salary >= 1500.01 and salary <= 2000):
    readjustment = (salary * 10/100)
    currentSalary = salary + readjustment
    percentual = (readjustment * 100) / salary

    print(f'\nNovo salário: {currentSalary:.2f}')  
    print(f'\nReajuste Ganho: {readjustment:.2f}')
    print(f'\nEm percentual: {percentual:.0f}%')

elif (salary > 2000):
    readjustment = (salary * 5/100)
    currentSalary = salary + readjustment
    percentual = (readjustment * 100) / salary

    print(f'\nNovo salário: {currentSalary:.2f}')  
    print(f'\nReajuste Ganho: {readjustment:.2f}')
    print(f'\nEm percentual: {percentual:.0f}%')

else: 
    print('\nNão consegui compreender, tente novamente.')