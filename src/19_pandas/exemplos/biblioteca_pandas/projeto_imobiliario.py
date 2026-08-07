import pandas as pd
import matplotlib.pyplot as plt

# Carrega o arquivo CSV de aluguel de imóveis da URL especificada
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Carrega o DataFrame e imprime o conteúdo para visualização
print(pd.read_csv(url))

# Carrega o DataFrame especificando o delimitador ';' e imprime o conteúdo
print(pd.read_csv(url, sep=';'))

# Armazena o DataFrame na variável 'dados'
dados = pd.read_csv(url, sep=';')
print(dados)

# Imprime as primeiras 10 linhas do DataFrame
print(dados.head(10))

# Imprime as últimas linhas do DataFrame
print(dados.tail())

# Verifica o tipo de 'dados'
print(type(dados))

# Imprime a forma (número de linhas e colunas) do DataFrame
print(dados.shape)

# Imprime os nomes das colunas do DataFrame
print(dados.columns)

# Imprime informações sobre o DataFrame, como número de entradas, tipos de dados e valores nulos
print(dados.info())

# Imprime a coluna 'Tipo'
print(dados['Tipo'])

# Imprime as colunas 'Quartos' e 'Valor'
print(dados[['Quartos', 'Valor']])

# Imprime as primeiras linhas do DataFrame
print(dados.head())

# Calcula e imprime a média da coluna 'Valor'
print(dados['Valor'].mean())

# Agrupa os dados por 'Tipo' e calcula a média para cada tipo
print(dados.groupby('Tipo').mean(numeric_only=True))

# Agrupa os dados por 'Tipo' e calcula a média da coluna 'Valor'
print(dados.groupby('Tipo')['Valor'].mean())

