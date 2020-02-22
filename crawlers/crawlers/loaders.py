from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Identity, Compose

from .items import CrawlersItem
from .processors import string_to_date_processor


class CrawlersLoader(ItemLoader):
    """Loader to the Crawlers"""

    default_item_class = CrawlersItem
    default_output_processor = TakeFirst()
    data_publicacao_out = Compose(string_to_date_processor)
    tags_out = Identity()
    fontes_out = Identity()

    def add_xpaths(self, data, *processors, **kw):
        """Add multiple xpaths"""

        for key, value in data.items():
            if key.startswith('_'):
                pass
            else:
                values = self._get_xpathvalues(value)
                self.add_value(key, values, *processors, **kw)

    def add_values(self, data, *processors, **kw):
        """Add multiple values"""

        for key, value in data.items():
            self.add_value(key, value)
