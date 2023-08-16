# System
from django.urls import include, path


# Project
from apps.users.views.auth_views import AuthViewSet

auth_urls = [
    path("login/", AuthViewSet.as_view({"post": "login"})),  # Login
    path("register/", AuthViewSet.as_view({"post": "register"})),  # Register
]

user_urls = []


urlpatterns = [
    path("api/v1/auth/", include(auth_urls)),
    path("api/v1/users/", include(user_urls)),
]
