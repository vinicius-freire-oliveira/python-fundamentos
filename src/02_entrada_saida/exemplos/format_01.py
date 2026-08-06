# Solicita ao usuário que insira o nome do hotel, o número de estrelas e o local, armazenando os valores como strings nas variáveis correspondentes.
hotel = str(input("Digite o hotel: "))
estrelas = str(input("Digite número de estrelas: "))
local = str(input("Digite o local: "))

# Imprime uma linha em branco para separar a entrada do usuário da saída formatada.
print("\n")

# Imprime uma linha de asteriscos para separar a informação do hotel.
print("*" * 20)

# Imprime o nome do hotel centralizado em uma linha de asteriscos com uma largura mínima de 20 caracteres.
print("{0:*^20}".format(hotel))

# Imprime o número de estrelas centralizado em uma linha de asteriscos com uma largura mínima de 20 caracteres.
print("{0:*^20}".format(estrelas))

# Imprime o local centralizado em uma linha de asteriscos com uma largura mínima de 20 caracteres.
print("{0:*^20}".format(local))

# Imprime outra linha de asteriscos para separar a informação do hotel.
print("*" * 20)
