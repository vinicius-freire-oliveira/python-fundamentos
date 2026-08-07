# Divide a string em uma tupla com três elementos, similar a partition(), mas divide da direita para a esquerda.
texto = "primeira segunda terceira"
print(texto.rpartition(" "))  # Saída: ('primeira segunda', ' ', 'terceira')
