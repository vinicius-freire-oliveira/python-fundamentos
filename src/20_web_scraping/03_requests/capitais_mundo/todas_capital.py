# Função para processar um arquivo de texto contendo pares de país e capital
def processar_arquivo_paises(nome_arquivo):
    # Abre o arquivo no modo de leitura
    with open(nome_arquivo, 'r', encoding='latin1') as file:
        # Itera sobre cada linha do arquivo
        for linha in file:
            partes = linha.strip().split(":")  # Divide a linha em país e capital usando ':' como delimitador
            if len(partes) == 2:  # Verifica se a linha contém exatamente dois elementos
                pais = partes[0].strip()  # Remove espaços em branco extras e obtém o nome do país
                capital = partes[1].strip()  # Remove espaços em branco extras e obtém o nome da capital
                print(f"{pais}: {capital}.")  # Imprime o par país-capital
            else:
                print(f"Formato inválido na linha: {linha.strip()}")  # Se o formato for inválido, imprime uma mensagem de erro

# Exemplo de uso
nome_arquivo = "paises.txt"  # Nome do arquivo a ser processado
processar_arquivo_paises(nome_arquivo)  # Chama a função para processar o arquivo


