import requests
from bs4 import BeautifulSoup
import csv

# URL da página a ser raspada
url = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o"

# Fazendo a requisição para obter o conteúdo da página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontra a tabela com a classe 'wikitable'
tabela = soup.find('table', class_='wikitable')

if tabela is None:
    raise ValueError("Tabela com a classe 'wikitable' não encontrada.")

# Abre o arquivo CSV para escrita
with open('populacao.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Posição', 'Unidade Federativa', 'População 2022', 'População 2010', 'Mudança', 'Porcentagem população', 'País comparável']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escreve o cabeçalho no arquivo CSV
    writer.writeheader()

    # Itera sobre as linhas da tabela, ignorando o cabeçalho
    linhas = tabela.find_all('tr')[1:]  # Ignora o cabeçalho

    if not linhas:
        raise ValueError("Nenhuma linha encontrada na tabela.")

    for linha in linhas:
        colunas = linha.find_all('td')
        
        if len(colunas) < 7:
            print(f"Linha com menos de 7 colunas encontrada: {linha}")
            continue
        
        # Extraindo dados
        posicao = colunas[0].get_text(strip=True)
        unidade_federativa = colunas[1].find('a').get_text(strip=True) if colunas[1].find('a') else colunas[1].get_text(strip=True)
        populacao_2022 = colunas[2].get_text(strip=True)
        populacao_2010 = colunas[3].get_text(strip=True)
        mudanca = colunas[4].find('span').get_text(strip=True) if colunas[4].find('span') else colunas[4].get_text(strip=True)
        porcent_populacao = colunas[5].get_text(strip=True)
        pais_comparavel = colunas[6].find('a').get_text(strip=True) if colunas[6].find('a') else colunas[6].get_text(strip=True)
        
        # Log dos dados extraídos
        print(f"Posição: {posicao}, Unidade Federativa: {unidade_federativa}, População 2022: {populacao_2022}, População 2010: {populacao_2010}, Mudança: {mudanca}, Porcentagem População: {porcent_populacao}, País Comparável: {pais_comparavel}")
        
        # Escreve a linha no arquivo CSV
        writer.writerow({
            'Posição': posicao,
            'Unidade Federativa': unidade_federativa,
            'População 2022': populacao_2022,
            'População 2010': populacao_2010,
            'Mudança': mudanca,
            'Porcentagem população': porcent_populacao,
            'País comparável': pais_comparavel,
        })

print("Raspagem concluída e dados salvos em populacao.csv")
