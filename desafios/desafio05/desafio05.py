print('='*10 + ' Desafio05 ' + '='*10)

while True:
    try:
        status = input('\nPosição do Papagaio: ')

        if(status == 'esquerda'):
            print('ingles\n')

        elif(status == 'direita'):
            print('frances\n')

        elif(status == 'nenhuma'):
            print('portugues\n')

        elif(status == 'ambas'):
            print('caiu\n')
        
        else:
            print('\nNão consegui compreender, tente novamente.')
            break
    except EOFError:
        print(EOFError)
        break