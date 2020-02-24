# -*- coding: utf-8 -*-
import scrapy
import logging

from .constants import (START_URL,
                        URL_PAGINACAO,
                        XPATHS_TECBLOG)
from .steps import get_dados

logger = logging.getLogger(__name__)


class TecblogSpider(scrapy.Spider):
    name = 'tecblog'
    allowed_domains = ['tecblog.net']
    start_urls = [START_URL]

    def __init__(self, paginas, *args, **kwargs):

        super(TecblogSpider, self).__init__(*args, **kwargs)

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

        urls = response.xpath(XPATHS_TECBLOG['_urls']).extract()
        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=get_dados,
                dont_filter=True,
            )
