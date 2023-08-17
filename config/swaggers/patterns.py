# System
from django.urls import path, include


# Project
# v1 urls
from apps.users.urls import urlpatterns as users_urls
from apps.articles.urls import urlpatterns as articles_urls


api_v1_patterns = [
    path("", include(users_urls)),
    path("", include(articles_urls)),
]
