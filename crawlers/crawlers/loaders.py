from scrapy.loader import ItemLoader
from scrapy.loader.processors import (Compose,
                                      TakeFirst)

from .items import CrawlersItem
from .processors import (clean_termos,
                         string_to_date_processor)


class CrawlersLoader(ItemLoader):
    """Classe de loader para os crawlers"""

    default_item_class = CrawlersItem
    default_output_processor = TakeFirst()
    data_publicacao_out = Compose(string_to_date_processor)
    tags_out = Compose(clean_termos)
    fontes_out = Compose(clean_termos)

    def add_xpaths(self, data, *processors, **kw):
        """Adiciona multiplos xpaths"""

        for key, value in data.items():
            if key.startswith('_'):
                pass
            else:
                values = self._get_xpathvalues(value)
                self.add_value(key, values, *processors, **kw)

    def add_values(self, data, *processors, **kw):
        """Adiciona multiplos values"""

        for key, value in data.items():
            self.add_value(key, value)
