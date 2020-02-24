def get_spider_name(spider, item):
    """Retorna o item com o nome da spider que foi executada"""

    spider_name = spider.name
    item = item.copy()
    item['spider_name'] = spider_name

    return item
