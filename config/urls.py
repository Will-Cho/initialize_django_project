# System
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


# Project
from config.constants import SERVICE
from config.swaggers.info import api_v1_info
from config.swaggers.patterns import api_v1_patterns

schema_view_v1 = get_schema_view(
    info=api_v1_info,
    permission_classes=[AllowAny],
    patterns=api_v1_patterns,
)


urlpatterns = [
    path("", include("apps.users.urls")),
    path("admin/", admin.site.urls),
]


if SERVICE.DEBUG:
    urlpatterns += [
        re_path(r"^swagger/v1/(?P<format>\.json|\.yaml)$", schema_view_v1.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r"^swagger/v1/$", schema_view_v1.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    ]
