FROM tiangolo/uwsgi-nginx:python3.7-alpine3.8
#FROM debian:stretch-slim

RUN apk update
RUN apk add gcc libc-dev g++ libffi-dev libxml2 unixodbc-dev freetds

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=code9 Version=0.0.1
EXPOSE 8000
#ENV LISTEN_PORT=8000

# Indicate where uwsgi.ini lives
#ENV UWSGI_INI uwsgi.ini

WORKDIR /app
ADD . /app

RUN chmod g+w /app
RUN chmod g+w /app/db.sqlite3

# Using pip to install all required packages:
RUN python3 -m pip install -r requirements.txt

# Run the Django development server instead of Alpine's ngnix and uwsgi web servers:
CMD python manage.py runserver 0.0.0.0:8000
