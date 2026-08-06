"""# Dicionário (Mapa etc)"""
# Criação de um dicionário chamado "aparicoes" que associa algumas palavras a suas respectivas contagens.
aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

print(type(aparicoes))  # Resultado: <class 'dict'>

# Acessa o valor associado à chave "Guilherme" no dicionário "aparicoes" e imprime.
print(aparicoes["Guilherme"])  # Resultado: 1

print(aparicoes["cachorro"])  # Resultado: 2

# Tentativa de acessar o valor associado à chave "xpto" no dicionário "aparicoes".
# Como "xpto" não é uma chave válida, o método get() retorna o valor 0 (segundo argumento).
print(aparicoes.get("xpto", 0))  # Resultado: 0

# Acessa o valor associado à chave "cachorro" no dicionário "aparicoes" usando o método get().
# Como "cachorro" é uma chave válida, o método get() retorna o valor associado (2).
print(aparicoes.get("cachorro", 0))  # Resultado: 2

# Redefine o dicionário "aparicoes" com novos valores usando a função dict() com a sintaxe de atribuição.
aparicoes = dict(Guilherme=2, cachorro=1)
print(aparicoes)
