# -*- coding: utf-8 -*-

import pymongo
import pandas as pd


def get_itens():
    """Faz a conexão com o mongo local e devolve um cursor com todos os dados"""

    connection_local = "mongodb://localhost:27017"
    local = pymongo.MongoClient(connection_local)

    cursor = local.noticias["noticias"].find({})

    return cursor


def create_df(itens):
    """Cria o DataFrame com todos os itens do cursor"""

    itens = get_itens()
    itens_lista = list(itens)
    data = pd.DataFrame(itens_lista)

    return data


def save_df_as_html(data):
    """Salva o DataFrame em um arquivo html"""

    html = data.to_html()

    with open('df.html', 'w') as f:
        f.write(html.encode('utf8'))


def main():
    """Chama todas as funções acima"""

    itens = get_itens()
    df = create_df(itens)
    save_df_as_html(df)


if __name__ == "__main__":
    main()
