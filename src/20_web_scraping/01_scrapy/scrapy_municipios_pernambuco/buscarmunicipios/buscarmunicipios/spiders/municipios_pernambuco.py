import scrapy

class MunicipiosPernambucoSpider(scrapy.Spider):
    name = 'municipios_pernambuco'
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Pernambuco_por_popula%C3%A7%C3%A3o']

    def parse(self, response):
        # Seleciona a tabela de municípios pelo corpo da tabela <tbody>
        tabela = response.xpath('//table[contains(@class, "wikitable")]/tbody')

        # Verifica se a tabela foi encontrada
        self.log(f'Tabela encontrada: {len(tabela)}')

        if len(tabela) == 0:
            self.log('Nenhuma tabela encontrada.')
            return

        # Itera sobre as linhas da tabela, começando da primeira linha de dados (pula o cabeçalho)
        for linha in tabela.xpath('.//tr'):
            colunas = linha.xpath('.//td')
            self.log(f'Número de colunas na linha: {len(colunas)}')

            if len(colunas) == 3:
                posicao = colunas[0].xpath('string()').get(default='').strip()
                municipio = colunas[1].xpath('.//a/text() | .//text()').get(default='').strip()
                populacao = colunas[2].xpath('string()').get(default='').strip()

                # Adiciona logs para verificar os dados extraídos
                self.log(f'Posição: {posicao}, Município: {municipio}, População: {populacao}')

                # Cria um dicionário para armazenar os dados raspados
                yield {
                    'Posição': posicao,
                    'Município': municipio,
                    'População': populacao
                }
