num = int(input("Número (3 ou 4 dígitos): "))

a = num // 1 % 10 # último dígito
b = num // 10 % 10 # penúltimo dígito
c = num // 100 % 10 # Antepenúltimo dígito
d = num // 1000 % 100 # primeiro dígito

e = num // 1 % 100 # dois últimos dígitos
f = num // 1 % 1000  # três últimos dígitos

g = num // 100 % 10 # primeiro dígito de 3 dígitos
h = num // 1000 % 10 # primeiro dígito de 4 dígitos

i = num // 10 % 100 # dois primeiros dígitos de uma centena
j = num // 100 % 100 # dois primeiros dígitos de uma milhar
k = num // 10 % 1000 # três primeiros dígitos de uma milhar

l = num // 1 % 1000  # todos os três dígitos 
m = num // 1 % 10000  # todos os quatro dígitos

n = num // 1000 % 10 * 1000 # parte inteira do milhar
o = num // 100 % 10 * 100 # parte inteira da centena

print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}, g = {g},\nh = {h}, i = {i}, j = {j}, k = {k}, l = {l}, m = {m}, n = {n}, o = {o}')

