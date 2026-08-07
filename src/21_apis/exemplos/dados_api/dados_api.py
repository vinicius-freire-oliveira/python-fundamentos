import requests  # Importa a biblioteca requests para fazer requisições HTTP
import json  # Importa a biblioteca json para lidar com dados JSON

# Faz uma requisição GET para a API que retorna informações sobre frutas
dados_frutas = requests.get('https://fruityvice.com/api/fruit/all')

# Converte a resposta da requisição para JSON
resultado = json.loads(dados_frutas.text)

import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados

# Normaliza os dados JSON e cria um dataframe com Pandas
dados_frutas_normalizado = pd.json_normalize(resultado)

# Imprime o dataframe 'dados_frutas_normalizado'
print(dados_frutas_normalizado)
