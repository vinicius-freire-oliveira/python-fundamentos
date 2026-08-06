# Define uma lista de frutas
frutas = ["maçã", "banana", "laranja", "melancia"]

# Cria uma lista vazia chamada 'lista'
lista = []

# Itera sobre cada fruta na lista 'frutas'
for fruta in frutas:
    # Converte cada fruta para letras maiúsculas usando o método upper() e adiciona à lista 'lista'
    lista.append(fruta.upper())

# Imprime a lista 'lista', que agora contém as frutas em letras maiúsculas
print(lista)

# Outra maneira de criar a lista 'lista' com as frutas em letras maiúsculas usando uma list comprehension
lista = [fruta.upper() for fruta in frutas]

# Imprime a lista 'lista' novamente para demonstrar o mesmo resultado
print(lista)
