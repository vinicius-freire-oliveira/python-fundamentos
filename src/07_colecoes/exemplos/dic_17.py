usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

print(len(assistiram))

print(set(assistiram))

print(set([1,2,3,1]))

print({4, 1,2,3,1})

print(type({1,2}))

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_machine_learning)

#print(usuarios_machine_learning[3])

for usuario in set(assistiram):
  print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science | usuarios_machine_learning)

print(usuarios_data_science & usuarios_machine_learning)

print(usuarios_data_science - usuarios_machine_learning)

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
print(15 in fez_ds_mas_nao_fez_ml)

print(23 in fez_ds_mas_nao_fez_ml)

print(usuarios_data_science ^ usuarios_machine_learning)

usuarios = {1,5,76,34,52,13,17}
print(len(usuarios))

usuarios.add(13)
print(len(usuarios))

usuarios.add(765)
print(len(usuarios))

print(usuarios)

usuarios = frozenset(usuarios)
print(usuarios)

print(type(usuarios))

#print(usuarios.add(134))

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
print(meu_texto.split())

print(set(meu_texto.split()))

"""# Dicionário (Mapa etc)"""

"""aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

print(type(aparicoes))

print(aparicoes["Guilherme"])

print(aparicoes["cachorro"])

#print(aparicoes["xpto"])

print(aparicoes.get("xpto", 0))

print(aparicoes.get("cachorro", 0))

aparicoes = dict(Guilherme = 2, cachorro = 1)
print(aparicoes)"""

aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

aparicoes["Carlos"] = 1

print(aparicoes)

aparicoes["Carlos"] = 2

print(aparicoes)

del aparicoes["Carlos"]

print(aparicoes)

print("cachorro" in aparicoes)

print("Carlos" in aparicoes)

for elemento in aparicoes:
  print(elemento)

for elemento in aparicoes.keys():
  print(elemento)

for elemento in aparicoes.values():
  print(elemento)

print(1 in aparicoes.values())

for elemento in aparicoes.keys():
  valor = aparicoes[elemento]
  print(elemento, valor)

for elemento in aparicoes.items():
  print(elemento)

for chave, valor in aparicoes.items():
  print(chave, "=", valor)

print(["palavra {}".format(chave) for chave in aparicoes.keys()])

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
  ate_agora = aparicoes.get(palavra, 0)
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)

# Importa a classe defaultdict do módulo collections
from collections import defaultdict

# Cria um defaultdict chamado 'aparicoes' que retorna 0 quando uma nova chave é acessada
aparicoes = defaultdict(int)

# Suponha que 'meu_texto' é uma string contendo o texto que queremos analisar
meu_texto = "este é um exemplo de texto com várias palavras este é um texto de exemplo"

# Itera sobre cada palavra no texto dividido em palavras
for palavra in meu_texto.split():
    # Obtém o número atual de aparições da palavra (inicialmente 0 se a palavra não foi vista antes)
    ate_agora = aparicoes[palavra]
    # Atualiza o número de aparições da palavra, incrementando-o em 1
    aparicoes[palavra] = ate_agora + 1

# Imprime o dicionário de aparições de palavras
print(aparicoes)

# Imprime o valor padrão retornado por int() que é 0
print(int())

# Cria um defaultdict chamado 'dicionario' que retorna 0 quando uma nova chave é acessada
dicionario = defaultdict(int)
# Acessa a chave 'guilherme' no dicionário, que ainda não foi definida, então retorna 0
print(dicionario['guilherme'])

# Define o valor da chave 'guilherme' como 15
dicionario['guilherme'] = 15
# Acessa a chave 'guilherme' no dicionário, que agora possui o valor 15
print(dicionario['guilherme'])

