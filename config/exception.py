# System
from rest_framework.exceptions import APIException
from rest_framework import status


# Project
from config.constants import SYSTEM_CODE


class CustomAPIException(APIException):
    """
    Custom API Exception Response
    의도한 예외 발생 시, 호출하는 exception code (CustomAPIException)
    """

    def __init__(self, **kwargs):
        self.status_code = kwargs.get("status", status.HTTP_400_BAD_REQUEST)
        self.data = kwargs.get("data", None)
        self.code = kwargs.get("code", SYSTEM_CODE.CLIENT_ERROR)
        self.extra = kwargs.get("extra", None)
        self.detail = kwargs.get("detail", "오류가 발생했습니다.")


def raise_exception(**kwargs):
    """
    Call CustomAPIException Class
    """
    raise CustomAPIException(**kwargs)
