VERSION = $(shell gobump show -r)
CURRENT_REVISION = $(shell git rev-parse --short HEAD)
BUILD_LDFLAGS = "-X github.com/zrma/1d1python.revision=$(CURRENT_REVISION)"
ifdef update
  u=-u
endif

PYTHON_VERSION = 3.12

.PHONY: help init sync sync-dev clean ruff coverage cover lock lock-dev venv direnv

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "ruff - check style and formatting"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "direnv - setup direnv for automatic virtual environment activation"

direnv:
	@echo "#!/bin/bash" > .envrc
	@echo "export VIRTUAL_ENV=\"./.venv\"" >> .envrc
	@echo "layout python" >> .envrc
	@direnv allow
	@echo "direnv setup complete. Environment will be automatically activated when entering this directory."

clean: clean-pyc clean-test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .coverage
	rm -fr htmlcov/

ruff:
	uv run ruff check --fix .

lint:
	uv run pre-commit run --all-files

test:
	uv run pytest

coverage: test
	uv run coverage run -m pytest ;\
	uv run coverage report -m ;\
	uv run coverage html ;\
	open htmlcov/index.html

cover:
	uv run coverage run -m pytest ;\
	uv run coverage xml -i ;\
	uv run coveralls --service=github ;\
	uv run pytest --cov=src tests/ ;\
	uv run codecov
