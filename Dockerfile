# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
MAINTAINER Fernando Oksman

WORKDIR /usr/src/app
COPY requirements.txt ./requirements.txt
RUN set -ex \
    && pip install --upgrade pip  \
    && pip install --no-cache-dir -r requirements.txt

ADD . .

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
