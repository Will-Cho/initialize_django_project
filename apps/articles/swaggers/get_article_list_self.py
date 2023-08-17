# System
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Project
from config.constants import SYSTEM_CODE


class SwaggerGetArticleSelfSwagger:
    params = [
        openapi.Parameter("cursor", openapi.IN_QUERY, type=openapi.TYPE_STRING, default=None, required=False, description="cursor"),
        openapi.Parameter("limit", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=8, required=False, description="limit - 한번에 가져올 엔티티 수"),
    ]
    res = {
        200: openapi.Schema(
            "response",
            description="유저 자신의 article 리스트 조회",
            type=openapi.TYPE_OBJECT,
            properties={
                "data": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    description="응답 데이터 객체",
                    properties={
                        "page": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            description="페이지네이션",
                            properties={
                                "cursor": openapi.Schema(type=openapi.TYPE_STRING, description="다음 페이지 cursor 값", default=None),
                            },
                        ),
                        "results": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
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
                                    "thumbnail": openapi.Schema(type=openapi.TYPE_STRING, default=None, description="url"),
                                    "status": openapi.Schema(type=openapi.TYPE_STRING, enum=["temp", "public", "private"], default="temp", description="status (temp, public, private)"),
                                    "created_at": openapi.Schema(type=openapi.TYPE_STRING, description="생성일시", default="2023-08-17T10:14:08.335123Z"),
                                    "updated_at": openapi.Schema(type=openapi.TYPE_STRING, description="갱신일시", default="2023-08-17T10:14:08.335123Z"),
                                },
                            ),
                            default=[],
                            description="푸시 리스트",
                        ),
                    },
                ),
                "msg": openapi.Schema(type=openapi.TYPE_STRING, description="message", default=SYSTEM_CODE.SUCCESS[1]),
                "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code", default=SYSTEM_CODE.SUCCESS[0]),
                "extra": openapi.Schema(type=openapi.TYPE_OBJECT, description="extra data", nullable=True, default=None),
            },
        )
    }


swagger_get_article_list_self = swagger_auto_schema(manual_parameters=SwaggerGetArticleSelfSwagger.params, responses=SwaggerGetArticleSelfSwagger.res)
