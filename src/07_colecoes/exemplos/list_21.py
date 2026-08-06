idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39, 30, 27, 18]

print(type(idades))

print(len(idades))

print(idades[0])

print(idades)

print(idades[1])
print(idades[2])
print(idades[3])

idades.append(15)

print(idades)

print(idades[4])

#print(idades[5]) A lista tem apenas cinco elementos (índices válidos de 0 a 4), isso resultará em um erro.

for idade in idades:
    print(idade)

print(idades.remove(30))

print(idades)

#print(idades.remove(30)) Essa linha tenta remover novamente o valor 30 da lista "idades", mas como ele já foi removido anteriormente, isso causará um erro e não terá efeito.

print(idades.append(15))

print(idades)

print(idades.remove(15))

print(idades)
print(idades.append(27))
print(idades.remove(27))
print(idades)