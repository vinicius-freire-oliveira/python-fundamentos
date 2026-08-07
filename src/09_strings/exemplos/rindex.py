# Exemplo de uso do método rindex

texto = "Este é um exemplo de um texto de exemplo."

try:
    # Procurando a última ocorrência da substring "exemplo"
    indice = texto.rindex("exemplo")
    print("Texto original:", texto)
    print("Última ocorrência de 'exemplo' está no índice:", indice)
    
    # Usando o índice para extrair a parte da string a partir da última ocorrência
    print("Texto a partir da última ocorrência de 'exemplo':", texto[indice:])
except ValueError:
    print("A substring 'exemplo' não foi encontrada.")
