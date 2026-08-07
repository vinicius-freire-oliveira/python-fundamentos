import scrapy

class PresidentesDoBrasilSpider(scrapy.Spider):
    name = 'presidentes_do_brasil'
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_presidentes_do_Brasil']

    def parse(self, response):
        tabelas = response.xpath('//table[contains(@class, "wikitable")]')
        self.log(f'Número de tabelas encontradas: {len(tabelas)}')

        for tabela in tabelas:
            for linha in tabela.xpath('.//tr')[1:]:  # Pular o cabeçalho
                colunas = linha.xpath('.//td')

                if len(colunas) >= 8:
                    numero = self.extrair_texto(colunas[0])
                    presidente = self.extrair_texto(colunas[1])
                    periodo = self.extrair_texto(colunas[3])
                    partido = self.extrair_texto(colunas[4])
                    vice_presidente = self.extrair_texto(colunas[5])
                    eleicao = self.extrair_texto(colunas[7])

                    self.log(f'Número: {numero}, Presidente: {presidente}, Período: {periodo}, Partido: {partido}, Vice-Presidente(s): {vice_presidente}, Eleição: {eleicao}')

                    yield {
                        'Número': numero,
                        'Presidente': presidente,
                        'Período do Mandato': periodo,
                        'Partido': partido,
                        'Vice-Presidente(s)': vice_presidente,
                        'Eleição': eleicao
                    }

    def extrair_texto(self, celula):
        textos = []

        # Extraí texto direto e de sub-elementos
        for sub_elemento in celula.xpath('.//text()').getall():
            texto = sub_elemento.strip()
            if texto:
                textos.append(texto)

        return ' '.join(textos).replace('\n', ' ').strip()
