# Importa a função pow do módulo math
from math import pow

# Solicita ao usuário que digite a base da potência
base = int(input("Digite a base da potência: "))

# Solicita ao usuário que digite o expoente da potência
expoente = int(input("Digite o expoente da potência: "))

# Calcula a potência utilizando a função pow importada e imprime o resultado formatado
print(f"{base} elevado a {expoente} é igual a {pow(base, expoente)}")

