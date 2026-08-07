import scrapy

class AreasPaisesSpider(scrapy.Spider):
    name = 'areas_paises'
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_e_territ%C3%B3rios_por_%C3%A1rea']

    def parse(self, response):
        # Encontra todas as tabelas na página
        tabelas = response.xpath('//table[contains(@class, "wikitable")]')
        self.log(f'Número de tabelas encontradas: {len(tabelas)}')

        # Itera sobre todas as tabelas encontradas
        for tabela in tabelas:
            # Itera sobre as linhas da tabela, começando da segunda linha (pula o cabeçalho)
            for linha in tabela.xpath('.//tr')[1:]:  # [1:] para pular o cabeçalho
                colunas = linha.xpath('.//td')
                self.log(f'Número de colunas na linha: {len(colunas)}')

                if len(colunas) >= 4:  # Verifica se há pelo menos 4 colunas
                    posicao = colunas[0].xpath('string()').get(default='').strip()
                    pais = colunas[1].xpath('string()').get(default='').strip()
                    area = colunas[2].xpath('string()').get(default='').strip()

                    # Adiciona logs para verificar os dados extraídos
                    self.log(f'Posição: {posicao}, País: {pais}, Área: {area}')

                    # Cria um dicionário para armazenar os dados raspados
                    yield {
                        'Posição': posicao,
                        'País': pais,
                        'Área (km²)': area
                    }
