import os  # Importa o módulo os para interagir com o sistema operacional

# Define o diretório raiz onde estão as pastas das bandas
diretorio_raiz = r'definir arqui o diretório'

# Define o nome do arquivo de saída que conterá a lista de bandas
arquivo_saida = 'listagem_bandas.txt'

# Obtém a lista de subpastas dentro do diretório raiz
subpastas = [subpasta for subpasta in os.listdir(diretorio_raiz) if os.path.isdir(os.path.join(diretorio_raiz, subpasta))]

# Ordena as subpastas em ordem alfabética
subpastas.sort()

# Abre o arquivo de saída no modo de escrita
with open(arquivo_saida, 'w') as arquivo:
    # Itera sobre cada subpasta na lista de subpastas
    for subpasta in subpastas:
        # Constrói o caminho completo para a subpasta
        caminho_subpasta = os.path.join(diretorio_raiz, subpasta)
        # Obtém uma lista das bandas dentro da subpasta
        bandas = [banda for banda in os.listdir(caminho_subpasta) if os.path.isdir(os.path.join(caminho_subpasta, banda))]
        # Ordena as bandas em ordem alfabética
        bandas.sort()
        
        # Itera sobre cada banda na lista de bandas
        for banda in bandas:
            # Escreve o nome da banda no arquivo de saída seguido por uma quebra de linha
            arquivo.write(f'{banda}\n')

# Imprime uma mensagem indicando que o arquivo de saída foi criado com sucesso
print(f'Arquivo "{arquivo_saida}" criado com sucesso.')
