FROM python:3.8.10-slim-buster

COPY requirements.txt /application/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc
WORKDIR application/
RUN pip install -r requirements.txt
COPY src/* ./


CMD ["python3", "./timeout.py"]