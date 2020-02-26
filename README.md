# Oncase Teste

## Sobre o projeto

É possível encontrar comandos auxiliares no Makefile, para saber quais comandos estão disponiveis, no
diretório `crawlers`, execute: `make help`. O projeto faz uso de `.env` para o set dos valores das quantidades
de páginas que o scraping acontecerá. Por padrão os valores já estão setados no arquivo `.env` localizado na pasta
`crawlers`. Os valores padrões são: 10 para `tecblog`e 10 para `tecmundo`, caso deseje alterar a quantidade
de paginas apenas altere no arqivo `.env`.

## Como executar o projeto

### Instalando mongodb

* Install mongo <https://www.mongodb.com/>
* Iniciar o servidor pelo cmd utilizando o comando `mongod`
* Install robo3t para a visualização dos dados <https://robomongo.org/download>

## Executando spiders para a captura das noticias

Considerando que o servidor do mongo está rodando em sua máquina. Execute:

```console
 cd crawlers
 make install
 make run
```

Neste ponto serão iniciados os crawlers tecmundo e tecblog, é possível visualizar os logs da execução
na pasta logs. Cada spider terá seu arquivo `.log`.
Para ver se os dados foram executados com sucesso cheque no robo3t.

É possível também executar as spiders por linha de comando. Para isso, execute:

```console
 scrapy crawl nome_spider -a paginas=valor_paginas
```

## Outras informações

Na pasta `analise` é possível encontrar algumas pequenas análises feitas em uma busca de algumas paginas
do tecmundo e tecblog, em `Analise_DB.html` e também o arquivo `.ipynb`.
Lá também é possível encontrar um arquivo `run.py`que faz uma conexão com o mongodb local
e salva os dados em um arquivo `df.html`.
