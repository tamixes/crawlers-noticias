# -*- coding: utf-8 -*-
import scrapy
import logging

from .constants import (START_URL,
                        XPATHS_TECMUNDO,
                        URL_PAGINACAO)
from .steps import get_dados

logger = logging.getLogger(__name__)


class TecmundoSpider(scrapy.Spider):
    name = 'tecmundo'
    allowed_domains = ['tecmundo.com.br']
    start_urls = [START_URL]

    def __init__(self, paginas, *args, **kwargs):
        super(TecmundoSpider, self).__init__(*args, **kwargs)

        self.paginas = int(paginas)

    def start_requests(self):
        """Da start em todas as requisições das paginas iniciais"""

        for i in range(1, self.paginas+1):
            yield scrapy.Request(
                url=URL_PAGINACAO(i),
                callback=self.parse
            )

    def parse(self, response):
        """Faz as requisiçoes para cada noticia da pagina"""

        meta = response.meta.copy()
        total_resultados = response.xpath(XPATHS_TECMUNDO
                                          ['_resultados']).extract_first()
        urls = response.xpath(XPATHS_TECMUNDO['_urls']).extract()

        for url in urls:
            meta = {
                'url': url,
                'resultados': total_resultados,
            }
            yield scrapy.Request(
                url=url,
                callback=get_dados,
                meta=meta,
                dont_filter=True,
            )
