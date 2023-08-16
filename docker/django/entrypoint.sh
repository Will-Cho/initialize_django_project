#!/bin/bash
echo "run django service"
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations --noinput
python3 manage.py migrate &
gunicorn --preload config.wsgi:application --config=docker/django/gunicorn_conf.py