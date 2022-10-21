import string

print('='*10 + ' Desafio 04 ' + '='*10)

alphabet = list(string.ascii_uppercase)
#print(alphabet)

letter = input('\nDigite uma letra: ')
index_letter = alphabet.index(letter)

print(index_letter + 1)
