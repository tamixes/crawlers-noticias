# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class CrawlersItem(Item):
    """Items dos Crawlers"""

    url = Field()
    autor = Field()
    tags = Field()
    data_publicacao = Field()
    data_consulta = Field()
    texto = Field()
    titulo = Field()
    paragrafos = Field()
    tamanho = Field()
    palavras = Field()
    fontes = Field()
    tempo_leitura = Field()
    total_resultados = Field()
    spider_name = Field()
