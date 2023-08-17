# Project Descriptions
## Project Develop Enviroment
### Develop
- General 
  - use Python 3.11
  - use Django 4.2.4
  - use djangorestframework 3.14.0
  - check more in requirements.txt
- About Django
  - use viewsets.Viwset
  - use serializers (drf)
- Run Django
  - ```pip install requirements```
  - set **.env** file
  - ```python manage.py runserver```
  - http://127.0.0.1:8000/
### code test & conventions
  - check ```.pre-commit-config.yaml```
    - use pre-commit
      - recommend to install pre-commit in your os
    - use black (python code formatter)
  - test
    - before test, you have to set database info in **.env** file
      - especially set the test database name under DB_TEST_NAME - this test database must created in your database
    - ```python manage.py test apps --keepdb```
## Project Structure
```
├── .env # => you have to create this file. Please refer to **env-sample** file
├── .gitignore
├── .pre-commit-config.yaml
├── apps
│   ├── apps.py
│   ├── systems
│   └── users
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── auth.py
│   ├── constants.py
│   ├── exception.py
│   ├── response.py
│   ├── rest_framework.py
│   ├── settings.py
│   ├── swaggers
│   ├── urls.py
│   └── wsgi.py
├── docker
├── env-sample
├── manage.py
├── readme.md
├── requirements.txt
└── utils
    ├── decorator
    ├── redis
    ├── swagger
    └── times.py

```
### What is Django Project?
- config
### Where Django Apps?
- located in **apps** subdirectory
  - users (users)
  - systems (a collection of code on which this apps are based)
  - more...
### Authentication
- use jwt (PyJWT)
- use "access_token" & "refresh_token"
- use django rest framework
### Swagger API Docs
- use drf_yasg
  - ```http(s)://domain( or localhost)/swagger/v1/```

## Deploy
### Architecture
- nginx + gunicron + django + mariadb
### Set Enviroment
- edit **.env** file
```
# SERVICE
DEPLOY_ENV= # server deploy enviroment (dev or prod or ...)
DJANGO_SETTINGS_MODULE= # django default settings (default = config.settings)
CORS_ORIGIN_WHITELIST= # String Array ('["http://localhost:3000", "http://localhost:8000",]')
SECRET_KEY= # Secret Key
DEBUG= # Debug on/off (on = 1, off = 0)
ACCESS_TOKEN_EXP_MIN= # access token expire minutes
REFRESH_TOKEN_EXP_DAY= # refresh token expire day

# DATABASE
DB_NAME= # database name
DB_USER= # database granted user
DB_PASSWORD= # database granted user's password
DB_HOST= # database host
DB_PORT= # database port
DB_TEST_NAME= # test database name

# REDIS
REDIS_HOST= # redis host
```

- **env sample**
```
# SERVICE
DEPLOY_ENV=dev
DJANGO_SETTINGS_MODULE=config.settings
CORS_ORIGIN_WHITELIST='[
    "http://localhost:3000",
    "http://localhost:8000",
]'
SECRET_KEY=django-insecure-%nimn^2j%!qj8ox=u+qzc6gmk87psqc3))z#jc32%&hd=^ad7i
DEBUG=1
ACCESS_TOKEN_EXP_MIN=5
REFRESH_TOKEN_EXP_DAY=30

# DATABASE
DB_NAME=service_db
DB_USER=db_user
DB_PASSWORD=db_user1!
DB_HOST=127.0.0.1
DB_PORT=3306
DB_TEST_NAME=test_service_db

# REDIS
REDIS_HOST=
```


### Test Deploy with docker-compose

- set "**DB_HOST**=mariadb" in **.env** file
  - ```DB_HOST=mariadb```


- docker-compose (in local)
  - use **env sample**
    ```
    # path : $project_path
    docker-compose -f $project_path/docker/docker-compose-yml up --build -d
    ```
  - web site
    - ```http://localhost```
    - ```http://localhost/admin/```
    - ```http://localhost/swagger/v1/```

  - create superuser (if you want to login to admindjango page)
    - if you want to create superuser in test deploy enviroment
      - connect to background running container ""
      - enter this command : ```python manage.py createsuperuser```
      - enter email, username, password


