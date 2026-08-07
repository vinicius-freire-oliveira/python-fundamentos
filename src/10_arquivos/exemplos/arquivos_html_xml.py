# Importa a biblioteca pandas, que é usada para manipulação de dados
import pandas as pd

# Lê todas as tabelas da página HTML 'filmes_wikipedia.html' e as armazena em uma lista de DataFrames
dados_html = pd.read_html('filmes_wikipedia.html')

# Imprime a lista de DataFrames obtida a partir da página HTML
print(dados_html)

# Imprime o tipo da variável 'dados_html', que deve ser uma lista
print(type(dados_html))

# Imprime a quantidade de tabelas encontradas na página HTML
print(len(dados_html))

# Seleciona a segunda tabela (índice 1) da lista de DataFrames
top_filmes = dados_html[1]

# Imprime o DataFrame 'top_filmes'
print(top_filmes)

# Converte o DataFrame 'top_filmes' de volta para um arquivo HTML e salva como 'top_filmes.html'
top_filmes.to_html('top_filmes.html')

# Lê as tabelas do arquivo HTML 'top_filmes.html' e as imprime
print(pd.read_html('top_filmes.html'))

# Converte o DataFrame 'top_filmes' para um arquivo CSV e salva como 'top_filmes_1998.csv' sem incluir o índice
top_filmes.to_csv('top_filmes_1998.csv', index=False)

# Lê o arquivo CSV 'top_filmes_1998.csv' e armazena os dados em um DataFrame
dados = pd.read_csv('top_filmes_1998.csv')

# Imprime as primeiras 5 linhas do DataFrame 'dados'
print(dados.head())

# Lê o arquivo XML 'imdb_top_1000.xml' e armazena os dados em um DataFrame
dados_imdb = pd.read_xml('imdb_top_1000.xml')

# Imprime as primeiras 3 linhas do DataFrame 'dados_imdb'
print(dados_imdb.head(3))

# Converte o DataFrame 'dados_imdb' para um arquivo XML e salva como 'filmes_imdb.xml'
dados_imdb.to_xml('filmes_imdb.xml')
