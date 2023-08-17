# System
from rest_framework import serializers


# Project
from apps.articles.models import Article, ArticleStatus
from apps.users.serializers.user_serializers import UserReferSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserReferSerializer(read_only=True)
    thumbnail = serializers.ImageField(use_url=True)

    class Meta:
        model = Article
        fields = ["id", "user", "title", "thumbnail", "status", "created_at", "updated_at"]


class ArticleSerialzier(serializers.ModelSerializer):
    user = UserReferSerializer(read_only=True)
    thumbnail = serializers.ImageField(use_url=True)

    class Meta:
        model = Article
        fields = ["id", "user", "title", "content", "thumbnail", "created_at", "updated_at"]


class PostArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, required=True)
    content = serializers.CharField(required=True)
    thumbnail = serializers.ImageField(use_url=True, required=True)
    status = serializers.ChoiceField(choices=ArticleStatus.choices, required=True)


class PatchArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, required=False)
    content = serializers.CharField(required=False)
    thumbnail = serializers.ImageField(use_url=True, required=False)
    status = serializers.ChoiceField(choices=ArticleStatus.choices, required=False)

    class Meta:
        model = Article
        fields = ["id", "title", "content", "thumbnail", "status"]
