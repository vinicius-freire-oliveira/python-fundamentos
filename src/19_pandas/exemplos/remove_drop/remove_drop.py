import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados

# Cria um dataframe 'dados' com informações sobre preços de produtos em diferentes locais
dados = pd.DataFrame([
    ['Feira', 'Cebola', 2.5],
    ['Mercado', 'Cebola', 1.99],
    ['Supermercado', 'Cebola', 1.69],
    ['Feira', 'Tomate', 4],
    ['Mercado', 'Tomate', 3.29],
    ['Supermercado', 'Tomate', 2.99],
    ['Feira', 'Batata', 4.2],
    ['Mercado', 'Batata', 3.99],
    ['Supermercado', 'Batata', 3.69]
], columns=['Local', 'Produto', 'Preço'])

print(dados)  # Imprime o dataframe 'dados'

# Remove linhas específicas do dataframe 'dados' com base nos índices especificados
dados.drop([2, 5, 8], axis=0, inplace=True)

print(dados)  # Imprime o dataframe 'dados' após a remoção das linhas
