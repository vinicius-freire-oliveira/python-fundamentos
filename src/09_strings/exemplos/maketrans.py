# Cria uma tabela de mapeamento para ser usada com translate().
tabela = str.maketrans("abc", "123")
texto = "abc"
print(texto.translate(tabela))  # Saída: '123'
