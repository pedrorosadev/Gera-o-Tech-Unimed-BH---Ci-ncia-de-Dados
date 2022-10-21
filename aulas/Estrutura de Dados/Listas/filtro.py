numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
#quadrado = [numero ** 2 for numero in numeros]
pares = []
#pares = [numero for numero in numeros if numero % 2 == 0]

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

for numero in numeros:
    quadrado.append(numero**2)

print(numeros)
print(pares)
print(quadrado)