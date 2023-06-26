FROM python:latest

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

COPY ./entrypoint.sh /
COPY ./run_celery.sh /


# ENTRYPOINT ["sh", "/entrypoint.sh"]
