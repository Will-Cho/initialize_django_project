import os
import multiprocessing

bind = "0.0.0.0:8000"

# reload = True
workers = multiprocessing.cpu_count() * 2 + 1

pidfile = "/misc/django_api_server/run/gunicorn.pid"

accesslog = "/misc/django_api_server/log/gunicorn-access.log"
errorlog = "/misc/django_api_server/log/gunicorn-error.log"
loglevel = "info"
