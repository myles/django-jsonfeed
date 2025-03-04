.PHONY: all
all: clean setup test lint mypy

.PHONY: setup
setup: pyproject.toml
	poetry check
	poetry install

.PHONY: test
test:
	poetry run pytest --cov=jsonfeed/ --cov-report=xml

.PHONY: lint
lint:
	poetry run black --check jsonfeed/
	poetry run isort --check jsonfeed/
	poetry run ruff check jsonfeed/

.PHONY: lintfix
lintfix:
	poetry run black jsonfeed/
	poetry run isort jsonfeed/
	poetry run ruff check jsonfeed/ --fix

.PHONY: mypy
mypy:
	poetry run mypy jsonfeed/

.PHONY: clean
clean:
	rm -fr ./.mypy_cache
	rm -fr ./.pytest_cache
	rm -fr ./.ruff_cache
	rm -fr ./dist
	rm -f .coverage
	rm -f coverage.xml
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: ci
ci: setup test lint mypy