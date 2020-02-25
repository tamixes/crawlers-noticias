import os
import subprocess


def load_env():
    from dotenv import load_dotenv
    from pathlib import Path

    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)


def crawl_process():
    spider_1 = os.getenv('SPIDER_1', default='tecblog')
    tecmundo_pages = os.getenv('TECMUNDO_PAGES', default=2)

    spider_2 = os.getenv('SPIDER_2', default='tecmundo')
    tecblog_pages = os.getenv('TECBLOG_PAGES', default=2)

    comando = 'scrapy crawl {0} -a paginas="{1}" --logfile ./logs/{2}.log'.format

    subprocess.call(comando(spider_1, tecmundo_pages, spider_1), shell=True)
    subprocess.call(comando(spider_2, tecblog_pages, spider_2), shell=True)


def main():
    load_env()
    crawl_process()


if __name__ == '__main__':
    main()
