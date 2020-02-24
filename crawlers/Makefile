clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete
	@find . -name "*.pytest_cache" -exec rm -rf {} \;

test:
	pytest

coverage:
	pytest --cov=crawlers