# System
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Project
from config.constants import SYSTEM_CODE


class SwaggerDeletetArticle:
    params = [
        openapi.Parameter("article_id", openapi.IN_PATH, type=openapi.TYPE_INTEGER, default=None, required=True, description="article id"),
    ]
    res = {
        204: openapi.Schema(
            "response",
            description="article 삭제",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    properties={},
                    nullable=True,
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


swagger_delete_article = swagger_auto_schema(manual_parameters=SwaggerDeletetArticle.params, responses=SwaggerDeletetArticle.res)
