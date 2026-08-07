# Converte a string para minúsculas, de forma mais agressiva do que lower(), especialmente útil para comparações sem considerar maiúsculas e minúsculas.
texto = "Groß"
print(texto.casefold())  # Saída: 'gross'
