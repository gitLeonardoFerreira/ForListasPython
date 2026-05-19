#Listas

#Colecao flexivel
minhaLista = ['café', 'açucar', 'agua']
print(minhaLista)

#Indexizacao
#   0       1       2
#   -3      -2      -1
#['café', 'açucar', 'agua']
#sempre : o primerio é o zero e o ultimo é o menos 1
print(f'Primeiro elemento: {minhaLista[0]}')
print(f'Ultimo elemento(indice negatico): {minhaLista[-1]}')
print(f'Ultimo elemento(indice positivo): {minhaLista[2]}')
print(f'\n\n')
minhaLista = ['café', 'açucar', 'agua', 'chantilly', 'canela']
print(minhaLista)

#Slicing - fatiamento
#   0       1        2         3           4
# -5       -4          -3        -2        -1
#['café', 'açucar', 'agua', chantiççy, canela]
#SINTAXE  lista[inicio:fim-1:pulo] mesmo raciocinio do RANGE
parteLista = minhaLista[2:4+1]
#parteLista = minhaLista[2:] #se deixar os : sem nada ele pega a lista toda ate o final
print(parteLista)
print(f'equivalente ao lado negativo: {minhaLista[-3:]}')
print(f'invertendo: {minhaLista[3:1-1:-1]}')
print(f'pulando{minhaLista[0::2]}')#::2 ele pula de dois em dois, se fosse ::3 seria de 3 em 3


#Concatenacao
#Juntar duas listas
print(f'\n')
complemento = ['raspas de limao']
minhaLista = minhaLista + complemento
print(minhaLista)
print('extend')
maiselementos = ['pimenta']
minhaLista.extend(maiselementos)
print(minhaLista)


#Alteracao
print('\nAlterando um elemento')
minhaLista[5] = 'raspas de laranja'
print(minhaLista)


#Inclusao
print('\nIncluindo')
print('append - insere no final')
minhaLista.append('gengibre')
print(minhaLista)
print('insert - insere em uma posicao 3')
minhaLista.insert(3, 'chocolate em po')
print(minhaLista)


#Exclusao
print(f'\n')
minhaLista.pop()
print(minhaLista)
#pop de uma posicao 3
minhaLista.pop(3)
print(minhaLista)


#Sort
print(f'\n')
minhaLista.sort()
print(minhaLista)

print(f'\n')

#Sorteio
# import random
#
# teste = ['agua', 'açucar', 'café', 'canela', 'chantilly', 'pimenta', 'raspas de laranja']
# print(teste)
# print(f'tamanho: {len(teste)}')
# aleatorio = []
# indices_sorteado = []
# while len(aleatorio) != len(teste):
#     indices_sorteado = random.randint(0,6)
#     if indices_sorteado not in indices_sorteado:
#         aleatorio.append(teste[indices_sorteado])
#     indices_sorteado.append(indices_sorteado)
# print(aleatorio)

#Matriz nada mais é que lista dentro de lista
matriz = [[0, 1, 2], [3, 4, 5]]
print(matriz)
#alterando o valor 2 para 8
matriz[0][2] = 8
print(matriz)
#imprimindo elemento a elemento
for linha in matriz:
    for coluna in linha:
        print(coluna)
#0 1 2
#3 4 5
for linha in matriz:
    for coluna in linha:
        print(coluna, end='\t')
    print()