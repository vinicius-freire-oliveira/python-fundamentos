n = int(input("Número: "))

# Inicializa a variável fact como 1
fact = 1

# Loop para calcular o fatorial
for i in range(1, n + 1): 
    fact = fact * i 

# Imprime o resultado do fatorial
print("O fatorial de {} é: {}".format(n, fact), end="")
