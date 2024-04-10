FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install pipenv

RUN pipenv install --deploy --ignore-pipfile

ARG SERVER_IP
ENV SERVER_IP $SERVER_IP

ARG SERVER_PORT
ENV SERVER_PORT $SERVER_PORT