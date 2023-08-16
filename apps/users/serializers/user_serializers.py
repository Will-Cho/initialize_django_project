# System
from rest_framework import serializers


# Project
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "last_login", "date_joined"]
