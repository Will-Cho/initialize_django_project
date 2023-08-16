# System
from rest_framework.response import Response


# Project
from config.constants import SYSTEM_CODE


def create_response(**kwargs):
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
