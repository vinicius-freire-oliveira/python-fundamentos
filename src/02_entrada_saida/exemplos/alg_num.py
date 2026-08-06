numero_int = int(input("Digite o número de quatro dígitos: "))

# Calcula e imprime o último algarismo do número inserido.
# Divide o número por 1, converte para string, obtém o último caractere e converte de volta para inteiro.
print(int(str(int(numero_int/1))[-1]))

# Calcula e imprime o penúltimo algarismo do número inserido.
# Divide o número por 10, converte para string, obtém o último caractere e converte de volta para inteiro.
print(int(str(int(numero_int/10))[-1]))

# Calcula e imprime o antepenúltimo algarismo do número inserido.
# Divide o número por 100, converte para string, obtém o último caractere e converte de volta para inteiro.
print(int(str(int(numero_int/100))[-1]))

# Calcula e imprime o primeiro algarismo do número inserido.
# Divide o número por 1000, converte para string, obtém o último caractere e converte de volta para inteiro.
print(int(str(int(numero_int/1000))[-1]))


# O uso de int(str(int(...))) quando recebe um número inteiro do usuário usando input(),
# ele é inicialmente tratado como uma string. Isso ocorre porque o input() retorna uma 
# string, independentemente do que o usuário insira.