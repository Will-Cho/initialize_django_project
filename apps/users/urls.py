# System
from django.urls import include, path


# Project
from apps.users.views.auth_views import AuthViewSet
from apps.users.views.user_views import UserViewSet

auth_urls = [
    path("login/", AuthViewSet.as_view({"post": "post_login"})),  # Login
    path("register/", AuthViewSet.as_view({"post": "post_register"})),  # Register
    path("refresh/", AuthViewSet.as_view({"post": "post_token_refresh"})),  # Token Refresh
]

user_urls = [
    path("", UserViewSet.as_view({"get": "get_user"})),  # Get User Own Info
]


urlpatterns = [
    path("api/v1/auth/", include(auth_urls)),
    path("api/v1/users/", include(user_urls)),
]
