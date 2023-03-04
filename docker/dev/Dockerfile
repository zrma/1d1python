FROM python:3.12.0a5

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY ./ /app/

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt
