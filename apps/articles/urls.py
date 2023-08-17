# System
from django.urls import include, path


# Project
from apps.articles.views import ArticleViewSet


service_urls = [
    path("", ArticleViewSet.as_view({"get": "get_article_list", "post": "post_article"})),
    path("<int:article_id>/", ArticleViewSet.as_view({"get": "get_article", "patch": "patch_article", "delete": "delete_article"})),
    path("self/", ArticleViewSet.as_view({"get": "get_aritcle_list_self"})),
    path("self/<int:article_id>/", ArticleViewSet.as_view({"get": "get_article_self"})),
]


urlpatterns = [
    path("api/v1/articles/", include(service_urls)),
]
