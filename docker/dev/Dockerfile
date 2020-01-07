FROM python:3.8.0

RUN mkdir /app
WORKDIR /app

COPY ./* /app/

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt

CMD /bin/sh
