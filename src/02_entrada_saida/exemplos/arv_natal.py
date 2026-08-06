# Imprime uma estrela centralizada dentro de uma largura de 20 caracteres
print('☆'.center(20)) #center(int) para centralizar a estrela

# Construindo a parte superior da árvore
for i in range(1, 20, 2):
    # Imprime uma linha de asteriscos (*) com um número ímpar de caracteres,
    # centralizada dentro de uma largura de 20 caracteres
    print(('*'*i).center(20))

# Tronco da árvore
for r in range(2):
    # Imprime uma linha contendo duas barras verticais (||) centralizadas dentro de uma largura de 19 caracteres
    print(('||').center(19))

# Base da árvore
# Imprime uma linha contendo a representação de uma base para a árvore,
# centralizada dentro de uma largura de 19 caracteres
print('\====/'.center(19))
print()

# Mensagem final
# Imprime a mensagem desejando um Feliz Natal, seguida por duas quebras de linha
# end='\n\n', há duas quebras de linha depois do texto
print('Feliz Natal e que Jesus ilumine a todos vocês!',end='\n\n')
