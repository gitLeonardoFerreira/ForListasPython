""""Gerar uma matriz 4x3 que armazene nomes aleatorios"""
import faker
pessoa = faker.Faker('pt-BR')
print(pessoa.name())

matriz = []
pessoas = []
for linha in range(4):
    for coluna in range(3):
        pessoas.append(pessoa.name())
    matriz.append(linha)
print(matriz)