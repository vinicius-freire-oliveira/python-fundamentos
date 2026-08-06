usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()

# Adiciona os elementos da lista usuarios_machine_learning na lista assistiram.
assistiram.extend(usuarios_machine_learning)

print(assistiram)

print(len(assistiram))

# Transforma a lista assistiram em um conjunto para eliminar elementos duplicados
print(set(assistiram))

# Demonstra que um conjunto não aceita elementos duplicados ao criar um conjunto a partir de uma lista com elementos duplicados.
print(set([1,2,3,1]))

print({4, 1,2,3,1})

print(type({1,2}))

# como conjuntos (sets) em vez de listas (utiliza chaves {} para definir um conjunto).
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_machine_learning)

# Tenta acessar o elemento no índice 3 do conjunto usuarios_machine_learning,
# mas conjuntos não são indexados, então isso gerará um erro.
# Comentado para evitar o erro durante a execução.
# usuarios_machine_learning[3]

# Utiliza um loop para percorrer o conjunto de elementos assistiram,
# já convertido para um conjunto, removendo elementos duplicados.
# Imprime cada usuário presente no conjunto assistiram.
for usuario in set(assistiram):
    print(usuario)

# Realiza a união dos dois conjuntos usuarios_data_science e usuarios_machine_learning
# utilizando o operador "|" e imprime o conjunto resultante, que conterá todos os elementos
# de ambos os conjuntos, eliminando duplicatas.
print(usuarios_data_science | usuarios_machine_learning)
