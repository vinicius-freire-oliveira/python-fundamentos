idades = [15, 87, 32, 65, 56, 32, 49, 37]
print(idades)

# É utilizada a função "sorted()" para ordenar a lista "idades" em ordem crescente, e o resultado é impresso.
print(sorted(idades))

# É realizada uma comparação entre os valores 15 e 32, que retorna True, pois 15 é menor que 32.
print(15 < 32)

# A função "reversed()" é utilizada para inverter a ordem dos elementos da lista "idades", e em seguida é convertida para uma lista, exibindo o resultado.
print(list(reversed(idades)))

# Aqui é usada novamente a função "sorted()" para ordenar a lista "idades" em ordem decrescente, devido ao parâmetro "reverse=True". O resultado é impresso.
print(sorted(idades, reverse=True))

# A lista "idades" é ordenada em ordem crescente com a função "sorted()", e depois é invertida usando "reversed()" e convertida para uma lista. O resultado é impresso.
print(list(reversed(sorted(idades))))

# A lista original "idades" é impressa novamente para mostrar que não foi modificada pelas operações anteriores.
print(idades)

""" Nesta linha, o método "sort()" é aplicado à lista "idades", que reorganiza a lista em ordem crescente, mas o resultado é None. Isso ocorre porque o método "sort()" modifica a lista in-place e não retorna nenhum valor. Em seguida, a lista "idades" é impressa novamente, agora ordenada em ordem crescente. """
print(idades.sort())

print(idades)