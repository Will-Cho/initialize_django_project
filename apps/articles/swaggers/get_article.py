# System
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Project
from config.constants import SYSTEM_CODE


class SwaggerGetArticle:
    params = [
        openapi.Parameter("article_id", openapi.IN_PATH, type=openapi.TYPE_INTEGER, default=None, required=True, description="article id"),
    ]
    res = {
        200: openapi.Schema(
            "response",
            description="article 조회",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="article 고유 ID", default=None),
                        "user": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
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
                            },
                        ),
                        "title": openapi.Schema(type=openapi.TYPE_STRING, description="article 제목", default="제목"),
                        "content": openapi.Schema(type=openapi.TYPE_STRING, description="article 내용", default="내용"),
                        "thumbnail": openapi.Schema(type=openapi.TYPE_STRING, default=None, description="url"),
                        "status": openapi.Schema(type=openapi.TYPE_STRING, enum=["temp", "public", "private"], default="temp", description="status (temp, public, private)"),
                        "created_at": openapi.Schema(type=openapi.TYPE_STRING, description="생성일시", default="2023-08-17T10:14:08.335123Z"),
                        "updated_at": openapi.Schema(type=openapi.TYPE_STRING, description="갱신일시", default="2023-08-17T10:14:08.335123Z"),
                    },
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.SUCCESS[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.SUCCESS[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
        404: openapi.Schema(
            description="해당 게시글 미존재",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    nullable=True,
                    properties={},
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.ARTICLE_NOT_FOUND[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.ARTICLE_NOT_FOUND[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        ),
    }


swagger_get_article = swagger_auto_schema(manual_parameters=SwaggerGetArticle.params, responses=SwaggerGetArticle.res)
