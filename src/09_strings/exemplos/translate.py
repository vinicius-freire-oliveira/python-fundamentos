# Retorna uma cópia da string em que todos os caracteres foram mapeados usando a tabela de mapeamento criada com maketrans().
tabela = str.maketrans("abc", "123")
texto = "abc"
print(texto.translate(tabela))  # Saída: '123'
