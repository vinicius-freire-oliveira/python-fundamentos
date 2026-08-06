usuarios = {1, 5, 76, 34, 52, 13, 17}

print(len(usuarios))  # Resultado: 7

# Como o 13 já está presente no conjunto, a operação não adiciona um novo elemento.
usuarios.add(13)
print(len(usuarios))  # Resultado: 7

usuarios.add(765)
print(len(usuarios))  # Resultado: 8

print(usuarios)

# Converte o conjunto "usuarios" em um frozenset (conjunto imutável).
usuarios = frozenset(usuarios)
print(usuarios)

print(type(usuarios))  # Resultado: <class 'frozenset'>

# Tentativa de adicionar o elemento 134 ao conjunto "usuarios" após a conversão para frozenset.
# Isso causará um erro, pois um frozenset é imutável e não permite adição de elementos.
# O código está comentado para evitar o erro.
# usuarios.add(134)

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"

# Divide a string "meu_texto" em palavras utilizando o método split().
# O resultado é uma lista contendo as palavras separadas da string original.
print(meu_texto.split())

# Converte a lista de palavras em um conjunto utilizando a função set().
# Isso removerá as duplicatas, pois conjuntos não aceitam elementos repetidos.
print(set(meu_texto.split()))
