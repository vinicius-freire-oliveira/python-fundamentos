# Lista inicial
lista = [24, 10, 16]

# Lista que será populada com tuplas contendo índice e valor correspondente da lista inicial
lista_de_tuplas = []

# Loop sobre os índices da lista inicial
for i in range(len(lista)):
    # Cria uma tupla com o índice i e o valor lista[i], e adiciona à lista_de_tuplas
    lista_de_tuplas.append((i, lista[i]))

# Imprime a lista de tuplas resultante
print(lista_de_tuplas)
