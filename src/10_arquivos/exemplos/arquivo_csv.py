# Importa a biblioteca pandas, que é usada para manipulação de dados
import pandas as pd

# URL do arquivo CSV a ser lido
url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data.csv'

# Lê o arquivo CSV da URL e armazena os dados em um DataFrame do pandas
dados = pd.read_csv(url)

# Imprime as primeiras 5 linhas do DataFrame 'dados'
print(dados.head())

# URL de outro arquivo CSV a ser lido
url_2 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data_ponto_virgula.csv'

# Lê o arquivo CSV da URL e armazena os dados em um DataFrame do pandas
dados_ponto_virgula = pd.read_csv(url_2)

# Imprime as primeiras 5 linhas do DataFrame 'dados_ponto_virgula'
print(dados_ponto_virgula.head())

# Lê o arquivo CSV da URL usando ponto e vírgula como separador de campos
dados_ponto_virgula = pd.read_csv(url_2, sep=';')

# Imprime todo o DataFrame 'dados_ponto_virgula'
print(dados_ponto_virgula)

# Lê apenas as primeiras 5 linhas do arquivo CSV da URL e armazena os dados em um DataFrame do pandas
dados_primeiras_linhas = pd.read_csv(url, nrows=5)

# Imprime o DataFrame 'dados_primeiras_linhas'
print(dados_primeiras_linhas)

# Lê o arquivo CSV da URL, selecionando apenas as colunas 'Id', 'Year_Birth' e 'Income'
dados_selecao = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income'])

# Imprime o DataFrame 'dados_selecao'
print(dados_selecao)

# Lê o arquivo CSV da URL, selecionando apenas as colunas de índice 0, 1 e 4
dados_selecao = pd.read_csv(url, usecols=[0, 1, 4])

# Imprime o DataFrame 'dados_selecao'
print(dados_selecao)

# Salva o DataFrame 'dados_selecao' em um arquivo CSV chamado 'clientes_mercado.csv'
dados_selecao.to_csv('clientes_mercado.csv')

# Lê o arquivo CSV 'clientes_mercado.csv' e armazena os dados em um DataFrame do pandas
clientes_mercado = pd.read_csv('clientes_mercado.csv')

# Imprime o DataFrame 'clientes_mercado'
print(clientes_mercado)

# Salva o DataFrame 'dados_selecao' em um arquivo CSV chamado 'dados_mercado.csv' sem incluir o índice
dados_selecao.to_csv('dados_mercado.csv', index=False)

# Lê o arquivo CSV 'dados_mercado.csv' e armazena os dados em um DataFrame do pandas
dados_mercado = pd.read_csv('dados_mercado.csv')

# Imprime o DataFrame 'dados_mercado'
print(dados_mercado)
