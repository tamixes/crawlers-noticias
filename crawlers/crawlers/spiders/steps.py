# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime
import logging
import re

from crawlers.loaders import CrawlersLoader
from .constants import XPATHS_TECMUNDO, GARBAGE_LIST

logger = logging.getLogger(__name__)

def get_dados(response):
    """get the news data"""

    logger.info(u'Iniciando extraçao dos dados da noticia')

    meta = response.meta.copy()
    resultados = re.search(r'\d+.\d+', meta['resultados']).group(0)

    mensagem = u'Encontrados {} resultados'.format(resultados)
    logger.info(mensagem)

    dados = get_dados_paragrafo(response)

    loader = CrawlersLoader(response=response)
    loader.add_xpaths(XPATHS_TECMUNDO)
    loader.add_values({
        'url': meta['url'],
        'texto': dados['texto'],
        'paragrafos': dados['paragrafos'],
        'palavras': dados['palavras'],
        'total_resultados': resultados,
        'data_consulta': datetime.now()
        })
    item = loader.load_item()

    yield item

    logger.info(u'Extraçao finalizada')


def get_dados_paragrafo(response):
    """get text data"""

    text = [BeautifulSoup(text, features="lxml").get_text()
            for text in response.xpath('.//p').getall()]

    lista = GARBAGE_LIST
    texto = text[2:]
    for item in lista:
        for linha in texto:
            if item in linha:
                index = texto.index(linha)
                texto.pop(index)

    materia = ' '.join(texto)
    palavras = len(materia.split())

    dados = {
        'texto': materia,
        'palavras': palavras,
        'paragrafos': len(texto),
    }
    return dados
