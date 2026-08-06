# Nesse bloco, é criada uma lista de idades e são feitas iterações sobre ela utilizando range, enumerate, e desempacotamento de tuplas para obter os índices e idades.
idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
  print(i, idades[i])

print(range(len(idades))) # lazy...

print(enumerate(idades)) # lazy

print(list(range(len(idades)))) # forcei a geração dos valores

print(list(enumerate(idades)))

for indice, idade in enumerate(idades): # unpacking da nossa tupla
  print(indice, "x", idade)

""" Neste trecho, temos uma lista de tuplas chamada "usuarios", contendo informações de nomes, idades e anos de nascimento. Em seguida, são feitas iterações para imprimir apenas os nomes e ignorar o resto das informações das tuplas. """
usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios: # ja desempacotando
  print(nome)

for nome, _, _ in usuarios: # ja desempacotando, ignorando o resto
  print(nome)