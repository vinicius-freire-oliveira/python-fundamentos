import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados

# ID da planilha do Google Sheets
sheet_id = '1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw'

# URL para fazer o download da planilha como um arquivo CSV
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'

# Lê os dados da planilha do Google Sheets e cria um dataframe 'dados'
dados = pd.read_csv(url)

# Imprime o dataframe 'dados'
print(dados)

# Salva os dados do dataframe em um arquivo CSV local
dados.to_csv('dados_emissoes_co2.csv', index=False)

# Imprime novamente o dataframe 'dados', que agora inclui as modificações feitas
print(dados)
