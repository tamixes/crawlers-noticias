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
        """Check if have `paginas`, case not, set default as 3"""

        super(TecmundoSpider, self).__init__(*args, **kwargs)
        if paginas:
            self.paginas = int(paginas)
        else:
            self.paginas = 3

    def start_requests(self):
        """Make requests to all pages, the default is 3"""
        for i in range(1, self.paginas+1):
            yield scrapy.Request(
                url=URL_PAGINACAO(i),
                callback=self.parse
            )
    def parse(self, response):
        """make requests to each url on the page"""

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
                meta=meta
            )
