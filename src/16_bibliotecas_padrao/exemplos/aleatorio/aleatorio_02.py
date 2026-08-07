from random import randrange

nome = input("Qual o seu nome? ")
# Gerando um token par de 1000 a 9998. O randrange tem o intervalo aberto em 10000, ou seja,
# não considera 10000 como opção de escolha (token >= 1000 e token < 10000)
token = randrange(1000, 10000, 2)

print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!")
