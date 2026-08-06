idades = [39, 18, 15, 27]

# Essa linha verifica se o valor 28 está presente na lista "idades". O resultado será "False", pois 28 não está na lista.
""" print(28 in idades)

# Essa linha verifica se o valor 15 está presente na lista "idades". O resultado será "True", pois 15 está na lista.
print(15 in idades)

# Nesse trecho, é verificado se o valor 15 está na lista "idades". Como está presente, o valor 15 é removido da lista.
if 15 in idades:
    idades.remove(15)

print(idades) """

# Nesse trecho, é verificado se o valor 28 está na lista "idades". Como não está presente, esse bloco de código será ignorado e não haverá alterações na lista.
if 28 in idades:
    idades.remove(28)

print(idades)

idades.append(19)
print(idades)

""" # Essa linha insere o valor 20 na posição 0 da lista "idades".
idades.insert(0, 20)
print(idades)

idades = [20, 39, 18]
print(idades)

# Essa linha adiciona uma lista [27, 19] como um único elemento à lista "idades".
idades.append([27, 19])

print(idades)

# Este é um loop "for" que percorre cada elemento da lista "idades" e imprime uma mensagem para cada elemento.
for elemento in idades:
    print("Recebi o elemento", elemento)

''' Neste trecho, a lista "idades" é redefinida novamente com os valores [20, 39, 18]. Em seguida, a função "extend()" é usada para adicionar os elementos da lista [27, 19] à lista "idades". O resultado será [20, 39, 18, 27, 19].'''
idades = [20, 39, 18]
idades.extend([27,19])
print(idades)

'''Este é um loop "for" que percorre cada elemento da lista "idades" e imprime o elemento incrementado em 1.'''
for idade in idades:
    print(idade + 1)

''' Neste trecho, é usada uma lista de compreensão para criar a lista "idades_no_ano_que_vem". A lista de compreensão percorre cada elemento da lista "idades" e incrementa cada elemento em 1, criando uma nova lista com os resultados. O resultado será o mesmo que o trecho anterior: [21, 40, 19, 28, 20].'''
idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)
print(idades_no_ano_que_vem)

#Obtém o mesmo resultado do comando da parte superior
idades_no_ano_que_vem = [idade+1 for idade in idades]
print(idades_no_ano_que_vem)

''' Neste trecho, é usada uma lista de compreensão para criar a lista "idades_no_ano_que_vem". A lista de compreensão percorre cada elemento da lista "idades" e adiciona apenas os elementos maiores que 21 à nova lista. O resultado será [39, 27].'''
idades_no_ano_que_vem = [idade for idade in idades if idade > 21]

print(idades_no_ano_que_vem)

def proximo_ano(idade):
    return idade+1

''' A cada elemento da lista "idades" que é maior que 21, o resultado é uma nova lista com as idades maiores que 21 incrementadas em 1. No caso da lista "idades", o resultado será [40, 28].'''
print([proximo_ano(idade) for idade in idades if idade > 21])
 """