FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install pipenv

RUN pipenv install --deploy --ignore-pipfile

ARG SERVER_IP
ENV SERVER_IP $SERVER_IP

ARG SELF_IP
ENV SELF_IP $SELF_IP

EXPOSE 50051

CMD [ "pipenv", "run", "python", "datanode.py" ]