FROM python:3.12.0-alpine

WORKDIR /app/api

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY ./requirements.txt /app/api
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /app/api