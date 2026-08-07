# Definindo duas listas de palavras, uma tratada e outra não tratada
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

# Definindo a função que avalia o texto
def avalia_texto(texto: list):
    for palavra in texto:  # Itera por cada palavra na lista de texto
        if (',' or '.' or '!' or '?') in palavra:  # Verifica se a palavra contém alguma pontuação
            raise ValueError(f'O texto apresenta pontuações na palavra "{palavra}".')
    return "Texto já tratado!"  # Retorna uma mensagem se nenhum erro for encontrado

# Testando no exemplo que não lança exceção (lista_tratada)
try:
    avaliacao = avalia_texto(lista_tratada)
except Exception as e:
    print(e)
else:
    print(avaliacao)

# Testando no exemplo que lança exceção (lista_nao_tratada)
try:
    avaliacao = avalia_texto(lista_nao_tratada)
except Exception as e:
    print(e)
else:
    print(avaliacao)

