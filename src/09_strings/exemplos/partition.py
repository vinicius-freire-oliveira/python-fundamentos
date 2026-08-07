# Divide a string em uma tupla com três elementos: a parte antes da primeira ocorrência de uma substring, a própria substring, e a parte após a substring.
texto = "frase com separador"
print(texto.partition("com"))  # Saída: ('frase ', 'com', ' separador')
