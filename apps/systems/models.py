# System
from django.db import models


class BaseModel(models.Model):
    """
    모든 Model에서 사용할 Base Model
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
