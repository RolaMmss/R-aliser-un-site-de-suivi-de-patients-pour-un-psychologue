FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /code

ARG postgre_db
ARG utilisateur
ARG mot_de_passe

RUN apt-get update

COPY requirements.txt /code/

RUN pip install -r ../requirements.txt

COPY . /code/