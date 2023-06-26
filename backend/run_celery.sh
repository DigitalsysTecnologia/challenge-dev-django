#!/bin/sh

celery -A djangoproject.celery worker --loglevel=info -P threads