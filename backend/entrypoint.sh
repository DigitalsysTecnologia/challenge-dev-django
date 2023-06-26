#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic


DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --username admin --email admin@mail.com --noinput

gunicorn djangoproject.wsgi:application --bind 0.0.0.0:8000 --timeout 600
# python manage.py runserver 
