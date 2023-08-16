# System
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Project
from config.constants import SYSTEM_CODE


class SwaggerRegister:
    params = {
        "email": openapi.Schema(type=openapi.TYPE_STRING, description="이메일", default="test@test.com"),
        "password": openapi.Schema(type=openapi.TYPE_STRING, description="비밀번호", default="test1!"),
        "username": openapi.Schema(type=openapi.TYPE_STRING, description="이름", default="tester"),
    }
    req = openapi.Schema(type=openapi.TYPE_OBJECT, properties=params)
    res = {
        201: openapi.Schema(
            "response",
            description="회원가입 성공",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    properties={
                        "access_token": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="access_token",
                            default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE2OTIxNTQ4NzUsImlhdCI6MTY5MjE1NDU3NX0.VqH_jqGvTM6qWXGZBsh41xUOoUHiehIm8Q6S5XYLPtc",
                        ),
                        "refresh_token": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="refresh_token",
                            default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE2OTQ3NDY1NzUsImlhdCI6MTY5MjE1NDU3NX0.R7jOTt53tsMHM1CzP6rm8cVBByIR96WalvRvpHajBss",
                        ),
                    },
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.SUCCESS[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.SUCCESS[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
        400: openapi.Schema(
            description="부적절한 형태의 파라미터",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    nullable=True,
                    properties={},
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.INVALID_FORMAT[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.INVALID_FORMAT[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
        409: openapi.Schema(
            description="이미 사용중인 이메일",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    nullable=True,
                    properties={},
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.EMAIL_ALREADY_USE[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.EMAIL_ALREADY_USE[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
    }


class SwaggerLogin:
    params = {
        "email": openapi.Schema(type=openapi.TYPE_STRING, description="이메일", default="test@test.com"),
        "password": openapi.Schema(type=openapi.TYPE_STRING, description="비밀번호", default="test1!"),
    }
    req = openapi.Schema(type=openapi.TYPE_OBJECT, properties=params)
    res = {
        200: openapi.Schema(
            "response",
            description="로그인 성공",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    properties={
                        "access_token": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="access_token",
                            default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE2OTIxNTQ4NzUsImlhdCI6MTY5MjE1NDU3NX0.VqH_jqGvTM6qWXGZBsh41xUOoUHiehIm8Q6S5XYLPtc",
                        ),
                        "refresh_token": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="refresh_token",
                            default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE2OTQ3NDY1NzUsImlhdCI6MTY5MjE1NDU3NX0.R7jOTt53tsMHM1CzP6rm8cVBByIR96WalvRvpHajBss",
                        ),
                    },
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.SUCCESS[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.SUCCESS[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
        400: openapi.Schema(
            description="부적절한 형태의 파라미터",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    nullable=True,
                    properties={},
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.INVALID_FORMAT[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.INVALID_FORMAT[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
        401: openapi.Schema(
            description="패스워드 불일치",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    nullable=True,
                    properties={},
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.EMAIL_PASSWORD_MISMATCH[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.EMAIL_PASSWORD_MISMATCH[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
        404: openapi.Schema(
            description="해당 이메일 미존재",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    nullable=True,
                    properties={},
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.EMAIL_NOT_FOUND[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.EMAIL_NOT_FOUND[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
    }


class SwaggerTokenRefresh:
    params = {
        "refresh_token": openapi.Schema(type=openapi.TYPE_STRING, description="refresh_token", default=""),
    }
    req = openapi.Schema(type=openapi.TYPE_OBJECT, properties=params)
    res = {
        200: openapi.Schema(
            "response",
            description="토큰 갱신 성공",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    properties={
                        "access_token": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="access_token",
                            default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE2OTIxNTQ4NzUsImlhdCI6MTY5MjE1NDU3NX0.VqH_jqGvTM6qWXGZBsh41xUOoUHiehIm8Q6S5XYLPtc",
                        ),
                        "refresh_token": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="refresh_token",
                            default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE2OTQ3NDY1NzUsImlhdCI6MTY5MjE1NDU3NX0.R7jOTt53tsMHM1CzP6rm8cVBByIR96WalvRvpHajBss",
                        ),
                    },
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.SUCCESS[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.SUCCESS[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
        400: openapi.Schema(
            description="부적절한 형태의 파라미터",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    nullable=True,
                    properties={},
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.INVALID_FORMAT[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.INVALID_FORMAT[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
        401: openapi.Schema(
            description="토큰 만료 또는 올바르지 않음.",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    nullable=True,
                    properties={},
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.TOKEN_EXPIRED[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.TOKEN_EXPIRED[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
        404: openapi.Schema(
            description="유저 미존재",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    nullable=True,
                    properties={},
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.USER_NOT_FOUND[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.USER_NOT_FOUND[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
    }


swagger_register = swagger_auto_schema(security=[], request_body=SwaggerRegister.req, responses=SwaggerRegister.res)
swagger_login = swagger_auto_schema(security=[], request_body=SwaggerLogin.req, responses=SwaggerLogin.res)
swagger_refresh_token = swagger_auto_schema(security=[], request_body=SwaggerTokenRefresh.req, responses=SwaggerTokenRefresh.res)
