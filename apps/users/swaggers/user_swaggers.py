# System
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Project
from config.constants import SYSTEM_CODE


class SwaggerGetUser:
    res = {
        200: openapi.Schema(
            "response",
            description="유저 자신의 정보 성공",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    properties={
                        "id": openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description="user_id",
                            default=1,
                        ),
                        "email": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="email",
                            default="test@test.com",
                        ),
                        "username": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="username",
                            default="tester",
                        ),
                        "last_login": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="마지막 로그인 일시",
                            default="2023-08-16T06:53:45.906861Z",
                        ),
                        "date_joind": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="회원가입 일시",
                            default="2023-08-16T06:53:45.906861Z",
                        ),
                    },
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.SUCCESS[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.SUCCESS[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
    }


swagger_get_user = swagger_auto_schema(responses=SwaggerGetUser.res)
