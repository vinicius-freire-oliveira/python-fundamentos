# Exemplo 1: Adição composta
a = 5
a += 3  # Equivalente a a = a + 3
print(a)  # Saída: 8

# Exemplo 2: Subtração composta
b = 10
b -= 4  # Equivalente a b = b - 4
print(b)  # Saída: 6

# Exemplo 3: Multiplicação composta
c = 7
c *= 2  # Equivalente a c = c * 2
print(c)  # Saída: 14

# Exemplo 4: Divisão composta
d = 20
d /= 4  # Equivalente a d = d / 4
print(d)  # Saída: 5.0

# Exemplo 5: Divisão inteira composta
e = 15
e //= 2  # Equivalente a e = e // 2
print(e)  # Saída: 7

# Exemplo 6: Módulo composto
f = 9
f %= 4  # Equivalente a f = f % 4
print(f)  # Saída: 1

# Exemplo 7: Exponenciação composta
g = 3
g **= 2  # Equivalente a g = g ** 2
print(g)  # Saída: 9

# Exemplo 8: E bit a bit composto
h = 0b1010  # 10 em decimal
h &= 0b1100  # Equivalente a h = h & 0b1100
print(bin(h))  # Saída: 0b1000 (8 em decimal)

# Exemplo 9: Ou bit a bit composto
i = 0b1010  # 10 em decimal
i |= 0b1100  # Equivalente a i = i | 0b1100
print(bin(i))  # Saída: 0b1110 (14 em decimal)

# Exemplo 10: Ou exclusivo bit a bit composto
j = 0b1010  # 10 em decimal
j ^= 0b1100  # Equivalente a j = j ^ 0b1100
print(bin(j))  # Saída: 0b0110 (6 em decimal)

# Exemplo 11: Deslocamento à esquerda composto
k = 0b1010  # 10 em decimal
k <<= 2  # Equivalente a k = k << 2
print(bin(k))  # Saída: 0b101000 (40 em decimal)

# Exemplo 12: Deslocamento à direita composto
l = 0b1010  # 10 em decimal
l >>= 2  # Equivalente a l = l >> 2
print(bin(l))  # Saída: 0b10 (2 em decimal)
