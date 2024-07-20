VERSION = $(shell gobump show -r)
CURRENT_REVISION = $(shell git rev-parse --short HEAD)
BUILD_LDFLAGS = "-X github.com/zrma/1d1python.revision=$(CURRENT_REVISION)"
ifdef update
  u=-u
endif

.PHONY: help init sync sync-dev clean ruff coverage cover

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "ruff - check style and formatting"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"

init: sync-dev
	rye run pre-commit install

sync:
	rye sync --no-lock --no-dev

sync-dev:
	rye sync --no-lock

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
	rye check --fix

lint:
	rye run pre-commit run --all-files

test:
	rye run pytest

coverage: test
	rye run coverage run -m pytest ;\
	rye run coverage report -m ;\
	rye run coverage html ;\
	open htmlcov/index.html

cover:
	rye run coverage run -m pytest ;\
	rye run coverage xml -i ;\
	rye run coveralls --service=github ;\
	rye run pytest --cov=src tests/ ;\
	rye run codecov
