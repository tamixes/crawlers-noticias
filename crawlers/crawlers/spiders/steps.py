# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime
import re

from crawlers.loaders import CrawlersLoader

from .constants import XPATHS_TECMUNDO, BLACK_LIST


def get_dados(response):
    meta = response.meta.copy()
    resultados = re.search(r'\d+.\d+', meta['resultados']).group(0)

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


def get_dados_paragrafo(response):
    text = [BeautifulSoup(text, features="lxml").get_text()
            for text in response.xpath('.//p').getall()]

    lista = BLACK_LIST
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
