FROM python:3.7.3

RUN mkdir /app
WORKDIR /app

COPY ./* /app/

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt

CMD /bin/sh
