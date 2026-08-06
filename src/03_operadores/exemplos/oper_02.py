# Operador *
# Definindo uma função que aceita um número variável de argumentos
def soma(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

# Chamando a função com diferentes números de argumentos
print(soma(1, 2, 3))  # Saída: 6
print(soma(4, 5, 6, 7))  # Saída: 22
print(soma(8, 9))  # Saída: 17