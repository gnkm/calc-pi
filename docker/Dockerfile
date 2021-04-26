FROM python:3.9.4-alpine3.13

COPY requirements.txt /requirements.txt

RUN apk add \
        musl-dev \
        gcc && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY . /app
WORKDIR /app
