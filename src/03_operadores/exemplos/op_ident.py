# Exemplo 1: Usando o operador is
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, pois b é uma referência a a
print(a is c)  # False, pois c é um novo objeto na memória

# Exemplo 2: Usando o operador is not
x = 42
y = 42
z = 43

print(x is not y)  # False, pois x e y apontam para o mesmo objeto
print(x is not z)  # True, pois x e z são objetos diferentes
