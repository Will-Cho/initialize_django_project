# System
import traceback
import jwt
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from rest_framework.exceptions import APIException
from rest_framework import status


# Project
from apps.users.models import User
from config.constants import SYSTEM_CODE, SERVICE
from config.exception import raise_exception
from config.response import create_response
from utils import times


class CustomJWTAuthentication(BaseAuthentication):
    """
    Rest Framework Authentication Class
    """

    def authenticate(self, request):
        authorization_header = request.headers.get("Authorization")
        if not authorization_header:
            return None

        try:
            access_token = authorization_header.split(" ")[1]  # "Bearer xxxxxxx"
            payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms="HS256")

        except jwt.ExpiredSignatureError:
            # 토큰 만료
            raise_exception(code=SYSTEM_CODE.TOKEN_EXPIRED, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.DecodeError:
            # 토큰일 올바르지 않은 경우
            raise_exception(code=SYSTEM_CODE.TOKEN_INVALID, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.filter(id=payload["user_id"], email=payload["email"]).first()
        if not user:
            raise_exception(code=SYSTEM_CODE.USER_NOT_FOUND)

        return (user, None)


def cusotm_api_exception_handler(exc, context):
    """
    Custom Api Exception Handler
    """

    if isinstance(exc, APIException):
        payload = {
            "data": getattr(exc, "data", None),
            "code": getattr(exc, "code", SYSTEM_CODE.UNKNOWN_SERVER_ERROR),
            "status": getattr(exc, "status_code"),
            "extra": getattr(exc, "extra", None),
        }
        return create_response(**payload)

    if exc.__class__.__name__ == "DoesNotExist":
        return create_response(code=SYSTEM_CODE.OBJECT_DOES_NOT_EXIST, status=status.HTTP_404_NOT_FOUND)

    if SERVICE.DEBUG:
        # Print Unexpected Error Message to Console in Debug
        print(traceback.format_exc())

    return create_response(code=SYSTEM_CODE.UNKNOWN_SERVER_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
