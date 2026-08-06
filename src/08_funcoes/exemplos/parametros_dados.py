import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados

# URL do arquivo CSV que contém os dados do SUS
url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/dados_sus.csv'

# Lê os dados do arquivo CSV para um dataframe Pandas
# Parâmetros utilizados:
# - encoding='ISO-8859-1': Especifica o encoding do arquivo como ISO-8859-1 (também conhecido como Latin-1)
# - sep=';': Especifica o separador como ponto e vírgula (;)
# - skiprows=3: Pula as 3 primeiras linhas do arquivo
# - skipfooter=9: Pula as 9 últimas linhas do arquivo (necessário o uso de 'engine'='python' para suportar 'skipfooter')
dados = pd.read_csv(url, encoding='ISO-8859-1', sep=';', skiprows=3, skipfooter=9, engine='python')

# Imprime os dados carregados do arquivo CSV
print(dados)
