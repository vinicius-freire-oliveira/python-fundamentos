# Importa a biblioteca pandas para manipulação de dados
import pandas as pd

# Lê o arquivo JSON 'pacientes.json' e carrega os dados em um DataFrame
dados_pacientes = pd.read_json('pacientes.json')

# Imprime o DataFrame 'dados_pacientes', exibindo os dados do arquivo JSON
print(dados_pacientes)

# Lê o arquivo JSON 'pacientes_2.json' e carrega os dados em um DataFrame
dados_pacientes_2 = pd.read_json('pacientes_2.json')

# Imprime o DataFrame 'dados_pacientes_2', exibindo os dados do segundo arquivo JSON
print(dados_pacientes_2)

# Normaliza os dados da coluna 'Pacientes' do DataFrame 'dados_pacientes_2' em um novo DataFrame 'df_normalizado'
df_normalizado = pd.json_normalize(dados_pacientes_2['Pacientes'])

# Imprime o DataFrame 'df_normalizado', que contém os dados normalizados
print(df_normalizado)

# Converte o DataFrame 'df_normalizado' de volta para JSON e salva como 'historico_pacientes_norm.json'
df_normalizado.to_json('historico_pacientes_norm.json')

# Lê o arquivo JSON 'historico_pacientes_norm.json' e imprime seu conteúdo
print(pd.read_json('historico_pacientes_norm.json'))
