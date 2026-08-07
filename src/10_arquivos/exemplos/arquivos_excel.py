# Importa a biblioteca pandas, que é usada para manipulação de dados
import pandas as pd

# URL do arquivo Excel a ser lido
url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'

# Lê o arquivo Excel da URL e armazena os dados na planilha padrão em um DataFrame do pandas
dados_co2 = pd.read_excel(url)

# Imprime as primeiras 5 linhas do DataFrame 'dados_co2'
print(dados_co2.head())

# Imprime os nomes de todas as planilhas no arquivo Excel
print(pd.ExcelFile(url).sheet_names)

# Lê a planilha 'emissoes_percapita' do arquivo Excel e armazena os dados em um DataFrame do pandas
percapita = pd.read_excel(url, sheet_name='emissoes_percapita')

# Imprime as primeiras 5 linhas do DataFrame 'percapita'
print(percapita.head())

# Lê a planilha 'fontes' do arquivo Excel e armazena os dados em um DataFrame do pandas
fontes = pd.read_excel(url, sheet_name='fontes')

# Imprime as primeiras 5 linhas do DataFrame 'fontes'
print(fontes.head())

# Lê a planilha 'emissoes_C02' do arquivo Excel, selecionando apenas as colunas 'A' até 'D'
intervalo = pd.read_excel(url, sheet_name='emissoes_C02', usecols='A:D')

# Imprime o DataFrame 'intervalo'
print(intervalo)

# Lê as primeiras 10 linhas da planilha 'emissoes_C02', selecionando apenas as colunas 'A' até 'D'
intervalo_2 = pd.read_excel(url, sheet_name='emissoes_C02', usecols='A:D', nrows=10)

# Imprime o DataFrame 'intervalo_2'
print(intervalo_2)

# Salva o DataFrame 'percapita' em um arquivo Excel chamado 'co2_percapita.xlsx' sem incluir o índice
percapita.to_excel('co2_percapita.xlsx', index=False)

# Lê o arquivo Excel 'co2_percapita.xlsx' e armazena os dados em um DataFrame do pandas
print(pd.read_excel('co2_percapita.xlsx'))

# ID da planilha Google Sheets
sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'
# URL base para acessar a planilha Google Sheets em formato CSV
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'

# Lê a planilha Google Sheets e armazena os dados em um DataFrame do pandas
dados_co2_sheets = pd.read_csv(url)

# Imprime o DataFrame 'dados_co2_sheets'
print(dados_co2_sheets)

# Nome da aba da planilha Google Sheets a ser lida
sheet_name = 'emissoes_percapita'
# URL para acessar a aba 'emissoes_percapita' da planilha Google Sheets em formato CSV
url_percapita = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

# Lê a aba 'emissoes_percapita' da planilha Google Sheets e armazena os dados em um DataFrame do pandas
percapita_sheets = pd.read_csv(url_percapita)

# Imprime as primeiras 5 linhas do DataFrame 'percapita_sheets'
print(percapita_sheets.head())

# Nome da aba da planilha Google Sheets a ser lida
sheet_name = 'fontes'
# URL para acessar a aba 'fontes' da planilha Google Sheets em formato CSV
url_fontes = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

# Lê a aba 'fontes' da planilha Google Sheets e armazena os dados em um DataFrame do pandas
fontes_sheets = pd.read_csv(url_fontes)

# Imprime as primeiras 5 linhas do DataFrame 'fontes_sheets'
print(fontes_sheets.head())

# Repete o processo de leitura do arquivo Excel original e impressões

# Lê o arquivo Excel da URL e armazena os dados na planilha padrão em um DataFrame do pandas
dados_co2 = pd.read_excel(url)

# Imprime as primeiras 5 linhas do DataFrame 'dados_co2'
print(dados_co2.head())

# Imprime os nomes de todas as planilhas no arquivo Excel
print(pd.ExcelFile(url).sheet_names)

# Lê a planilha 'emissoes_percapita' do arquivo Excel e armazena os dados em um DataFrame do pandas
percapita = pd.read_excel(url, sheet_name='emissoes_percapita')

# Imprime as primeiras 5 linhas do DataFrame 'percapita'
print(percapita.head())

# Lê a planilha 'fontes' do arquivo Excel e armazena os dados em um DataFrame do pandas
fontes = pd.read_excel(url, sheet_name='fontes')

# Imprime as primeiras 5 linhas do DataFrame 'fontes'
print(fontes.head())

# Lê a planilha 'emissoes_C02' do arquivo Excel, selecionando apenas as colunas 'A' até 'D'
intervalo = pd.read_excel(url, sheet_name='emissoes_C02', usecols='A:D')

# Imprime o DataFrame 'intervalo'
print(intervalo)

# Lê as primeiras 10 linhas da planilha 'emissoes_C02', selecionando apenas as colunas 'A' até 'D'
intervalo_2 = pd.read_excel(url, sheet_name='emissoes_C02', usecols='A:D', nrows=10)

# Imprime o DataFrame 'intervalo_2'
print(intervalo_2)

# Salva o DataFrame 'percapita' em um arquivo Excel chamado 'co2_percapita.xlsx' sem incluir o índice
percapita.to_excel('co2_percapita.xlsx', index=False)

# Lê o arquivo Excel 'co2_percapita.xlsx' e armazena os dados em um DataFrame do pandas
print(pd.read_excel('co2_percapita.xlsx'))

# ID da planilha Google Sheets
sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'
# URL base para acessar a planilha Google Sheets em formato CSV
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'

# Lê a planilha Google Sheets e armazena os dados em um DataFrame do pandas
dados_co2_sheets = pd.read_csv(url)

# Imprime o DataFrame 'dados_co2_sheets'
print(dados_co2_sheets)

# Nome da aba da planilha Google Sheets a ser lida
sheet_name = 'emissoes_percapita'
# URL para acessar a aba 'emissoes_percapita' da planilha Google Sheets em formato CSV
url_percapita = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

# Lê a aba 'emissoes_percapita' da planilha Google Sheets e armazena os dados em um DataFrame do pandas
percapita_sheets = pd.read_csv(url_percapita)

# Imprime as primeiras 5 linhas do DataFrame 'percapita_sheets'
print(percapita_sheets.head())

# Nome da aba da planilha Google Sheets a ser lida
sheet_name = 'fontes'
# URL para acessar a aba 'fontes' da planilha Google Sheets em formato CSV
url_fontes = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

# Lê a aba 'fontes' da planilha Google Sheets e armazena os dados em um DataFrame do pandas
fontes_sheets = pd.read_csv(url_fontes)

# Imprime as primeiras 5 linhas do DataFrame 'fontes_sheets'
print(fontes_sheets.head())
