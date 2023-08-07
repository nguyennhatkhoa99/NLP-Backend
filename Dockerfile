FROM python:3.11.4-slim-bullseye

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y gcc g++ libpq-dev python3-dev
RUN pip install --upgrade pip setuptools

RUN pip install .

ENV FLASK_APP=run.py

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]