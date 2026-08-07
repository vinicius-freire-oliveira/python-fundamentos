import os  # Importa o módulo os para interagir com o sistema operacional

# Define o diretório raiz onde estão as pastas dos soundtracks
diretorio_raiz = r'definir aqui o diretório'

# Define o nome do arquivo de saída que conterá a listagem dos soundtracks
arquivo_saida = 'listagem_soundtracks.txt'

# Obtém a lista de subpastas dentro do diretório raiz que contêm os soundtracks
subpastas = [subpasta for subpasta in os.listdir(diretorio_raiz) if os.path.isdir(os.path.join(diretorio_raiz, subpasta))]

# Ordena as subpastas em ordem alfabética
subpastas.sort()

# Abre o arquivo de saída no modo de escrita
with open(arquivo_saida, 'w') as arquivo:
    # Itera sobre cada subpasta na lista de subpastas
    for subpasta in subpastas:
        # Escreve o nome da subpasta (soundtrack) no arquivo de saída seguido por uma quebra de linha
        arquivo.write(subpasta + '\n')

# Imprime uma mensagem indicando que o arquivo de saída foi criado com sucesso
print(f'Arquivo "{arquivo_saida}" criado com sucesso.')
