FROM python:3.11-slim

RUN mkdir code
WORKDIR code

ADD . /code/

ENV APP_NAME=root

RUN pip install -r requirements.txt

CMD gunicorn root.wsgi:application -b 0.0.0.0:8000 
