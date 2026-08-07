# Exemplo de uso do método rfind

texto = "Este é um exemplo de um texto de exemplo."

# Procurando a última ocorrência da substring "exemplo"
indice = texto.rfind("exemplo")

print("Texto original:", texto)
print("Última ocorrência de 'exemplo' está no índice:", indice)

# Usando o índice para extrair a parte da string a partir da última ocorrência
if indice != -1:
    print("Texto a partir da última ocorrência de 'exemplo':", texto[indice:])
else:
    print("A substring 'exemplo' não foi encontrada.")
