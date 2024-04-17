FROM python:3.8.10-slim-buster

COPY requirements.txt /application/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc
WORKDIR application/
RUN pip install -r requirements.txt
COPY src/* ./

RUN adduser --disabled-password --gecos '' --system --uid 1001 python && chown -R python /application

USER 1001

CMD ["python3", "./timeout.py"]