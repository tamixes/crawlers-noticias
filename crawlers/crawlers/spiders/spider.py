# -*- coding: utf-8 -*-
import scrapy
import logging


from .constants import START_URL, XPATHS_TECMUNDO
from .steps import get_dados

logger = logging.getLogger(__name__)


class TecmundoSpider(scrapy.Spider):
    name = 'tecmundo'
    allowed_domains = ['tecmundo.com.br']
    start_urls = [START_URL]
    collection_name = 'noticias'

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
