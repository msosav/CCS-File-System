FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install pipenv

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 8080

CMD [ "pipenv", "run", "python", "namenode.py" ]