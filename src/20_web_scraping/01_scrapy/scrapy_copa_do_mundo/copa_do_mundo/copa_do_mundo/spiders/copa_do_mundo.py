""" import requests
from bs4 import BeautifulSoup
import csv

# URL da página da Copa do Mundo na Wikipedia
url = "https://pt.m.wikipedia.org/wiki/Copa_do_Mundo_FIFA"

# Fazendo a requisição HTTP para a página
response = requests.get(url)

# Parseando o conteúdo HTML da página com BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Buscando todas as tags h3 na página
h3_tags = soup.find_all('h3')
tabela = None

# Percorrendo as tags h3 para encontrar a seção "Por edições"
for h3 in h3_tags:
    if 'Por edições' in h3.get_text():
        tabela = h3.find_next('table')
        break

# Verificando se a tabela foi encontrada
if tabela:
    # Nome do arquivo CSV a ser criado
    csv_file = 'copa_do_mundo.csv'
    
    # Abrindo (ou criando) o arquivo CSV no modo de escrita
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Escrevendo o cabeçalho do CSV
        writer.writerow(['Ano', 'País-sede', 'Campeão', 'Vice-campeão', 'Terceiro lugar', 'Quarto lugar'])
        
        # Extraindo as linhas da tabela
        for linha in tabela.find_all('tr')[1:]:  # Ignorando o cabeçalho
            colunas = linha.find_all('td')
            
            # Verificando se há colunas suficientes na linha
            if len(colunas) >= 6: 
                # Extraindo os dados de cada coluna
                ano = colunas[0].get_text(strip=True).replace('Detalhes', '').replace('[nota 3]', '').strip()  # Ano
                pais_sede = colunas[1].get_text(strip=True)  # País-sede
                campeao = colunas[2].get_text(strip=True).replace(' (pro)', '').strip()  # Campeão
                vice_campeao = colunas[4].get_text(strip=True).replace(' (pro)', '').strip()  # Vice-Campeão
                terceiro_lugar = colunas[5].get_text(strip=True).replace(' (pro)', '').strip()  # Terceiro lugar
                quarto_lugar = colunas[7].get_text(strip=True).replace(' (pro)', '').strip()  # Quarto lugar

                # Corrigindo a linha de 1950 especificamente
                if ano == '1950':
                    campeao = 'Uruguai'
                    vice_campeao = 'Brasil'
                    terceiro_lugar = 'Suécia'
                    quarto_lugar = 'Espanha'

                # Escrevendo a linha de dados no CSV
                writer.writerow([ano, pais_sede, campeao, vice_campeao, terceiro_lugar, quarto_lugar])
    
    print(f"Arquivo '{csv_file}' criado com sucesso.")
else:
    print("Tabela 'Por edições' não encontrada.")
 """

import requests
from bs4 import BeautifulSoup
import csv

# URL da página da Copa do Mundo na Wikipedia
url = "https://pt.m.wikipedia.org/wiki/Copa_do_Mundo_FIFA"

# Fazendo a requisição HTTP para a página
response = requests.get(url)

# Parseando o conteúdo HTML da página com BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

def limpar_texto(texto):
    # Remove "Detalhes" e "[nota x]"
    texto_limpo = texto.replace('Detalhes', '').split('[')[0].strip()
    return texto_limpo

def extrair_tabela(titulo, nome_arquivo, colunas_necessarias, colunas_indices, correcao_1950=None):
    # Buscando todas as tags h3 na página
    h3_tags = soup.find_all('h3')
    tabela = None

    # Percorrendo as tags h3 para encontrar a seção desejada
    for h3 in h3_tags:
        if titulo in h3.get_text():
            tabela = h3.find_next('table')
            break

    # Verificando se a tabela foi encontrada
    if tabela:
        # Abrindo (ou criando) o arquivo CSV no modo de escrita
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Escrevendo o cabeçalho do CSV
            writer.writerow(colunas_necessarias)
            
            # Extraindo as linhas da tabela
            for linha in tabela.find_all('tr')[1:]:  # Ignorando o cabeçalho
                colunas = linha.find_all(['td', 'th'])  # Inclui 'th' para capturar cabeçalhos nas tabelas

                # Verificando se há colunas suficientes na linha
                if len(colunas) >= max(colunas_indices) + 1: 
                    dados_linha = [limpar_texto(colunas[i].get_text(strip=True)) for i in colunas_indices]

                    # Aplicando a correção específica para 1950, se fornecida
                    if correcao_1950 and dados_linha[0] == '1950':
                        dados_linha[1:] = correcao_1950

                    writer.writerow(dados_linha)
                else:
                    print(f"Linha ignorada, colunas insuficientes: {linha}")

        print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
    else:
        print(f"Tabela '{titulo}' não encontrada.")

# Extraindo a tabela "Por edições"
extrair_tabela(
    titulo="Por edições",
    nome_arquivo="copa_do_mundo_por_edicoes.csv",
    colunas_necessarias=['Ano', 'País-sede', 'Campeão', 'Vice-campeão', 'Terceiro lugar', 'Quarto lugar'],
    colunas_indices=[0, 1, 2, 4, 5, 7],
    correcao_1950=['Brasil', 'Uruguai', 'Brasil', 'Suécia', 'Espanha']
)

# Extraindo a tabela "Por seleções"
extrair_tabela(
    titulo="Por seleções",
    nome_arquivo="copa_do_mundo_por_selecoes.csv",
    colunas_necessarias=['Seleção', 'Títulos', 'Vices', '3º lugar', '4º lugar'],
    colunas_indices=[0, 1, 2, 3, 4]
)

# Extraindo a tabela "Por confederações"
extrair_tabela(
    titulo="Por confederações",
    nome_arquivo="copa_do_mundo_por_confederacoes.csv",
    colunas_necessarias=['Seleções', 'Títulos', 'Vices', '3º lugar', '4º lugar'],
    colunas_indices=[0, 1, 2, 3, 4]
)
