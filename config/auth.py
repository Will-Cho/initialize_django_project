# System
import jwt
from datetime import datetime, timezone, timedelta
from django.conf import settings


# Project
from apps.users.models import User
from config.constants import SERVICE


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
