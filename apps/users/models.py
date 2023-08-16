# System
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Project
from apps.systems.models import BaseModel
from apps.users.managers import CustomUserManager


class User(AbstractUser, BaseModel, PermissionsMixin):
    objects = CustomUserManager()

    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    email = models.EmailField(unique=True, help_text="이메일")

    class Meta:
        db_table = "users"  # user table 명
        app_label = "users"  # App Label

    def __str__(self):
        return self.email
