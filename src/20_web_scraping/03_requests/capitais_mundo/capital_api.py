import requests

def obter_informacoes_pais(nome_pais):
    # Consulta a REST Countries API para obter informações do país
    url = f"https://restcountries.com/v3.1/name/{nome_pais}"  # URL da API
    response = requests.get(url)  # Faz a requisição GET para a API
    data = response.json()  # Converte a resposta para JSON
    
    if len(data) > 0:  # Verifica se a resposta contém dados
        pais = data[0]  # Extrai os dados do primeiro país retornado
        capital = pais['capital'][0]  # Obtém a capital do país
        continente = pais['region']  # Obtém o continente do país
        return capital, continente  # Retorna a capital e o continente
    else:
        return None, None  # Retorna None se não houver dados

# Exemplo de uso
pais = "Israel"  # Nome do país para buscar informações
capital, continente = obter_informacoes_pais(pais)  # Chama a função para obter informações

if capital and continente:  # Verifica se foram retornadas informações válidas
    print(f"A capital do país {pais} é {capital} e o continente {continente}.")  # Imprime as informações
else:
    print(f"Não foi possível encontrar informações para o país {pais}.")  # Imprime uma mensagem de erro caso não haja informações

