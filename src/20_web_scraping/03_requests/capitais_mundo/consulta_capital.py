# Função para consultar a capital de um país em um arquivo de texto
def consultar_capital(nome_arquivo, pais_consultado):
    # Abre o arquivo no modo de leitura
    with open(nome_arquivo, 'r', encoding='latin1') as file:
        # Itera sobre cada linha do arquivo
        for linha in file:
            partes = linha.strip().split(":")  # Divide a linha em país e capital usando ':' como delimitador
            if len(partes) == 2:  # Verifica se a linha contém exatamente dois elementos
                pais = partes[0].strip()  # Remove espaços em branco extras e obtém o nome do país
                capital = partes[1].strip()  # Remove espaços em branco extras e obtém o nome da capital
                if pais.lower() == pais_consultado.lower():  # Compara o país consultado (ignorando maiúsculas/minúsculas)
                    return capital  # Retorna a capital se o país for encontrado
        # Se o país não for encontrado, retorna None
        return None

# Exemplo de uso
nome_arquivo = "paises.txt"  # Nome do arquivo a ser consultado
pais_consultado = input("Digite o nome do país para consultar a capital: ")  # Solicita o nome do país ao usuário
capital = consultar_capital(nome_arquivo, pais_consultado)  # Chama a função para consultar a capital

if capital:
    print(f"A capital {pais_consultado} é {capital}.")
else:
    print(f"Não foi encontrada a capital para o país {pais_consultado}.")