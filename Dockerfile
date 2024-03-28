# Use Python 3.12.2 as the base image
FROM python:3.12.2

# 1. Disable python process buffering
ENV PYTHONUNBUFFERD 1

# 2. Change working directory to /app/server
WORKDIR /app/server
ADD . /app/server

ARG DEV=false

# 3. Install MySQL and PostgreSQL dev tools
RUN apt-get update && apt-get install gcc default-libmysqlclient-dev libpq-dev -y

COPY requirements.txt ./requirements/

RUN pip install --upgrade pip && pip install -r requirements.txt

# Set up database migrations
# RUN python manage.py migrate


# CMD python manage.py runserver 0.0.0.0:8000
