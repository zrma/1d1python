FROM python:3.10.2

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/
COPY ./requirements-test.txt /app/
COPY ./README.md /app/
COPY ./setup.py /app/
COPY ./Makefile /app/

RUN make bootstrap

COPY ./ /app/

RUN make lint
RUN make test
