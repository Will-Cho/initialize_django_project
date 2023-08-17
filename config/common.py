# System
import os
from uuid import uuid4
from rest_framework.response import Response
from utils import times


# Project
from config.constants import SYSTEM_CODE


def create_response(**kwargs):
    """
    response handler
    """
    status = kwargs.get("status", 200)
    headers = kwargs.get("headers", None)

    data = kwargs.get("data", None)

    code = kwargs.get("code", SYSTEM_CODE.SUCCESS)

    msg = kwargs.get("msg", code[1])

    extra = kwargs.get("extra", None)

    payload = {
        "data": data,
        "msg": msg,
        "code": code[0],
        "extra": extra,
    }

    return Response(payload, status=status, headers=headers)


def image_upload_handler(instance, filename):
    """
    image file handler
    """
    date = times.get_now().strftime("%Y/%m/%d")
    uuid = uuid4().hex
    ext = os.path.splitext(filename)[-1].lower()
    return "/".join(
        [
            date,
            uuid + ext,
        ]
    )
