import scrapy
from scrapy.selector import Selector

class BuscarPopulacaoSpider(scrapy.Spider):
    name = "populacao"
    start_urls = ["https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o"]

    def parse(self, response):
        selector = Selector(response)
        tabelas = selector.xpath("//table[contains(@class, 'wikitable')]")
        
        for tabela in tabelas:
            linhas = tabela.xpath(".//tr[position()>1]")  # Ignora o cabeçalho
            
            for linha in linhas:
                colunas = linha.xpath(".//td")
                if len(colunas) >= 5:
                    posicao = colunas[1].xpath(".//text()").get().strip()
                    pais = colunas[2].xpath(".//a/text()").get() or colunas[1].xpath(".//text()").get().strip()
                    populacao = colunas[3].xpath(".//text()").get().strip()
                    crescimento = colunas[4].xpath(".//text()").get().strip()
                    
                    yield {
                        "posição": posicao,
                        "país": pais,
                        "população": populacao,
                        "crescimento": crescimento
                    }
