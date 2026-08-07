import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados

# Extrai a tabela HTML da Wikipedia que contém informações sobre países por população
dados = pd.read_html('https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o')[0]

# Imprime os dados extraídos da tabela HTML
print(dados)
