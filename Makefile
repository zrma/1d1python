VERSION = $(shell gobump show -r)
CURRENT_REVISION = $(shell git rev-parse --short HEAD)
BUILD_LDFLAGS = "-X github.com/zrma/tdd.revision=$(CURRENT_REVISION)"
ifdef update
  u=-u
endif

VENV ?= . env/bin/activate


.PHONY: help bootstrap clean lint test coverage docs release install jenkins

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "release - package and upload a release"
	@echo "install - install the package to the active Python's site-packages"

bootstrap:
	python -m venv env
	$(VENV) ;\
	pip install --upgrade setuptools ;\
	pip install --upgrade "pip>=19" ;\
	pip install -r requirements.txt ;\
	pip install -r requirements-test.txt ;\

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .coverage
	rm -fr htmlcov/

lint:
	$(VENV) ;\
	flake8 src tests
	$(VENV) ;\
	mypy ./src/*
	$(VENV) ;\
	mypy ./tests/*

test:
	$(VENV) ;\
	python setup.py test $(TEST_ARGS)
	make clean

jenkins: test

coverage: test
	$(VENV) ;\
	coverage run --source src setup.py test ;\
	coverage report -m ;\
	coverage html ;\
	open htmlcov/index.html ;\

release: clean
	fullrelease

install: clean
	$(VENV) ;\
	python setup.py install

cover:
	$(VENV) ;\
	coverage run --source=src setup.py test
	coverage xml -i
	COVERALLS_TOKEN=${COVERALLS_TOKEN} coveralls --service=travis-ci
	pytest --cov=src tests/
	codecov
