import pandas as pd
import matplotlib.pyplot as plt

# URL da base de dados CSV
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Carrega os dados do CSV na variável 'dados'
dados = pd.read_csv(url, sep=';')

# Lista de tipos de imóveis comerciais a serem removidos
imoveis_comerciais = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']
                      
# Remove imóveis comerciais da base de dados
df = dados.query('@imoveis_comerciais not in Tipo')

# Seleciona apenas imóveis do tipo "Apartamento"
df = df.query('Tipo == "Apartamento"')

# Visualiza as primeiras linhas da base de dados filtrada
print(df.head())

# Calcula e imprime a média do número de quartos dos apartamentos
print(df['Quartos'].mean())

# Calcula e imprime o número de bairros únicos na base de dados
print(len(df['Bairro'].unique()))

# Alternativa para calcular e imprimir o número de bairros únicos
print(df['Bairro'].nunique())

# Agrupa os dados por bairro e calcula a média dos valores de aluguel,
# em seguida, ordena os bairros pelo valor médio do aluguel
print(df.groupby('Bairro')[['Valor']].mean().sort_values('Valor'))

# Exibe os 5 bairros com os menores valores médios de aluguel
print(df.groupby('Bairro')[['Valor']].mean().sort_values('Valor').head())

# Salva os 5 bairros com os menores valores médios de aluguel em um DataFrame
df_bairros = df.groupby('Bairro')[['Valor']].mean().sort_values('Valor').head()

# Plota um gráfico de barras horizontais dos 5 bairros com menores valores médios de aluguel
df_bairros.plot(kind='barh', figsize=(14, 10), color='blue')

# Mostra o gráfico
plt.show()
