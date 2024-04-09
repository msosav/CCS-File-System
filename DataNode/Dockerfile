FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install pipenv

RUN pipenv install --deploy --ignore-pipfile

ARG SERVER_URL
ENV SERVER_URL $SERVER_URL

ARG SELF_IP
ENV SELF_IP $SELF_IP

EXPOSE 50051

CMD [ "pipenv", "run", "python", "namenode.py" ]