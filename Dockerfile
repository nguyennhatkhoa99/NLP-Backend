FROM python:3.11.4-slim-bullseye

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install -y gcc g++

COPY . /app

RUN pip install .

ENV FLASK_APP=run.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5001"]