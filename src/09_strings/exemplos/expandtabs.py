# Substitui os caracteres de tabulação ('\t') na string por espaços, com um número específico de espaços (padrão é 8).
texto = "um\tdois\ttres"
print(texto.expandtabs(4))  # Saída: 'um  dois    tres'
