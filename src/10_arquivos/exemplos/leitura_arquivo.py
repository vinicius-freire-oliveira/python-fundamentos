# Abre o arquivo 'frutas.txt' no modo de leitura ('r') e atribui o objeto de arquivo a 'arquivo'
arquivo = open('frutas.txt', 'r')

# Lê a primeira linha do arquivo e armazena em 'linha', e imprime essa linha
linha = arquivo.readline()
print(linha)

# Lê a próxima linha do arquivo e imprime essa linha
linha = arquivo.readline()
print(linha)

# Fecha o arquivo 'frutas.txt'
arquivo.close()

# Reabre o arquivo 'frutas.txt' no modo de leitura ('r') e atribui o objeto de arquivo a 'arquivo'
arquivo = open('frutas.txt', 'r')

# Lê todo o conteúdo do arquivo e armazena em 'conteudo', e imprime esse conteúdo
conteudo = arquivo.read()
print(conteudo)

# Tenta ler novamente o conteúdo do arquivo, mas como o arquivo já foi lido completamente, não há mais conteúdo para ler,
# portanto, 'conteudo' será uma string vazia e será impresso como tal
conteudo = arquivo.read()
print(conteudo)

# Fecha o arquivo 'frutas.txt' novamente
arquivo.close()



