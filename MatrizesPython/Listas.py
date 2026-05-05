#Listas

minhaLista = [] #Lista
#acrescentar valores na lista
#Append
minhaLista.append('Café')

#Lista permite elementos heterogenos
minhaLista.append(12)

print(minhaLista)

#recuperando o valor de uma determinada posicao
#0          1
#-2        -1
#['Café', 12]
print(f'segundo elemento: {minhaLista[1]}')
print(f'segundo elemento: {minhaLista[-1]}')

#Juntando duas listas (com extend)
complemento = ['açucar', 'agua quente', 'canela']
print('\n')
print(complemento)

#Aqui acrescenta os elementos da lista complemento na minhaLista
minhaLista.extend(complemento)
print(minhaLista)

#Localizando um elemento pelo indíce
print(f'A agua quente esta na posicao: {minhaLista.index('agua quente')}')

#apagando um elemento
#atraves de um indice
minhaLista.pop(3) #indice da agua quente
print(minhaLista)

#remover pelo proprio elemento
minhaLista.remove(12) #aqui é o elemento 12 e nao o indice
print(minhaLista)

#alterando o conteudo de um elemento
minhaLista[0] = 'café'
print(minhaLista)

#tentar acessar um indice que não existe
#print(minhaLista[5])

#inserindo um elemento em uma determinada posicao
#  0        1          2
#['café', 'açucar', 'canela']
#['café', 'açucar', 'chantilly', 'canela']
minhaLista.insert(2, 'chantilly')
print(minhaLista)

#ordenacao da lista
# ha dois tipos de ordenacao
#a ordenacao que é uma funcao nativa do python
#a ordenacao da propria classe list
#o que elas diferem?

print('\nOrdenacao com funcao nativa do python')
print(minhaLista)
print(sorted(minhaLista))

print('\nOrdenacao com metodo da classe list')
print(minhaLista)
minhaLista.sort()
print(minhaLista)

print('\nCom numeros')
meusNumeros = [1, 4, 6, 23, -1, 8, 0, 76, 2]
print(meusNumeros)
print('Ordenando temporariamente so para a impressado com SORTED')
print(sorted(meusNumeros))
print('Ordenando para todo sempre com o .sort()')
print(meusNumeros)
meusNumeros.sort()
print(meusNumeros)
print('Ordenando para todo sempre INVERSO com o .sort()')
meusNumeros.sort(reverse=True)
print(meusNumeros)
meusNumeros = [1, 4, 6, 23, 0, -1, 0, 76, 0, 2]
print(meusNumeros)
print(f'Qtos zeros tem na lista: {meusNumeros.count(0)}')
print(f'Onde esta o primeiro zero na lista:{meusNumeros.index(0)}')
print(f'onde esta  segundo zero: {meusNumeros.index(0,meusNumeros.index(0)+1)}')

#tamanho
print(f'Tamanho dos meusNumeros: {len(meusNumeros)}')
#min
print(f'Minimo: {min(meusNumeros)}')
#max
print(f'Maximo: {max(meusNumeros)}')