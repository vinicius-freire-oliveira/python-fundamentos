import scrapy

class LinguasPorFalantesSpider(scrapy.Spider):
    name = 'linguas_por_falantes'
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_l%C3%ADnguas_por_n%C3%BAmero_total_de_falantes']

    def parse(self, response):
        # Encontra todas as tabelas na página
        tabelas = response.xpath('//table[contains(@class, "wikitable")]')
        self.log(f'Número de tabelas encontradas: {len(tabelas)}')

        # Itera sobre todas as tabelas encontradas
        for tabela in tabelas:
            # Itera sobre as linhas da tabela, começando da segunda linha (pula o cabeçalho)
            for linha in tabela.xpath('.//tr')[1:]:  # [1:] para pular o cabeçalho
                colunas = linha.xpath('.//td')

                if len(colunas) >= 6:  # Verifica se há pelo menos 6 colunas
                    posicao = colunas[0].xpath('string()').get(default='').strip()
                    lingua = colunas[1].xpath('string()').get(default='').strip()
                    familia = colunas[2].xpath('string()').get(default='').strip()
                    lingua_materna = colunas[3].xpath('string()').get(default='').strip()
                    segunda_lingua = colunas[4].xpath('string()').get(default='').strip()
                    numero_total_falantes = colunas[5].xpath('string()').get(default='').strip()

                    # Adiciona logs para verificar os dados extraídos
                    self.log(f'Posição: {posicao}, Língua: {lingua}, Família: {familia}, Língua Materna: {lingua_materna}, Segunda Língua: {segunda_lingua}, Número Total de Falantes: {numero_total_falantes}')

                    # Cria um dicionário para armazenar os dados raspados
                    yield {
                        'Posição': posicao,
                        'Língua': lingua,
                        'Família': familia,
                        'Língua Materna': lingua_materna,
                        'Segunda Língua': segunda_lingua,
                        'Número Total de Falantes': numero_total_falantes
                    }
