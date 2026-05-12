from faker import Faker
fake = Faker('pt-BR')

nome = fake.name()
print(nome)
#print(Saudacao('Leticia'))