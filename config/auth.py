# System
import jwt
from datetime import datetime, timezone, timedelta
from django.conf import settings
import functools
from rest_framework import status

# Project
from apps.users.models import User
from config.constants import SERVICE, SYSTEM_CODE
from config.exception import raise_exception
from config.response import create_response


def generate_access_token(user):
    assert isinstance(user, User)

    payload = {
        "user_id": user.id,
        "email": user.email,
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=SERVICE.ACCESS_TOKEN_EXP_MIN),
        "iat": datetime.now(tz=timezone.utc),
    }

    access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return access_token


def generate_refresh_token(user):
    assert isinstance(user, User)

    payload = {
        "user_id": user.id,
        "email": user.email,
        "exp": datetime.now(tz=timezone.utc) + timedelta(days=SERVICE.REFRESH_TOKEN_EXP_DAY),
        "iat": datetime.now(tz=timezone.utc),
    }

    refresh_token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return refresh_token


def auth_requred(f):
    @functools.wraps(f)
    def wrap(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise_exception(code=SYSTEM_CODE.AUTH_REQUIRED, status=status.HTTP_403_FORBIDDEN)

        return f(self, request, *args, **kwargs)

    return wrap
