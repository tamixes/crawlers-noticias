
all: help

help:
	@echo "all: executa make help"
	@echo "help: explica todos os comandos do makefile"
	@echo "clean: remove arquivos .pyc, __pycache__ e pytest_cache"
	@echo "test: executa pytest rodando todos os testes implementados"
	@echo "coverage: mostra a cobertura de codigo baseado nos testes"
	@echo "run: cria a pasta logs e executa o script entrypoint.py que inicia o projeto"
	@echo "clean_logs: remove os arquivos de logs das spiders"
	@echo "install: executa a instalação de requirements.txt"
	@echo "clean_all: executa clean e clean_logs"

clean_all: clean clean_logs

clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete
	@find . -name "*.pytest_cache" -exec rm -rf {} \;

test:
	pytest

coverage:
	pytest --cov=crawlers

run: 
	@mkdir -p logs
	python entrypoint.py

clean_logs:
	@find . -name "tecmundo.log" -exec rm -rf {} \;
	@find . -name "tecblog.log" -exec rm -rf {} \;

install:
	pip install -r requirements.txt