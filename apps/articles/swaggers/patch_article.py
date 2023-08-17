# System
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Project
from config.constants import SYSTEM_CODE


class SwaggerPatchArticle:
    params = [
        openapi.Parameter("article_id", openapi.IN_PATH, type=openapi.TYPE_INTEGER, default=None, required=True, description="article id"),
        openapi.Parameter("title", openapi.IN_FORM, type=openapi.TYPE_STRING, default=None, required=False, description="제목"),
        openapi.Parameter("content", openapi.IN_FORM, type=openapi.TYPE_STRING, default=None, required=False, description="내용"),
        openapi.Parameter("thumbnail", openapi.IN_FORM, type=openapi.TYPE_FILE, default=None, required=False, description="제목"),
        openapi.Parameter("status", openapi.IN_FORM, type=openapi.TYPE_STRING, default=None, enum=["temp", "public", "private"], required=False, description="status (temp, public, private)"),
    ]
    res = {
        200: openapi.Schema(
            "response",
            description="article 수정",
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


swagger_patch_article = swagger_auto_schema(manual_parameters=SwaggerPatchArticle.params, responses=SwaggerPatchArticle.res)
