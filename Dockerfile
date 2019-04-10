FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code 
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
