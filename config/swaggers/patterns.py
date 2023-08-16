# System
from django.urls import path, include


# Project
# v1 urls
from apps.users.urls import urlpatterns as users_urls


api_v1_patterns = [
    path("", include(users_urls)),
]
