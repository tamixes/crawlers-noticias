START_URL = u'https://tecnoblog.net/categoria/news/'

URL_PAGINACAO = u'https://tecnoblog.net/categoria/news/page/{}'.format


XPATHS_TECBLOG = {
    '_urls': u'//div[contains(@class, "posts")]//article/div/a/@href',
    'titulo': u'//h1/a/text()',
    'sub_titulo': u'//h2/text()',
    'autor': u'//span[contains(@class, "author")]/a/text()',
    'data_publicacao': (u'//span[contains(@class, "author")]'
                        u'/following-sibling::time/@datetime'),
    'tags': u'//div[contains(@class, "tags")]/a/text()',
    'fontes': u'//em/a/text()',
    '_texto': u'//div[contains(@class, "entry")]//p'
}
