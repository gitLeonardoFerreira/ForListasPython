#Funções
#Para organizar o codigo
#Para reaproveitamento
#Primo pobre do microservico
from openpyxl.styles.builtins import total


#Sintaxe
#def nome_dafuncao(parametros separados por virgula):
#   instruncoes
#   return expressao

#1o passo é a definicao da funcao
#2o passo é o uso da funcao

#1o passo
def OlaMundo ():
    print('Ola mundo')

#2o passo
OlaMundo()

#Funcao com parametros e uso posicional
#A gente define um parametro apenas dizendo o seu nome
#Nao precisamos definir o tipo do parametro
def Soma (p1, p2):
    total = p1 + p2
    print(total)
print('O total é:', end=' ')
Soma(5,6)

#Funcao com parametros e uso nomeado
def Subtracao(p1, p2,):
    total = p1 - p2
    print(total)
print('Posicional')
print('O total é:', end=' ')
Subtracao(5,6)

print('Nomeado')
print('O total é:', end=' ')
Subtracao(p1=8,p2=5)

print('\n')
#Escopo
#No python e em qualquer linguagem há uma discussão sobre escopo
#O escopo é a VISIBILIDADE da VARIAVEL
#Existem variaveis de ESCOPO GLOBAL e variaveis de ESCOPO LOCAL
#No escopo GLOBAL as variaveis sao definidas no programa principal
clima = 'inverno' #o clima é de escopo global
def MostraClima ():
#percebemos que mesmo DENTRO da FUNCAO conseguimos acesar o valor da variavel CLIMA
    print(f'o clima de hoje é de {clima}')

MostraClima()

#a unica regra é que variavel global NAO PODE estar definida
#DEPOIS DA FUNCAO
#
# def MostraClima2():
# #percebemos que memo DENTRO DA FUNCAO conseguimos acessar o
# #valor da variavel clima
#     print(f'o clima de hoje é de {clima}')
# #Se usarmos a funcao antes de definir a variavel GLOBAL
# #ela apresenta um erro
# clima2 = 'verao'
# MostraClima()
# #Em outras linguagens mesmo definindo a variavel antes da chamada
# #da funcao, ela nao funcionaria
# MostraClima()
# clima2 = 'verao'

#E se nós tivessimos uma variave que fosse definida DENTRO DA FUNCAO?
#Ou seja ESCOPO LOCAL
#Sera que conseguiriamos ver o valor dela no programa principal
def MostraTemperatura():
    temperatura = 13
    print(f'A temperatura hoje é de {temperatura} graus')

MostraTemperatura()

def DefineTemperatura():
    #A variavel aqui tem escopo local
    #Ou seja, nao conseguimos acessar seu valor
    #no programa principal
    temp = 14
#Isso nao funciona
# DefineTemperatura()
# print(f'A temperatura hoje é de {temp} graus')

print('\nRetorno da FUnção')

def Soma2 (p1, p2):
    total = p1 + p2
    return total

#o def permite que usemos direto em outras funcoes
n1 = 8
n2 = 9
print(f'A soma de {n1} e {n2} é {Soma2(n1, n2)}')

def Saudacao (nome, horario):
    if horario == 'manha':
        print(f'Bom dia, {nome}')
    elif horario == 'tarde':
        print(f'Boa tarde, {nome}')
    elif horario == 'noite':
        print(f'Boa noite, {nome}')
    else: print('Erro')
nome = input('Qual seu nome? ').lower()
horario = input('Você está de manhã, tarde ou noite? ')
Saudacao(nome, horario)
