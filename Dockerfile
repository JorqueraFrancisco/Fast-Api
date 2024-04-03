FROM python:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /app/fast_api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
