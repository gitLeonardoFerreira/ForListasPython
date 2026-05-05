"""
preencha uma lista com numeros aleatorios nao repetidos de 1 a 20
"""
import random

numeros = []
for i in range(10): #gera 10 numeros de 0 a 9
    numero = random.randint(1, 20)
    while numero in numeros:
        numero = random.randint(1, 2)
    numeros.append(numero)
#
print(numeros)

