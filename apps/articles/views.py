# System
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, JSONParser


# Project
from config.auth import auth_requred
from config.common import create_response
from apps.articles.models import Article, ArticleStatus
from config.constants import SYSTEM_CODE
from config.exception import raise_exception
from config.pagination import custom_cursor_paginator
from apps.articles.serializers import ArticleListSerializer, ArticleSerialzier, PostArticleSerializer, PatchArticleSerializer
from apps.articles.swaggers import (
    swagger_get_article_list,
    swagger_get_article_list_self,
    swagger_get_article,
    swagger_post_article,
    swagger_delete_article,
    swagger_patch_article,
    swagger_get_article_self,
)


class ArticleViewSet(viewsets.ViewSet):
    swagger_tags = ["게시글"]
    parser_classes = [
        MultiPartParser,
    ]

    @swagger_get_article_list
    def get_article_list(self, request):
        """
        게시글 리스트를 조회
        """
        # curost pagination 사용
        pagination = custom_cursor_paginator

        queryset = Article.objects.filter(status=ArticleStatus.public).order_by("-id")

        # curost pagination 객체 추가
        pagination_data = pagination.paginate_queryset(queryset, request)

        # thumbnail url 호출을 위해 context에 reqeust 객체 추가
        serializer = ArticleListSerializer(pagination_data, many=True, context={"request": request})

        # pagination 처리된 데이터
        data = pagination.get_paginated_response(serializer.data)

        return create_response(data=data, status=status.HTTP_200_OK)

    @auth_requred
    @swagger_get_article_list_self
    def get_aritcle_list_self(self, request):
        """
        유저 자신이 작성한 게시글 리스트 조회
        """
        user = request.user
        # curost pagination 사용
        pagination = custom_cursor_paginator

        queryset = Article.objects.filter(user=user).order_by("-id")

        # curost pagination 객체 추가
        pagination_data = pagination.paginate_queryset(queryset, request)

        # thumbnail url 호출을 위해 context에 reqeust 객체 추가
        serializer = ArticleListSerializer(pagination_data, many=True, context={"request": request})

        # pagination 처리된 데이터
        data = pagination.get_paginated_response(serializer.data)

        return create_response(data=data, status=status.HTTP_200_OK)

    @auth_requred
    @swagger_get_article
    def get_article(self, request, article_id):
        """
        특정 게시글을 조회 (상세 조회)
        """
        article = Article.objects.filter(id=article_id, status=ArticleStatus.public).first()
        if not article:
            "게시글 미존재"
            raise_exception(code=SYSTEM_CODE.ARTICLE_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        seriazlier = ArticleSerialzier(article, context={"request": request})

        return create_response(data=seriazlier.data, status=status.HTTP_200_OK)

    @auth_requred
    @swagger_get_article_self
    def get_article_self(self, request, article_id):
        """
        유저 자신의 특정 게시글을 조회 (상세 조회)
        """
        user = request.user
        article = Article.objects.filter(id=article_id, user=user).first()
        if not article:
            "게시글 미존재"
            raise_exception(code=SYSTEM_CODE.ARTICLE_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        seriazlier = ArticleSerialzier(article, context={"request": request})

        return create_response(data=seriazlier.data, status=status.HTTP_200_OK)

    @auth_requred
    @swagger_post_article
    def post_article(self, request):
        """
        게시글 생성
        """
        user = request.user

        serializer = PostArticleSerializer(data=request.data)

        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT)

        data = serializer.validated_data
        article = Article.objects.create(user=user, **data)

        data = ArticleSerialzier(article, context={"request": request}).data

        return create_response(data=data, status=status.HTTP_201_CREATED)

    @auth_requred
    @swagger_patch_article
    def patch_article(self, request, article_id):
        """
        게시글 수정
        """
        user = request.user

        article = Article.objects.filter(id=article_id, user=user).first()
        if not article:
            # 해당 유저의 게시글 미존재
            raise_exception(code=SYSTEM_CODE.ARTICLE_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        serializer = PatchArticleSerializer(instance=article, data=request.data, partial=True)
        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT)

        serializer.save()

        return create_response(status=status.HTTP_200_OK)

    @auth_requred
    @swagger_delete_article
    def delete_article(self, request, article_id):
        """
        게시글 삭제
        """
        user = request.user

        article = Article.objects.filter(id=article_id, user=user).first()
        if not article:
            # 해당 유저의 게시글 미존재
            raise_exception(code=SYSTEM_CODE.ARTICLE_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        article.delete()

        return create_response(status=status.HTTP_204_NO_CONTENT)
