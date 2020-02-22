# -*- coding: utf-8 -*-
import scrapy
import logging

from .constants import (START_URL,
                        XPATHS_TECBLOG)
from .steps import get_dados

logger = logging.getLogger(__name__)


class TecblogSpider(scrapy.Spider):
    name = 'tecblog'
    allowed_domains = ['tecblog.net']
    start_urls = [START_URL]

    def __init__(self, paginas, *args, **kwargs):
        """Check if have `paginas`, case not, set default as 3"""

        super(TecblogSpider, self).__init__(*args, **kwargs)
        if paginas:
            self.paginas = int(paginas)
        else:
            self.paginas = 1

    # def start_requests(self):
    #     """Make requests to all pages, the default is 3"""
    #     for i in range(1, self.paginas+1):
    #         yield scrapy.Request(
    #             url=URL_PAGINACAO(i),
    #             callback=self.parse
    #         )

    def parse(self, response):
        """make requests to each url on the page"""

        meta = response.meta.copy()
        urls = response.xpath(XPATHS_TECBLOG['_urls']).extract()
        for url in urls:
            meta = {'url': url}
            yield scrapy.Request(
                url=url,
                callback=get_dados,
                meta=meta,
                dont_filter=True,
            )
