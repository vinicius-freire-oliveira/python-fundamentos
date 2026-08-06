# Copiar lista
L = [6,7,8,9]
V = L[:]
Z = list(L)

print(L, V, Z)
V[0] = -100
Z[0] = -8
print(L, V, Z)