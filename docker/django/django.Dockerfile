# pull offcial base image
FROM --platform=linux/amd64 python:3.8.2

# SET USER
USER root

# SET ENVIROMENT VARIABLES
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# INSTALL REQUIREMENTS
COPY ./requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

# CREATE DIRECTORIES
ENV APP_HOME=/misc/django_api_server
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/log
RUN mkdir -p $APP_HOME/run

# set work directory
WORKDIR $APP_HOME

# copy project
COPY . .

RUN echo $(ls -1 /misc/django_api_server)

EXPOSE 8000

# run entrypoint.sh
RUN chmod +x $APP_HOME/docker/django/entrypoint.sh