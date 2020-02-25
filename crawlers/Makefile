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
