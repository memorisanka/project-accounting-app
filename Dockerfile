FROM python:3.11.2-slim-bullseye

ENV PROJECT_DIR=/app
ENV PYTHONPATH /app

RUN apt update && apt -y upgrade
RUN apt install -y postgresql-client libpq-dev gcc

WORKDIR $PROJECT_DIR

COPY ./requirements.txt $PROJECT_DIR/requirements.txt
RUN pip install -r $PROJECT_DIR/requirements.txt

COPY ./ /app/

RUN chmod +x /app/run_dev_server.sh
RUN chmod +x /app/docker/check_psql.sh