# Agrupa os dados por 'Tipo', calcula a média da coluna 'Valor' e ordena os resultados
print(dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor'))

# Armazena o DataFrame agrupado e ordenado na variável 'df_preco_tipo'
df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

# Cria um gráfico de barras horizontais para 'df_preco_tipo'
df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple')

# Exibe o gráfico
plt.show()

# Imprime os tipos de imóveis únicos na coluna 'Tipo'
print(dados.Tipo.unique())

# Lista de tipos de imóveis comerciais
imoveis_comerciais = ['Conjunto Comercial/Sala', 'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém', 'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial', 'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio', 'Pousada/Chalé', 'Hotel', 'Indústria']

# Imprime os imóveis comerciais presentes no DataFrame
print(dados.query('@imoveis_comerciais in Tipo'))

# Imprime os imóveis que não são comerciais
print(dados.query('@imoveis_comerciais not in Tipo'))

# Filtra o DataFrame para remover imóveis comerciais
df = dados.query('@imoveis_comerciais not in Tipo')
print(df.head())

# Imprime os tipos de imóveis únicos após o filtro
print(df.Tipo.unique())

# Agrupa os dados filtrados por 'Tipo', calcula a média da coluna 'Valor' e ordena os resultados
df_preco_tipo = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

# Cria um gráfico de barras horizontais para 'df_preco_tipo'
df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple')

# Exibe o gráfico
plt.show()

# Imprime os tipos de imóveis únicos após o filtro
print(df.Tipo.unique())

# Imprime a distribuição dos tipos de imóveis no DataFrame como percentual
print(df.Tipo.value_counts(normalize=True))

# Converte a distribuição percentual para um DataFrame e ordena por 'Tipo'
print(df.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo'))

# Armazena a distribuição percentual no DataFrame 'df_percentual_tipo'
df_percentual_tipo = df.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')

# Cria um gráfico de barras para a distribuição percentual
df_percentual_tipo.plot(kind='bar', figsize=(14, 10), color='green',
                        xlabel='Tipos', ylabel='Percentual')

# Exibe o gráfico
plt.show()

# Filtra o DataFrame para mostrar apenas apartamentos
print(df.query('Tipo == "Apartamento"'))

# Atualiza o DataFrame para conter apenas apartamentos
df = df.query('Tipo == "Apartamento"')
print(df.head())

# Verifica se há valores nulos no DataFrame
print(df.isnull())

# Conta o número de valores nulos em cada coluna
print(df.isnull().sum())

# Preenche os valores nulos com 0
print(df.fillna(0))

# Atualiza o DataFrame preenchendo valores nulos com 0
df = df.fillna(0)

# Verifica novamente se há valores nulos após o preenchimento
print(df.isnull().sum())

# Filtra o DataFrame para mostrar registros onde o valor ou condomínio é 0
print(df.query('Valor == 0 | Condominio == 0'))

# Imprime os índices dos registros onde o valor ou condomínio é 0
print(df.query('Valor == 0 | Condominio == 0').index)

# Armazena os índices dos registros a serem removidos
registros_a_remover = df.query('Valor == 0 | Condominio == 0').index

# Remove os registros onde o valor ou condomínio é 0
df.drop(registros_a_remover, axis=0, inplace=True)

# Verifica se os registros foram removidos
print(df.query('Valor == 0 | Condominio == 0'))

# Imprime as primeiras linhas do DataFrame após a remoção dos registros
print(df.head())

# Imprime os tipos de imóveis únicos após a remoção dos registros
print(df.Tipo.unique())

# Remove a coluna 'Tipo' do DataFrame
df.drop('Tipo', axis=1, inplace=True)

# Imprime as primeiras linhas do DataFrame após a remoção da coluna
print(df.head())

# Verifica se há imóveis com 1 quarto
print(df['Quartos'] == 1)

# Armazena a seleção de imóveis com 1 quarto
selecao1 = df['Quartos'] == 1
print(df[selecao1])

# Armazena a seleção de imóveis com valor inferior a 1200
selecao2 = df['Valor'] < 1200
print(df[selecao2])

# Combina as seleções anteriores para selecionar imóveis com 1 quarto e valor inferior a 1200
selecao_final = (selecao1) & (selecao2)
print(df[selecao_final])

# Armazena o DataFrame filtrado na variável 'df_1'
df_1 = df[selecao_final]

# Seleciona imóveis com 2 ou mais quartos, valor inferior a 3000 e área maior que 70
selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)
print(df[selecao])

# Armazena o DataFrame filtrado na variável 'df_2'
df_2 = df[selecao]

# Salva o DataFrame atual em um arquivo CSV
df.to_csv('dados_apartamentos.csv')

# Lê e imprime o conteúdo do arquivo CSV salvo
print(pd.read_csv('dados_apartamentos.csv'))

# Salva o DataFrame atual em um arquivo CSV sem o índice
df.to_csv('dados_apartamentos.csv', index=False)

# Lê e imprime o conteúdo do arquivo CSV salvo sem o índice
print(pd.read_csv('dados_apartamentos.csv'))

# Salva o DataFrame atual em um arquivo CSV sem o índice e com o delimitador ';'
df.to_csv('dados_apartamentos.csv', index=False, sep=';')

# Lê e imprime o conteúdo do arquivo CSV salvo com o delimitador ';'
print(pd.read_csv('dados_apartamentos.csv'))

# Lê e imprime o conteúdo do arquivo CSV salvo com o delimitador ';'
print(pd.read_csv('dados_apartamentos.csv', sep=';'))

# Adiciona uma coluna 'Valor_por_mes' que é a soma do valor do aluguel e do condomínio
dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
print(dados.head())

# Adiciona uma coluna 'Valor_por_ano' que é o valor por mês multiplicado por 12, mais o IPTU
dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']
print(dados.head())

# Adiciona uma coluna 'Descricao' que combina o tipo de imóvel e o bairro
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro']
print(dados.head())

# Adiciona uma coluna 'Descricao' detalhada com tipo de imóvel, bairro, número de quartos e vagas de garagem
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com '  + \
                     dados['Quartos'].astype(str) + ' quarto(s) '  + \
                     ' e '  + dados['Vagas'].astype(str) + ' vaga(s) de garagem.'
print(dados.head())

# Adiciona uma coluna 'Possui_suite' que indica se o imóvel possui suíte
dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")
print(dados.head())

# Salva o DataFrame completo em um arquivo CSV com o delimitador ';'
dados.to_csv('dados_completos_dev.csv', index=False, sep=';')
