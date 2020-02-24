from bs4 import BeautifulSoup
from datetime import datetime
import logging

from crawlers.loaders import CrawlersLoader
from .constants import XPATHS_TECBLOG

logger = logging.getLogger(__name__)


def get_dados(response):
    """Extrai os dados da noticia"""

    logger.info(u'Iniciando extraçao dos dados da noticia')

    dados = get_dados_paragrafo(response)

    loader = CrawlersLoader(response=response)
    loader.add_xpaths(XPATHS_TECBLOG)
    loader.add_values({
        'url': response.url,
        'data_consulta': datetime.now(),
        'texto': dados['texto'],
        'palavras': dados['palavras'],
        'paragrafos': dados['paragrafos']
    })
    item = loader.load_item()

    yield item

    logger.info(u'Extração finalizada')


def get_dados_paragrafo(response):
    """Extrai o texto da noticia, quantidade de paragrafos e palavras"""

    logger.info('Extraindo dados dos paragrafos')

    texto = response.xpath(XPATHS_TECBLOG['_texto']).getall()
    text = [BeautifulSoup(text, features="lxml").get_text() for text in texto]

    materia = clean_texto(text)

    palavras = len(materia.split())

    mensagem = (u'Encontradas {palavras} palavras e {paragrafos} '
                u'paragrafos').format(palavras=palavras, paragrafos=len(text))
    logger.info(mensagem)

    dados = {
        'texto': materia,
        'palavras': palavras,
        'paragrafos': len(text),
    }
    return dados


def clean_texto(text):
    """Retorna a materia limpa e estruturada"""

    mensagem = u'Com informações:'
    for linha in text:
        if mensagem in linha:
            index = text.index(linha)
            text.pop(index)

    materia = ' '.join(text)

    return materia
