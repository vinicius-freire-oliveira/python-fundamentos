# Criação de um dicionário chamado "aparicoes" que associa algumas palavras a suas respectivas contagens.
aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

# Adiciona um novo par de chave-valor ao dicionário, associando "Carlos" à contagem 1.
aparicoes["Carlos"] = 1

print(aparicoes)

# Atualiza o valor associado à chave "Carlos" no dicionário para 2.
aparicoes["Carlos"] = 2

print(aparicoes)

# Remove o elemento com a chave "Carlos" do dicionário.
del aparicoes["Carlos"]

print(aparicoes)

# Resultado: True, pois a chave "cachorro" está presente no dicionário.
print("cachorro" in aparicoes)

# Resultado: False, pois a chave "Carlos" não está presente no dicionário.
print("Carlos" in aparicoes)

# Loop que itera sobre as chaves do dicionário "aparicoes" e imprime cada chave.
for elemento in aparicoes:
    print(elemento)

# Outra forma de fazer o mesmo loop, mas especificando explicitamente o uso do método keys().
for elemento in aparicoes.keys():
    print(elemento)

# Loop que itera sobre os valores do dicionário "aparicoes" e imprime cada valor.
for elemento in aparicoes.values():
    print(elemento)

# Verifica se o valor 1 está presente nos valores do dicionário "aparicoes".
# Resultado: True, pois o valor 1 está presente (a contagem de "Guilherme" e "vindo").
print(1 in aparicoes.values())

# Loop que itera sobre as chaves do dicionário "aparicoes" e imprime cada chave e seu valor associado.
for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)

# Loop que itera sobre os itens do dicionário "aparicoes" (pares de chave-valor) e imprime cada item como uma tupla.
# Resultado: ('Guilherme', 1), ('cachorro', 2), ('nome', 2), ('vindo', 1), ('Carlos', 2)
for elemento in aparicoes.items():
    print(elemento)

# Loop que itera sobre os itens do dicionário "aparicoes" e imprime cada chave e valor separadamente com "=" entre a chave e o valor
for chave, valor in aparicoes.items():
    print(chave, "=", valor)

# Cria uma lista contendo strings formatadas com as chaves do dicionário.
# Resultado: ['palavra Guilherme', 'palavra cachorro', 'palavra nome', 'palavra vindo', 'palavra Carlos']
print(["palavra {}".format(chave) for chave in aparicoes.keys()])
