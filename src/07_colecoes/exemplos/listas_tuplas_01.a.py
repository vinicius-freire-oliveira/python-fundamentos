# Definição das idades de quatro pessoas
idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

# Imprime cada idade individualmente
print(idade1)
print(idade2)
print(idade3)
print(idade4)

# Cria uma lista de idades
idades = [39, 30, 27, 18]

# Imprime o tipo da variável "idades"
print(type(idades))

# Imprime o número de elementos na lista "idades"
print(len(idades))

# Acessa e imprime o primeiro elemento da lista "idades"
print(idades[0])

# Imprime a lista completa de idades
print(idades)

# Acessa e imprime elementos individuais da lista "idades"
print(idades[1])
print(idades[2])
print(idades[3])

# Adiciona o valor 15 ao final da lista "idades"
idades.append(15)

# Imprime o novo último elemento da lista "idades"
print(idades[4])

# Itera sobre a lista "idades" e imprime cada elemento
for idade in idades:
    print(idade)

# Remove o valor 30 da lista "idades" e imprime o resultado da operação (None porque remove() retorna None)
print(idades.remove(30))

# Imprime a lista "idades" após a remoção do valor 30
print(idades)

# Tenta remover novamente o valor 30 da lista "idades", o que não é possível pois ele já foi removido anteriormente
# Esta linha está comentada para evitar um erro
# print(idades.remove(30))

# Adiciona o valor 15 novamente ao final da lista "idades" e imprime a lista atualizada
print(idades.append(15))
print(idades)

# Remove o valor 15 da lista "idades" e imprime o resultado da operação
print(idades.remove(15))

# Imprime a lista "idades" após a remoção do valor 15
print(idades)

# Adiciona o valor 27 novamente ao final da lista "idades" e remove o primeiro valor 27 encontrado na lista
# A operação remove apenas o primeiro valor encontrado
print(idades.append(27))
print(idades.remove(27))

# Imprime a lista "idades" após a remoção do primeiro valor 27 encontrado
print(idades)
