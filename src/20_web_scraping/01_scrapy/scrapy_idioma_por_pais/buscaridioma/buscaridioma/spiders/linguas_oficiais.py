import scrapy

class LinguasOficiaisSpider(scrapy.Spider):
    name = 'linguas_oficiais'
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_l%C3%ADnguas_oficiais_por_pa%C3%ADs']

    def parse(self, response):
        # Encontra todas as tabelas na página
        tabelas = response.xpath('//table[contains(@class, "wikitable")]')
        self.log(f'Número de tabelas encontradas: {len(tabelas)}')

        # Lista de idiomas relevantes para a África do Sul
        idiomas_africa_do_sul = {
            'africâner', 'inglês', 'ndebele', 'xhosa', 'zulu',
            'soto setentrional', 'soto meridional', 'tsuana',
            'suázi', 'venda', 'tsonga'
        }

        # Itera sobre todas as tabelas encontradas
        for tabela in tabelas:
            # Itera sobre as linhas da tabela, começando da segunda linha (pula o cabeçalho)
            for linha in tabela.xpath('.//tr')[1:]:  # [1:] para pular o cabeçalho
                colunas = linha.xpath('.//td')
                
                if len(colunas) >= 2:  # Verifica se há pelo menos 2 colunas
                    pais = colunas[0].xpath('.//text()').getall()
                    idioma = colunas[1]

                    # Remove conteúdo dentro de <figure> e <figcaption> na coluna de idiomas
                    idiomas_texto = idioma.xpath('.//text()').getall()
                    figcaption_text = idioma.xpath('.//figure//figcaption//text()').getall()
                    figcaption_text = ' '.join(text.strip() for text in figcaption_text if text.strip())
                    
                    # Filtra a lista de idiomas, excluindo o texto dentro de <figure> e <figcaption>
                    idioma_texto = ' '.join(text.strip() for text in idiomas_texto if text.strip() and text not in figcaption_text)

                    # Se o país for a África do Sul, precisa processar de forma específica
                    if 'África do Sul' in ' '.join(pais):
                        # Extrai apenas os idiomas listados em <ul>
                        lista_idiomas = idioma.xpath('.//ul/li/a/text()').getall()
                        lista_idiomas = [item.strip() for item in lista_idiomas if item.strip() in idiomas_africa_do_sul]
                        idioma_texto = ' '.join(lista_idiomas)
                    else:
                        idioma_texto = idioma_texto

                    pais_texto = ' '.join(text.strip() for text in pais if text.strip())

                    # Adiciona logs para verificar os dados extraídos
                    if pais_texto and idioma_texto:
                        self.log(f'País: {pais_texto}, Idioma: {idioma_texto}')

                        # Cria um dicionário para armazenar os dados raspados
                        yield {
                            'País': pais_texto,
                            'Idioma': idioma_texto
                        }
