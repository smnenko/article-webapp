FROM python:3

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    gettext

WORKDIR /project
COPY requirements.txt /project/
RUN pip install -r requirements.txt
COPY . /project/