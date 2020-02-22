START_URL = 'http://www.tecmundo.com.br/novidades/'

XPATHS_TECMUNDO = {
    '_resultados': (u'//div[contains(@class, "tec--page-filters")]'
                    u'/div/span/text()'),
    '_urls': (u'//div[contains(@class, "tec--list")]'
              '/div/article/div/h3/a/@href'),
    'titulo': u'//h1/text()',
    'tags': u'//div[contains(@id, "categories")]/a/text()',
    'data_publicacao': u'//time/@datetime',
    'tempo_leitura': (u'//div[contains(@class, "tec--timestamp '
                      u'tec--timestamp--lg")]/div/div/strong/text()'),
    'autor': u'//div[contains(@class, "tec--author")]/p[1]/a/text()',
    'fontes': (u'//h2[contains(text(), "Fontes")]/following-sibling::'
               u'div/a/text()'),
}

BLACK_LIST = [u'PUBLICIDADE',
              u'© COPYRIGHT 2020 - NO ZEBRA NETWORK S.A. TODOS OS '
              'DIREITOS RESERVADOS.',  'Cupons de desconto TecMundo:']