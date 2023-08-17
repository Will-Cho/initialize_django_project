# System
from django.db import models
from django.conf import settings

# Project
from apps.systems.models import BaseModel
from config.common import image_upload_handler


class ArticleStatus(models.TextChoices):
    temp = "temp", "임시저장"
    public = "public", "공개"
    private = "private", "비공개"


class Article(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="user_article",
        blank=False,
        null=False,
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to=image_upload_handler)  # if use s3, change filed to url or char
    status = models.CharField(max_length=10, choices=ArticleStatus.choices, default=ArticleStatus.temp)
